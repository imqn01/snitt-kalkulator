# "Snitt-kalkulator"
The purpose of this project is to create a website that automatically calculates a person’s grade average based on their uploaded diploma. 

Progress: 
- Created the calculation program
- Created the API
- Created a temporary solution to display a readable version of the grade average in the terminal 

What is left to do:
- Make tests 
- Create Frontend
# Important information regarding accepting pdf-files
By using the files in the “pdf_parser_information” folder, it became apparent that websites like Studentweb and Vitnemålsportalen differ in how the information in transcript records is formatted, even if they appear identical.
For the time being, this project works exclusively with signed diplomas from Vitnemålsportalen.

# How to use the calculator 
To use this calculator for the time being, pymupdf needs to be downloaded.
### Step 1: Get the correct diploma files
1. Go to [Vitnemålsportalen](https://www.vitnemalsportalen.no) and log in.
2. Go to my results and choose those classes you want to include in the calculation.
3. Follow the steps and use your own email as recipient. 
4. Open the link sent in the email.
5. Go to the bottom of the page an click on "Signed document with selected results (PDF)" / "Signert dokument med valgte resultater (PDF)"

The acquired pdf-version can be used in this project.

### Step: 2 Get your calculated grade average in the terminal 
1. Download the project. 
2. Move the acquired pdf from Step 1 into the project folder
3. Insert the pdf-name where the "INSERT PDF HERE" comment is at the bottom of the page in [the calculator](scr/calculator.py). The first line in the terminal displays your grade average: {'average_grade': x.xx}

