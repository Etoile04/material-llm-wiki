#!/usr/bin/env python3
"""Debug: check bulk_modulus structure in summary."""
from mp_api.client import MPRester

key = "NHAsv1uw5t70lhnGs5JVroinlACL6QKv"

with MPRester(key) as mpr:
    docs = mpr.materials.summary.search(
        chemsys="U",
        fields=["material_id", "bulk_modulus", "shear_modulus"],
    )
    for doc in docs[:3]:
        print(f"\n{doc.material_id}:")
        bm = getattr(doc, "bulk_modulus", None)
        sm = getattr(doc, "shear_modulus", None)
        print(f"  bulk_modulus type: {type(bm)}, value: {bm}")
        print(f"  shear_modulus type: {type(sm)}, value: {sm}")
        if bm is not None:
            for attr in dir(bm):
                if not attr.startswith('_'):
                    print(f"    bm.{attr} = {getattr(bm, attr, '?')}")
