import json
from pathlib import Path

from app.pdf.extractor import PDFExtractor


PDF_DIR = Path("data/pdfs")
OUTPUT_DIR = Path("data/extracted")


def main():

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    extractor = PDFExtractor()

    pdf_files = list(PDF_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in data/pdfs")
        return

    print(f"Found {len(pdf_files)} PDF(s)\n")

    for pdf in pdf_files:

        print(f"Processing {pdf.name}")

        result = extractor.extract(pdf)

        output_file = OUTPUT_DIR / f"{pdf.stem}.json"

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)

        print(f"Saved {output_file.name}")

    print("\nDone!")


if __name__ == "__main__":
    main()