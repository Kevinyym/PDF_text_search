import os
import re
import PyPDF2

def search_pdfs(pdf_files, search_string):
    results = []
    for pdf_file in pdf_files:
        if search_in_pdf(pdf_file, search_string):
            results.append(os.path.basename(pdf_file))
    return results

def search_in_pdf(pdf_file, search_string):
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if re.search(search_string, text, re.IGNORECASE):
                return True
    return False

def save_results(results, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for result in results:
            file.write(f"{result}\n")
    return output_file
