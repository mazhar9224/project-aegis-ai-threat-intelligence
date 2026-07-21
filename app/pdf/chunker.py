from langchain_text_splitters import RecursiveCharacterTextSplitter


class PDFChunker:
    """Split extracted PDF text into chunks."""

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", ". ", " ", ""]
        )

    def chunk_page(self, text: str):
        return self.splitter.split_text(text)