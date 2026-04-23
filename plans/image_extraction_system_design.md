# Material Property Image Extraction System Design

**Date**: 2026-02-19 11:57
**Goal**: Enhance extraction system to capture, store, and reference material property images
**Approach**: Agent Teams with specialized roles

---

## Current Gap

**Problem**: Material handbooks lack image URLs, making it difficult to:
- Visualize property trends (charts, graphs)
- Verify data from original sources
- Access experimental results visually

**Impact**: Reduced handbook utility for researchers

---

## System Architecture

### Agent Team Structure

```
┌─────────────────────────────────────────────────────┐
│         ORCHESTRATOR AGENT (Coordinator)             │
│  - Manages workflow                                  │
│  - Tracks progress                                   │
│  - Reports completion                                │
└──────────────┬──────────────────────────────────────┘
               │
       ┌───────┴────────┬─────────────┬──────────────┐
       │                │             │              │
   ┌───▼────┐      ┌───▼────┐    ┌──▼───┐      ┌──▼───┐
   │ IMAGE  │      │  META  │    │ DB   │      │ DOC  │
   │FINDER  │      │EXTRACT │    │STORE │      │UPDATE│
   └────────┘      └────────┘    └──────┘      └──────┘
```

---

## Agent Roles & Responsibilities

### 1. **IMAGE FINDER Agent**
**Task**: Scan PDF literature for material property images

**Capabilities**:
- PDF parsing (pdftotext + image extraction)
- Image classification (charts, graphs, microstructures)
- Property type identification
- OCR for chart labels and data

**Output**:
```json
{
  "image_id": "img_001",
  "source_file": "U-Mo_Handbook_ANL-09-31.pdf",
  "page_number": 18,
  "figure_number": "Figure 2.5",
  "image_type": "chart",
  "property_type": "thermal_conductivity",
  "material": "U-10Mo",
  "description": "Thermal conductivity vs temperature",
  "image_path": "/storage/images/img_001.png",
  "confidence": 0.95
}
```

---

### 2. **METADATA EXTRACTOR Agent**
**Task**: Extract provenance information

**Capabilities**:
- Extract literature metadata (title, authors, year, DOI)
- Identify figure/table captions
- Parse axis labels and units
- Extract data points from charts (if possible)

**Output**:
```json
{
  "provenance": {
    "literature_id": "ANL-09-31",
    "title": "U-Mo Fuels Handbook",
    "authors": ["Rest, J.", "Hofman, G.L."],
    "year": 2006,
    "institution": "Argonne National Laboratory",
    "doi": null,
    "report_number": "ANL-09/31"
  },
  "figure_info": {
    "caption": "Thermal conductivity of U-10Mo alloy",
    "figure_number": "2.5",
    "page": 18,
    "data_source": "Table 2.3"
  },
  "property_details": {
    "property_name": "thermal_conductivity",
    "units": "W/(m·K)",
    "temperature_range": "25-1000°C",
    "material_composition": "U-10Mo"
  }
}
```

---

### 3. **DATABASE STORE Agent**
**Task**: Store images and metadata in Supabase

**Schema Design**:

```sql
-- Images table
CREATE TABLE material_images (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  image_id VARCHAR(50) UNIQUE NOT NULL,
  material_id UUID REFERENCES materials(id),
  property_id UUID REFERENCES properties(id),
  
  -- Storage
  image_url TEXT NOT NULL,  -- Supabase storage URL
  thumbnail_url TEXT,
  image_format VARCHAR(10),  -- png, jpg, svg
  
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
  image_type VARCHAR(20),  -- chart, graph, microstructure, table
  property_type VARCHAR(50),
  
  -- Metadata
  extracted_date TIMESTAMP DEFAULT NOW(),
  extraction_confidence FLOAT,
  extraction_agent VARCHAR(50),
  
  -- Full-text search
  search_vector tsvector
);

-- Create indexes
CREATE INDEX idx_images_material ON material_images(material_id);
CREATE INDEX idx_images_property ON material_images(property_id);
CREATE INDEX idx_images_source ON material_images(source_literature_id);
```

**Operations**:
- Upload image to Supabase Storage
- Create database record with metadata
- Generate thumbnail for handbook display
- Update property records to link images

---

### 4. **DOCUMENT UPDATER Agent**
**Task**: Update handbooks with image references

**Capabilities**:
- Markdown generation
- Image embedding with captions
- Cross-reference linking
- Table of figures generation

