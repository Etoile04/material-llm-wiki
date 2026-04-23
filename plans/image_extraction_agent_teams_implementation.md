# Image Extraction Agent Teams - Implementation Plan

**Date**: 2026-02-19 12:10
**Goal**: Implement image extraction system using agent teams
**Approach**: Modular agents with clear responsibilities

---

## Quick Start: Test Implementation

### Step 1: Set Up Infrastructure (15 min)

```bash
# 1. Create Supabase storage bucket for images
# Run in Supabase dashboard SQL editor:

CREATE TABLE material_images (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  image_id VARCHAR(50) UNIQUE NOT NULL,
  material_id UUID,
  property_id UUID,

  -- Storage URLs
  image_url TEXT NOT NULL,
  thumbnail_url TEXT,
  image_format VARCHAR(10),

  -- Provenance
  source_literature_id VARCHAR(100),
  source_title TEXT,
  source_authors TEXT[],
  source_year INT,
  source_institution TEXT,
  source_doi TEXT,
  source_report_number VARCHAR(50),

  -- Figure info
  figure_number VARCHAR(20),
  page_number INT,
  caption TEXT,

  -- Classification
  image_type VARCHAR(20),
  property_type VARCHAR(50),

  -- Metadata
  extracted_date TIMESTAMP DEFAULT NOW(),
  extraction_confidence FLOAT,

  -- Search
  search_vector tsvector
);

CREATE INDEX idx_images_material ON material_images(material_id);
CREATE INDEX idx_images_property ON material_images(property_id);
CREATE INDEX idx_images_source ON material_images(source_literature_id);

# 2. Create storage bucket
# In Supabase dashboard: Storage > Create bucket > "material-images"
# Set to public access for handbook embedding
```

---

### Step 2: Test Agent - IMAGE FINDER (30 min)

Create `/Users/lwj04/.openclaw/workspace/agents/image_finder.py`:

```python
#!/usr/bin/env python3
"""
IMAGE FINDER Agent
Task: Extract images from PDF literature
"""

import fitz  # PyMuPDF
from pathlib import Path
import json
import hashlib
from typing import List, Dict

class ImageFinder:
    def __init__(self, output_dir: str):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def extract_images_from_pdf(self, pdf_path: str) -> List[Dict]:
        """Extract all images from PDF"""
        doc = fitz.open(pdf_path)
        images = []

        for page_num in range(len(doc)):
            page = doc[page_num]
            image_list = page.get_images()

            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                image_ext = base_image["ext"]

                # Save image
                img_hash = hashlib.md5(image_bytes).hexdigest()[:12]
                img_filename = f"img_{page_num+1}_{img_index+1}_{img_hash}.{image_ext}"
                img_path = self.output_dir / img_filename

                with open(img_path, 'wb') as f:
                    f.write(image_bytes)

                # Extract caption (text near image)
                caption = self._extract_caption(page, img)

                images.append({
                    "image_id": img_hash,
                    "source_file": Path(pdf_path).name,
                    "page_number": page_num + 1,
                    "image_index": img_index + 1,
                    "image_path": str(img_path),
                    "image_format": image_ext,
                    "caption": caption,
                    "image_size_bytes": len(image_bytes)
                })

        doc.close()
        return images

    def _extract_caption(self, page, img) -> str:
        """Extract figure caption from page"""
        # Simple heuristic: look for "Figure X.X" or "Fig." near image
        text = page.get_text()
        lines = text.split('\n')

        for i, line in enumerate(lines):
            if 'figure' in line.lower() or 'fig.' in line.lower():
                # Return next few lines as caption
                caption_lines = lines[i:i+3]
                return ' '.join(caption_lines).strip()

        return ""

    def classify_image_type(self, caption: str) -> str:
        """Classify image type based on caption"""
        caption_lower = caption.lower()

        if any(kw in caption_lower for kw in ['conductivity', 'capacity', 'expansion']):
            return 'chart'
        elif any(kw in caption_lower for kw in ['microstructure', 'sem', 'tem']):
            return 'microstructure'
        elif any(kw in caption_lower for kw in ['phase diagram', 'equilibrium']):
            return 'diagram'
        else:
            return 'figure'

    def identify_property(self, caption: str) -> str:
        """Identify material property from caption"""
        property_keywords = {
            'thermal_conductivity': ['conductivity', 'thermal'],
            'heat_capacity': ['heat capacity', 'cp'],
            'thermal_expansion': ['expansion', 'cte'],
            'swelling': ['swelling', 'volume change'],
            'density': ['density'],
            'microstructure': ['microstructure', 'grain']
        }

        caption_lower = caption.lower()
        for prop, keywords in property_keywords.items():
            if any(kw in caption_lower for kw in keywords):
                return prop

        return 'general'

if __name__ == "__main__":
    # Test with U-Mo Handbook
    finder = ImageFinder("/Users/lwj04/.openclaw/workspace/storage/images")
    pdf_path = "/path/to/U-Mo_Handbook.pdf"

    images = finder.extract_images_from_pdf(pdf_path)

    # Add classification
    for img in images:
        img['image_type'] = finder.classify_image_type(img['caption'])
        img['property_type'] = finder.identify_property(img['caption'])

    # Save results
    output_file = "/Users/lwj04/.openclaw/workspace/extractions/images_handbook.json"
    with open(output_file, 'w') as f:
        json.dump({
            "source": pdf_path,
            "total_images": len(images),
            "images": images
        }, f, indent=2)

    print(f"Extracted {len(images)} images")
    print(f"Results saved to {output_file}")
```

