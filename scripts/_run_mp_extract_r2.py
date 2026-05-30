#!/usr/bin/env python3
"""Run MP extraction round 2: remaining systems with proxy disabled."""
import os

# Disable proxy
for k in ["http_proxy", "https_proxy", "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "all_proxy"]:
    os.environ.pop(k, None)
os.environ["MP_API_KEY"] = "NHAsv1uw5t70lhnGs5JVroinlACL6QKv"
os.environ["NO_PROXY"] = "*"

import sys as _sys
_sys.path.insert(0, ".")
from scripts.mp_adapter import main

# Only query the systems that failed due to proxy
_sys.argv = ["mp_adapter", "--api-key", "NHAsv1uw5t70lhnGs5JVroinlACL6QKv", "-o", "data/mp-extracted-r2.json",
             "--systems", "Pu", "Fe", "Cr", "U-Mo", "U-Zr", "U-Nb", "U-Pu", "U-Pu-Zr", "SiC"]

main()
