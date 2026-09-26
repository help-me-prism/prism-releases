# Release packaging

- Every user-facing Prism download must be a `Prism-<version>-<platform>-Setup-Guide.zip` containing the installer and the matching installation guide PDF from `docs/guides/`.
- Use `python3 scripts/bundle-installer.py /path/to/installer` and verify the ZIP before uploading. A missing guide must stop publication.
- README and release-note download buttons must link to the installer-guide ZIP. Standalone installers may remain for existing clients and checksum verification, but must not be the primary download links.
- Update release assets, SHA256SUMS.txt, release-manifest.json, channels/beta.json (or stable.json), README and release notes together. Preserve assets for platforms outside the requested update.
- Record the exact application source commit and verify uploaded sizes and SHA-256 digests. Do not claim notarization for ad-hoc signed Mac builds.
