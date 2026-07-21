import json
from pathlib import Path

from app.pdf.chunker import PDFChunker

INPUT_DIR = Path("data/extracted")
OUTPUT_DIR = Path("data/chunks")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    chunker = PDFChunker()

    files = list(INPUT_DIR.glob("*.json"))

    if not files:
        print("No extracted JSON files found.")
        return

    for file in files:

        with open(file, "r", encoding="utf-8") as f:
            document = json.load(f)

        chunks = []

        chunk_number = 1

        for page in document["pages"]:

            page_chunks = chunker.chunk_page(page["text"])

            for chunk in page_chunks:

                chunks.append({
                    "id": f"{file.stem}-{chunk_number}",
                    "document": document["document"],
                    "page": page["page"],
                    "chunk": chunk_number,
                    "text": chunk
                })

                chunk_number += 1

        output = OUTPUT_DIR / f"{file.stem}_chunks.json"

        with open(output, "w", encoding="utf-8") as f:
            json.dump(chunks, f, indent=2, ensure_ascii=False)

        print(f"Created {len(chunks)} chunks from {file.name}")

    print("\nChunking completed.")


if __name__ == "__main__":
    main()