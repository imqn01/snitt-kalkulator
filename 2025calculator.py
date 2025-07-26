import pymupdf

doc = pymupdf.open("2025.pdf")

page = doc.load_page(0)

blocks = page.get_text()

print(blocks)