---

### Step 3: Test Agent - DATABASE STORE (20 min)

Create `/Users/lwj04/.openclaw/workspace/agents/database_store.py`:

```python
#!/usr/bin/env python3
"""
DATABASE STORE Agent
Task: Store images and metadata in Supabase
"""

import os
from supabase import create_client
from pathlib import Path
import json

class DatabaseStore:
    def __init__(self, supabase_url: str, supabase_key: str):
        self.client = create_client(supabase_url, supabase_key)

    def upload_image(self, image_path: str, bucket: str = "material-images") -> str:
        """Upload image to Supabase storage"""
        with open(image_path, 'rb') as f:
            image_data = f.read()

        filename = Path(image_path).name
        response = self.client.storage.from_(bucket).upload(filename, image_data)

        if response.status_code == 200:
            # Get public URL
            public_url = self.client.storage.from_(bucket).get_public_url(filename)
            return public_url
        else:
            raise Exception(f"Upload failed: {response.error_message}")

    def store_metadata(self, image_data: dict, image_url: str) -> dict:
        """Store image metadata in database"""
        record = {
            "image_id": image_data["image_id"],
            "image_url": image_url,
            "source_literature_id": image_data.get("source_file"),
            "page_number": image_data["page_number"],
            "figure_number": image_data.get("figure_number"),
            "caption": image_data["caption"],
            "image_type": image_data.get("image_type"),
            "property_type": image_data.get("property_type"),
            "extraction_confidence": image_data.get("confidence", 0.9)
        }

        response = self.client.table("material_images").insert(record).execute()
        return response.data[0]

if __name__ == "__main__":
    # Test
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")

    store = DatabaseStore(url, key)

    # Load extracted images
    with open("/Users/lwj04/.openclaw/workspace/extractions/images_handbook.json") as f:
        data = json.load(f)

    # Upload each image
    for img in data['images']:
        print(f"Uploading {img['image_path']}...")

        # Upload to storage
        image_url = store.upload_image(img['image_path'])

        # Store metadata
        record = store.store_metadata(img, image_url)
        print(f"Stored with ID: {record['id']}")
```

---

### Step 4: Test Agent - DOCUMENT UPDATER (15 min)

Create `/Users/lwj04/.openclaw/workspace/agents/document_updater.py`:

```python
#!/usr/bin/env python3
"""
DOCUMENT UPDATER Agent
Task: Update handbook with image references
"""

import re
from pathlib import Path

class DocumentUpdater:
    def __init__(self, handbook_path: str):
        self.handbook_path = Path(handbook_path)
        with open(handbook_path, 'r', encoding='utf-8') as f:
            self.content = f.read()

    def add_image_reference(self, section_title: str, image_url: str, caption: str, source: str):
        """Add image reference to section"""
        # Find section
        section_pattern = rf"(### {re.escape(section_title)}.*?)(\n###|\n##|\Z)"
        match = re.search(section_pattern, self.content, re.DOTALL)

        if match:
            section_content = match.group(1)

            # Create image block
            image_block = f"""

#### 图表参考

![{caption}]({image_url})
**图**: {caption}
*来源: {source}*

"""

            # Insert after section title
            updated_section = section_content + image_block
            self.content = self.content.replace(section_content, updated_section)

    def save(self, output_path: str = None):
        """Save updated handbook"""
        path = output_path or self.handbook_path
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.content)
        print(f"Handbook updated: {path}")

if __name__ == "__main__":
    updater = DocumentUpdater("/Users/lwj04/.openclaw/workspace/handbooks/U-Mo燃料性能手册_v2.1.md")

    # Add thermal conductivity image
    updater.add_image_reference(
        section_title="3.1.1 温度依赖关系（简化公式）",
        image_url="https://your-supabase-url/storage/v1/object/public/material-images/img_1_1_abc123.png",
        caption="热导率随温度变化曲线",
        source="Rest et al., U-Mo Fuels Handbook (ANL-09/31), Figure 2.5, page 18"
    )

    updater.save("/Users/lwj04/.openclaw/workspace/handbooks/U-Mo燃料性能手册_v2.2_with_images.md")
```

