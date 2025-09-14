from fastapi import FastAPI, UploadFile, File, HTTPException
import os
from needed_pdf_structure.scr.calculator import calculate_grade_average

app = FastAPI()

@app.post("/calculate-average")
async def calculate_average(pdf: UploadFile = File(...)):
    if not pdf.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed,")
    tmp_path = f"temp_{pdf.filename}"
    with open(tmp_path, "wb") as buffer:
        buffer.write(await pdf.read())
    
    try:
        average = calculate_grade_average(tmp_path)
    finally: 
        os.remove(tmp_path)
    if average is None: 
        raise HTTPException(status_code=400, detail="No valid courses found in the file.")
    return average