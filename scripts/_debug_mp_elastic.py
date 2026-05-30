#!/usr/bin/env python3
"""Debug: check MP elasticity endpoint structure."""
from mp_api.client import MPRester
import os

key = "NHAsv1uw5t70lhnGs5JVroinlACL6QKv"

with MPRester(key) as mpr:
    # Try U (mp-108) which we know has elasticity
    docs = mpr.materials.elasticity.search(material_ids=["mp-108"])
    if docs:
        ed = docs[0]
        print(f"Type: {type(ed)}")
        print(f"Fields: {[a for a in dir(ed) if not a.startswith('_')]}")
        print()
        
        for attr in ["elastic_tensor", "elastic_tensor_voigt", "k_vrh", "g_vrh",
                      "bulk_modulus_vrh", "shear_modulus_vrh", "homogeneous_poisson",
                      "universal_anisotropy"]:
            val = getattr(ed, attr, "NOT FOUND")
            print(f"  {attr}: {val}")
            if hasattr(val, '__iter__') and not isinstance(val, str):
                try:
                    l = list(val)
                    print(f"    -> as list: {l[:2]}...")
                except:
                    pass
    else:
        print("No elasticity data for mp-108")
    
    # Also try Mo
    docs2 = mpr.materials.elasticity.search(material_ids=["mp-9947"])
    if docs2:
        ed2 = docs2[0]
        print(f"\nMo (mp-9947) type: {type(ed2)}")
        for attr in ["elastic_tensor", "k_vrh", "g_vrh"]:
            val = getattr(ed2, attr, "NOT FOUND")
            print(f"  {attr}: {val}")
