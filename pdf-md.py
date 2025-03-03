import os
import fitz
import pytesseract
from PIL import Image
from tkinter import Tk, filedialog

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def merge_pdfs(pdf_list, output_filename):
    from PyPDF2 import PdfMerger
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as: {output_filename}")

def extract_text_or_ocr(pdf_path):
    doc = fitz.open(pdf_path)
    md_text = ""

    for i, page in enumerate(doc):
        text = page.get_text("text").strip()

        if not text:  # If no text is found, apply OCR
            img_list = page.get_pixmap()  # Convert PDF page to image
            img = Image.frombytes("RGB", [img_list.width, img_list.height], img_list.samples)
            text = pytesseract.image_to_string(img).strip()

        md_text += f"\n## Page {i+1}\n{text if text else '[No text detected]'}\n"

    md_filename = os.path.splitext(pdf_path)[0] + ".md"
    with open(md_filename, "w", encoding="utf-8") as md_file:
        md_file.write(md_text)

    print(f"Markdown file saved as: {md_filename}")

def select_files():
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])
    return list(file_paths)

if __name__ == "__main__":
    pdf_files = select_files()
    if not pdf_files:
        print("No files selected.")
    else:
        merged_pdf = "merged_output.pdf"
        merge_pdfs(pdf_files, merged_pdf)
        extract_text_or_ocr(merged_pdf)