**Output** (Markdown snippet):
```markdown
### 3.1.1 Thermal Conductivity

#### Figure Reference
![Thermal Conductivity vs Temperature](https://supabase.example.com/storage/v1/object/public/images/img_001.png)
**Figure 3.1**: Thermal conductivity of U-10Mo alloy as a function of temperature.
*Source: Rest et al., U-Mo Fuels Handbook (ANL-09/31), Figure 2.5, page 18*

**Data Table**:
| Temperature (°C) | k (W/m·K) | Reference |
|------------------|-----------|-----------|
| 25 | 11.4 | Figure 3.1 |
| 100 | 12.7 | Figure 3.1 |

**Related Images**:
- [Figure 3.2](#): Thermal diffusivity comparison
- [Figure 3.3](#): Heat capacity vs temperature
```

---

### 5. **ORCHESTRATOR Agent**
**Task**: Coordinate workflow and report progress

**Workflow**:
```
1. Initiate extraction → IMAGE FINDER
2. On image found → METADATA EXTRACTOR
3. On metadata ready → DATABASE STORE
4. On DB stored → DOCUMENT UPDATER
5. On document updated → QA VALIDATOR
6. Report completion
```

**Progress Tracking**:
```json
{
  "session_id": "img_ext_2026_02_19_001",
  "status": "in_progress",
  "total_pdfs": 13,
  "pdfs_processed": 3,
  "images_found": 47,
  "images_stored": 32,
  "handbook_updated": false,
  "errors": [],
  "eta": "2026-02-19 14:30:00"
}
```

---

## Implementation Plan

### Phase 1: Infrastructure Setup (1 hour)
1. ✅ Create Supabase storage bucket for images
2. ✅ Create database schema (material_images table)
3. ✅ Set up API endpoints for image upload
4. ✅ Configure image thumbnails generation

### Phase 2: Agent Development (2-3 hours)
1. ✅ IMAGE FINDER: PDF parsing + image extraction
2. ✅ METADATA EXTRACTOR: Literature metadata extraction
3. ✅ DATABASE STORE: Supabase integration
4. ✅ DOCUMENT UPDATER: Markdown generation
5. ✅ ORCHESTRATOR: Workflow coordination

### Phase 3: Testing & Validation (1 hour)
1. ✅ Test on single PDF (U-Mo Handbook)
2. ✅ Validate image extraction accuracy
3. ✅ Verify database storage
4. ✅ Check handbook rendering
5. ✅ User acceptance testing

### Phase 4: Production Deployment (30 min)
1. ✅ Process all Zotero PDFs
2. ✅ Update all handbooks
3. ✅ Generate extraction report
4. ✅ Documentation

---

## Test Case: U-Mo Handbook

**Input**:
- PDF: U-Mo Fuels Handbook (ANL-09/31)
- Expected images: ~30 charts/figures

**Expected Output**:
```json
{
  "images_extracted": 30,
  "property_types": [
    "thermal_conductivity",
    "heat_capacity",
    "thermal_expansion",
    "swelling",
    "microstructure"
  ],
  "storage_used": "2.5 MB",
  "handbook_sections_updated": 8,
  "processing_time": "45 seconds"
}
```

---

## Benefits

1. **Visual Verification**: Researchers can see original charts
2. **Data Traceability**: Every image linked to source
3. **Quick Reference**: Thumbnails in handbooks
4. **Search Enhancement**: Image-based property search
5. **Quality Assurance**: Visual validation of extracted data

---

## Technical Stack

- **PDF Processing**: `pdftotext`, `pdf2image`, `PyMuPDF`
- **Image Analysis**: `OpenCV`, `PIL`, `matplotlib`
- **OCR**: `Tesseract`, `EasyOCR`
- **Database**: Supabase (PostgreSQL + Storage)
- **Agent Framework**: Python asyncio + custom orchestrator
- **Storage**: Supabase Storage (S3-compatible)

---

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Image extraction errors | Medium | Confidence scoring + human review |
| Large storage usage | Low | Thumbnail generation + compression |
| OCR inaccuracy | Medium | Manual validation for key figures |
| Processing time | Low | Parallel processing + caching |

---

## Success Metrics

1. **Extraction Rate**: >95% of figures captured
2. **Accuracy**: >90% correct property classification
3. **Coverage**: All major property types have images
4. **User Satisfaction**: Researchers can find images quickly
5. **Time Savings**: <30 min to process 1 PDF

---

## Next Steps

1. **Immediate**: Set up Supabase schema and storage
2. **Short-term**: Develop IMAGE FINDER agent
3. **Medium-term**: Complete all agents and test
4. **Long-term**: Deploy to production for all materials

---

*Design Date: 2026-02-19 11:57*
*Estimated Implementation: 4-5 hours*
