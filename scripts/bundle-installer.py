#!/usr/bin/env python3
"""Bundle a Prism installer with its required platform-specific installation PDF."""
import argparse
import hashlib
import os
from pathlib import Path
import re
import tempfile
import zipfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("installer", type=Path)
args = parser.parse_args()
installer = args.installer.resolve(strict=True)
match = re.fullmatch(r"Prism-\d+\.\d+\.\d+(?:-beta\.\d+)?-(Windows-x64|macOS-(?:arm64|x64))\.(exe|dmg)", installer.name)
if not match:
    parser.error("Expected Prism-<version>-Windows-x64.exe or Prism-<version>-macOS-<arch>.dmg")
platform = "Windows" if match[1].startswith("Windows") else "macOS"
if match[2] != ("exe" if platform == "Windows" else "dmg"):
    parser.error("Installer extension does not match its platform")
guide = Path(__file__).resolve().parents[1] / "docs" / "guides" / f"Prism_설치_및_실행_가이드_{platform}.pdf"
guide_bytes = guide.read_bytes()  # Missing guides must stop packaging.
if not guide_bytes.startswith(b"%PDF-"):
    parser.error(f"Invalid PDF guide: {guide}")
output = installer.with_name(installer.stem + "-Setup-Guide.zip")
fd, temporary = tempfile.mkstemp(prefix=output.name + ".", dir=output.parent)
os.close(fd)
try:
    with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as bundle:
        bundle.write(installer, installer.name)
        bundle.write(guide, guide.name)
    with zipfile.ZipFile(temporary) as bundle:
        if bundle.namelist() != [installer.name, guide.name] or bundle.testzip() is not None:
            raise RuntimeError("Invalid installer-guide bundle")
        for source in (installer, guide):
            if hashlib.sha256(bundle.read(source.name)).digest() != hashlib.sha256(source.read_bytes()).digest():
                raise RuntimeError(f"Bundle content mismatch: {source.name}")
    os.replace(temporary, output)
finally:
    if os.path.exists(temporary):
        os.unlink(temporary)
print(f"{hashlib.sha256(output.read_bytes()).hexdigest()}  {output.name}")
print(f"Verified installer + {platform} installation guide: {output}")
