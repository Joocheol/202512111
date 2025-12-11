# HTML to PDF export helper

This repo contains an HTML snapshot (`my.htm` and supporting assets in `my_files/`) and a helper script for exporting it to PDF without committing large binary files.

## Setup
1. Install Python dependencies:
   ```bash
   pip install playwright
   playwright install chromium
   ```

## Usage
Run the helper script to produce `page.pdf` (ignored via `.gitignore`):
```bash
python export_pdf.py
```
