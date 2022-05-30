# FixOCR

## Setup

1. Install tesseract (`tesseract` in MacPorts and Homebrew, `tesseract-ocr` in Ubuntu)
2. Install tesseract language data (`tesseract-eng` in MacPorts for English data)
3. Install pkg-config (`pkgconfig` in MacPorts, `pkg-config` in Homebrew and Ubuntu)
4. Install poetry (`python -m pip install poetry` or `python3 -m pip install poetry`)
5. Clone and enter this repository: `git clone git@github.com:gmarmstrong/FixOCR && cd FixOCR`
6. Install dependencies from `poetry.lock`: `poetry install`
7. Run the app: `poetry run python -m app`
