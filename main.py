import pymupdf
GRADE_POINTS = {"A":5, "B":4, "C":3, "D":2, "E":1}

def parse_block(block):
    #Extracts course data from a block 
    lines = block[4].strip().split("\n")
    if len(lines) < 5:
        return None
    try: 
        studypoint = lines[3].replace(",", ".").replace("stp", "").strip()
        grade = lines[4].strip().upper()
        if grade in GRADE_POINTS and studypoint !="-":
            return{
                "code": lines[0],
                "name": lines[1],
                "term": lines[2],
                "studypoints": float(studypoint),
                "grade": grade
            }
    except ValueError:
        pass
    return None
def calculate_grade_average(pdf_path):
    doc = pymupdf.open(pdf_path)
    page = doc.load_page(0)
    blocks = page.get_text("blocks", sort = True)
    
    total_points = 0
    total_weight = 0
    
    for block in blocks:
        course = parse_block(block)
        if course: 
            grade_value = GRADE_POINTS[course["grade"]]
            weight = grade_value * course["studypoints"]
            total_weight += weight
            total_points += course["studypoints"]
            
            print(f"{course["code"]} – {course["name"]} ({course["term"]}): "
                  f"{course["studypoints"]} stp, karakter {course["grade"]} → {weight:.1f} poeng")
    if total_points <=0: 
        print("No valid courses found")
        return
    total_average = round(total_weight/total_points, 2)
    print(total_average)
    
calculate_grade_average("2024.pdf")