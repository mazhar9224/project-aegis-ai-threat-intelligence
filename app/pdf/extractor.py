import fitz  # PyMuPDF
from pathlib import Path


class PDFExtractor:
    """Extract text from PDF documents."""

    def extract(self, pdf_path: Path) -> dict:
        """Extract text from each page of a PDF."""

        doc = fitz.open(pdf_path)

        pages = []

        for page_num, page in enumerate(doc, start=1):
            pages.append(
                {
                    "page": page_num,
                    "text": page.get_text("text").strip()
                }
            )

        doc.close()

        return {
            "document": pdf_path.name,
            "total_pages": len(pages),
            "pages": pages
        }