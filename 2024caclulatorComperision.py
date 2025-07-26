import pymupdf

doc = pymupdf.open("vit25.pdf")

page = doc.load_page(0)

blocks = page.get_text()

print(blocks)

#2025: navn, kode (omvendt rekkefølge), termin, bestått, viser ikke poeng når man ikke har poeng 
#poeng vises feil 