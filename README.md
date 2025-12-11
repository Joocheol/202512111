# HTML to PDF export helper

This repo contains an HTML snapshot (`my.htm` and supporting assets in `my_files/`) and a helper script for exporting it to PDF without committing large binary files.

## Setup
1. (Optional) Create and activate a virtual environment.
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
3. On Debian/Ubuntu you may need system libraries for headless Chromium:
   ```bash
   sudo apt-get update
   sudo apt-get install -y \
     libatk1.0-0 libatk-bridge2.0-0 libdrm2 libxkbcommon0 libgtk-3-0 \
     libnss3 libnspr4 libx11-xcb1 libxdamage1 libxcomposite1 libxfixes3 \
     libxrandr2 libgbm1 libcups2 libglib2.0-0 libasound2t64
   ```

## Usage
Run the helper script to produce `page.pdf` (ignored via `.gitignore`):
```bash
python export_pdf.py
```
You should see a message like `Saved PDF to /path/to/page.pdf`, and the file will appear in the
repository root.
