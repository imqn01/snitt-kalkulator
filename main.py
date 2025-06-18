import pymupdf
import os

GRADE_POINTS = {"A":5, "B":4, "C":3, "D":2, "E":1}

def parse_block(block):
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
        return None
    return None
def calculate_grade_average(pdf_path, verbose=False):
    if not os.path.exists(pdf_path):
        return {"error": f"Cannot find PDF: {pdf_path}"}
    
    total_points = 0 
    total_weight = 0
    results = []
    
    with pymupdf.open(pdf_path) as doc: 
        for page in doc: 
            blocks = page.get_text("blocks", sort = True)
            for block in blocks:
                course = parse_block(block)
                if course: 
                    grade_value = GRADE_POINTS[course["grade"]]
                    weight = grade_value * course["studypoints"]
                    total_weight += weight
                    total_points += course["studypoints"]
                    results.append({
                        "code": course["code"],
                        "name": course["name"],
                        "term": course["term"],
                        "studypoints": course["studypoints"],
                        "grade": course["grade"],
                        "weight": round(weight, 2)
                        
                    })
                    if verbose: 
                        print(f"{course['code']} {course['name']} ({course['term']}): "
                        f"{course['studypoints']} stp, karakter {course['grade']} → {weight:.1f} poeng")
    if total_points <=0: 
        return{"error":"No valid courses found"}
    total_average = round(total_weight/total_points, 2)
    return {
        "Total average": total_average,
        "Courses": results
            }

average = calculate_grade_average("testVit.pdf")
if average is not None: 
    print(f"Totalt snitt: {average}")