---

### Step 5: ORCHESTRATOR - Run All Agents (10 min)

Create `/Users/lwj04/.openclaw/workspace/agents/orchestrator.py`:

```python
#!/usr/bin/env python3
"""
ORCHESTRATOR Agent
Task: Coordinate image extraction workflow
"""

import subprocess
import json
from datetime import datetime

class Orchestrator:
    def __init__(self):
        self.session_id = f"img_ext_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.status = {
            "session_id": self.session_id,
            "phase": "initialization",
            "images_found": 0,
            "images_stored": 0,
            "handbook_updated": False
        }

    def run_agent(self, agent_name: str, command: str):
        """Run agent and capture output"""
        print(f"[{agent_name}] Running...")
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"[{agent_name}] Error: {result.stderr}")
        return result.returncode == 0

    def execute_workflow(self, pdf_path: str):
        """Execute complete workflow"""

        # Phase 1: Find images
        self.status["phase"] = "image_finding"
        success = self.run_agent(
            "IMAGE_FINDER",
            f"python3 agents/image_finder.py --pdf {pdf_path}"
        )

        if not success:
            return False

        # Phase 2: Store in database
        self.status["phase"] = "database_storing"
        success = self.run_agent(
            "DATABASE_STORE",
            "python3 agents/database_store.py"
        )

        if not success:
            return False

        # Phase 3: Update handbook
        self.status["phase"] = "document_updating"
        success = self.run_agent(
            "DOCUMENT_UPDATER",
            "python3 agents/document_updater.py"
        )

        if not success:
            return False

        # Complete
        self.status["phase"] = "completed"
        self.status["handbook_updated"] = True
        print("\n✅ Workflow completed successfully!")
        return True

if __name__ == "__main__":
    orchestrator = Orchestrator()
    pdf_path = "/path/to/U-Mo_Handbook.pdf"

    success = orchestrator.execute_workflow(pdf_path)

    # Save status
    with open(f"logs/session_{orchestrator.session_id}.json", 'w') as f:
        json.dump(orchestrator.status, f, indent=2)
```

---

## Testing Plan

### Test Case 1: Single PDF (U-Mo Handbook)

**Input**: U-Mo Fuels Handbook (ANL-09/31)

**Expected Results**:
- ✅ 30+ images extracted
- ✅ Images uploaded to Supabase
- ✅ Metadata stored in database
- ✅ Handbook v2.2 created with image links

**Test Command**:
```bash
cd /Users/lwj04/.openclaw/workspace
python3 agents/orchestrator.py --pdf /path/to/U-Mo_Handbook.pdf
```

**Validation**:
```bash
# Check database
psql -c "SELECT count(*) FROM material_images;"

# Check storage
curl https://your-supabase-url/storage/v1/object/public/material-images/

# Check handbook
grep -c "!\[" handbooks/U-Mo燃料性能手册_v2.2_with_images.md
```

---

## Production Deployment

### Process All Zotero PDFs

```bash
#!/bin/bash
# process_all_pdfs.sh

ZOTERO_DIR="/path/to/zotero/pdfs"
LOG_FILE="logs/batch_processing.log"

for pdf in "$ZOTERO_DIR"/*.pdf; do
    echo "Processing: $pdf" >> "$LOG_FILE"
    python3 agents/orchestrator.py --pdf "$pdf" >> "$LOG_FILE" 2>&1
done

echo "Batch processing complete" >> "$LOG_FILE"
```

---

## Quality Assurance

### Validation Checklist

- [ ] All images extracted correctly
- [ ] Image quality acceptable (resolution > 150 DPI)
- [ ] Captions extracted accurately
- [ ] Property classifications correct (>90% accuracy)
- [ ] Database records created
- [ ] Image URLs accessible
- [ ] Handbook renders correctly with images
- [ ] Cross-references work
- [ ] No duplicate images
- [ ] Source attribution complete

---

## Estimated Timeline

| Phase | Duration | Deliverable |
|-------|----------|-------------|
| Infrastructure setup | 15 min | Supabase schema + storage |
| Agent development | 60 min | 4 working agents |
| Testing (single PDF) | 20 min | Validated v2.2 handbook |
| Batch processing | 30 min | All handbooks updated |
| Documentation | 15 min | User guide |
| **Total** | **2.5 hours** | **Production system** |

---

## Next Actions

1. **Now**: Set up Supabase infrastructure
2. **Next**: Implement IMAGE FINDER agent
3. **Then**: Test with U-Mo Handbook
4. **Finally**: Deploy to all materials

---

*Implementation Plan: 2026-02-19 12:10*
*Ready to start: Yes*
