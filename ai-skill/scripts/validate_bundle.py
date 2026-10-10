#!/usr/bin/env python3
"""Validate native research-bundle artifacts; NOT a master-contract certification."""
import hashlib, json, pathlib, sys
root = pathlib.Path(__file__).resolve().parents[2]
index = json.loads((root / "ai-skill/generated/research-bundle-index.json").read_text())
manifest = json.loads((root / "ai-skill/manifest.json").read_text())
errors = []
if manifest.get("master_contract_0_3_1") != "IMPLEMENTED":
    errors.append("master contract adapter missing")
artifacts = index.get("artifacts")
if not isinstance(artifacts, list):
    errors.append("native index lacks artifact list; manual migration required")
else:
    seen = set()
    for a in artifacts:
        p = a.get("path")
        if not isinstance(p, str) or not p or p in seen:
            errors.append("invalid or duplicate artifact path: " + repr(p))
            continue
        seen.add(p)
        target = (root / p).resolve()
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            errors.append("missing or unsafe artifact: " + p)
            continue
        raw = target.read_bytes()
        if "bytes" in a and len(raw) != a["bytes"]:
            errors.append("byte-count mismatch: " + p)
        if "sha256" in a and hashlib.sha256(raw).hexdigest() != a["sha256"]:
            errors.append("sha256 mismatch: " + p)
if errors:
    print("\n".join(errors))
    sys.exit(1)
print("PASS: native artifact checks; native integrity; fleet contract replay follows")

import runpy
runpy.run_path(str(root / "ai-skill/scripts/fleet_contract.py"))["replay"]()
