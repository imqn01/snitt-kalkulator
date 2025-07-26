import fitz  # pymupdf

filnavn = "2024.pdf"

try:
    doc = fitz.open(filnavn)
    print(f"Antall sider i PDF: {len(doc)}")
    for page in doc:
        blocks = page.get_text("blocks", sort=True)
        print(f"Side {page.number + 1}: {len(blocks)} tekstblokker")
except Exception as e:
    print(f"Feil ved lesing av PDF: {e}")