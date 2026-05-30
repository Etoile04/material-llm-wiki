#!/usr/bin/env python3
"""Run MP extraction with API key."""
import os, json, sys as _sys

# Set API key before importing mp_adapter
os.environ["MP_API_KEY"] = "NHAsv1uw5t70lhnGs5JVroinlACL6QKv"

_sys.path.insert(0, ".")

# Use argparse-style main instead
from scripts.mp_adapter import main

# Inject args
_sys.argv = ["mp_adapter", "--api-key", "NHAsv1uw5t70lhnGs5JVroinlACL6QKv", "-o", "data/mp-extracted.json"]

main()
