import pymupdf

doc = pymupdf.open("tester20.pdf") #INSERT PDF HERE

page = doc.load_page(0)

blocks = page.get_text("blocks", sort = True)

grade_characters = {"A":5, "B":4, "C":3, "D":2, "E":1}

for block in blocks: 
    text = block[4].strip()
    lines = text.split("\n")
    if len(lines) >=5:
        studypoint = lines[3].replace(",", ".").replace("stp", "").strip()
        grade = lines[4].strip()
        if grade in grade_characters and studypoint !="-":
            studypoint = float(studypoint)
            emnekode = lines[0]
            emnenavn = lines[1]
            termin = lines[2]
            average = studypoint * grade_characters[grade]
            print(f"{emnekode} {emnenavn} ({termin}): {studypoint} {grade}: {average} \n")
            
            