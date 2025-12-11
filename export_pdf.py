from pathlib import Path
from playwright.sync_api import sync_playwright


def main() -> None:
    project_root = Path(__file__).resolve().parent
    html_path = project_root / "my.htm"
    pdf_path = project_root / "page.pdf"

    if not html_path.exists():
        raise FileNotFoundError(f"HTML file not found: {html_path}")

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.set_default_timeout(120_000)

        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.emulate_media(media="screen")
        page.wait_for_timeout(1_000)

        page.pdf(path=str(pdf_path), print_background=True)
        browser.close()

    print(f"Saved PDF to {pdf_path}")


if __name__ == "__main__":
    main()
