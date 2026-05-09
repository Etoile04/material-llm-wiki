# skills/llm-wiki/scripts/slug_utils.py
"""
Slug sanitization utilities for llm-wiki knowledge base.
Ensures all slugs are filesystem-safe and deterministic.
"""
import re

# Maximum slug length (filesystem-safe)
MAX_SLUG_LEN = 80


def sanitize_slug(raw_name: str) -> str:
    """
    Convert a raw directory name into a filesystem-safe slug.
    
    Rules:
    1. If the name looks like a DOI slug (starts with 10_xxxx), keep as-is
    2. Replace spaces, commas, parentheses, and non-ASCII with underscores
    3. Collapse multiple underscores
    4. Trim to MAX_SLUG_LEN
    5. Preserve trailing _hash suffix (e.g., _06dff417)
    """
    # DOI slugs: starts with "10_" followed by digits/underscores — keep as-is
    if re.match(r'^10_[\d_]+', raw_name[:20]):
        return raw_name[:MAX_SLUG_LEN]
    
    # Preserve trailing hash suffix like _06dff417
    hash_suffix = ""
    hash_match = re.search(r'_([a-f0-9]{6,8})$', raw_name)
    if hash_match:
        hash_suffix = hash_match.group(0)
        raw_name = raw_name[:hash_match.start()]
    
    # Replace problematic characters
    slug = raw_name
    slug = re.sub(r'[^\x00-\x7F]+', '', slug)
    slug = re.sub(r'[,\s()\[\]{}"\'`:+!?&|<>]', '_', slug)
    slug = re.sub(r'_+', '_', slug)
    slug = slug.strip('_')
    
    if hash_suffix:
        slug = slug + hash_suffix
    
    if len(slug) > MAX_SLUG_LEN:
        if hash_suffix and slug.endswith(hash_suffix):
            base = slug[:MAX_SLUG_LEN - len(hash_suffix)]
            slug = base.rstrip('_') + hash_suffix
        else:
            slug = slug[:MAX_SLUG_LEN].rstrip('_')
    
    return slug


def is_doi_slug(slug: str) -> bool:
    """Check if a slug is DOI-based (already safe)."""
    return bool(re.match(r'^10_[\d_]+', slug))


if __name__ == "__main__":
    test_cases = [
        "10_1016_j_jnucmat_2020_152317",
        "An atomistic study of defect energetics and diffusion with respect to compositio_06dff417",
        "Kim, Hofman, Cheon_2013_Recrystallization and fission-gas-bubble swelling of U-Mo fuel",
        "Yun 等 - Investigation of swelling behaviors of U-10Zr meta",
        "TRANSFORMATION CHARACTERISTICS OF U-Mo AND U-Mo-Ti ALLOYS_b2a56895",
        "beeler_et_al._2021_radiation_driven_diffusion_in_γu-mo_2_",
        "R.M. WILLARD_A.R. SCHMITT_1985_Irradiation Swelling, Phase Reversion, and Intergranular Cracking of U-10 wt %",
    ]
    all_ok = True
    for tc in test_cases:
        result = sanitize_slug(tc)
        safe = all(c.isalnum() or c in '-_.' for c in result)
        if not safe:
            all_ok = False
        print(f"{'OK' if safe else 'FAIL'} {tc[:50]:50s} -> {result[:60]}")
    
    if not all_ok:
        raise SystemExit(1)
    print("\nAll tests passed!")
