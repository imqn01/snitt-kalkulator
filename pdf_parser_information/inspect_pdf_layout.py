import pymupdf
filename = "" #INSERT PDF HERE

doc = pymupdf.open(filename)

page = doc.load_page(0)

blocks = page.get_text()
print("PDF-oppsett på første side av vitnemålet:\n\n" + blocks + "________________________________________\n")

try:
    doc = pymupdf.open(filename)
    print(f"Antall sider i PDF: {len(doc)}")
    for page in doc:
        blocks = page.get_text("blocks", sort=True)
        print(f"Side {page.number + 1}: {len(blocks)} tekstblokker")
except Exception as e:
    print(f"Feil ved lesing av PDF: {e}")

#2025: navn, kode (omvendt rekkefølge), termin, bestått, viser ikke poeng når man ikke har poeng 
#poeng vises feil 
