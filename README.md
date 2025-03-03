# PDF to Markdown Converter

This script allows users to merge selected PDF documents into a single file and extract their content into a Markdown (`.md`) file. If the PDF contains non-selectable text (such as scanned pages), Optical Character Recognition (OCR) is applied to extract text.

## Features
- **Merge Multiple PDFs**: Combines multiple selected PDFs into one.
- **Text Extraction**: Extracts text from PDF pages.
- **OCR Processing**: Uses Tesseract OCR to recognise text in scanned images if no selectable text is found.
- **Markdown Conversion**: Saves the extracted content as a Markdown file.

## Prerequisites
Ensure you have the following dependencies installed:

- Python 3
- Required Python packages:
  ```sh
  pip install pymupdf pytesseract pillow pypdf2
  ```
- Tesseract OCR installed (Download from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)).
  - On Windows, set the `pytesseract.pytesseract.tesseract_cmd` path in the script:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```

## Usage
1. Run the script:
   ```sh
   python pdf-md.py
   ```
2. Select multiple PDF files in the file selection dialogue.
3. The selected PDFs will be merged into a file named `merged_output.pdf`.
4. The script extracts text from the merged PDF and saves it as `merged_output.md`.
5. If any pages contain images instead of text, OCR is applied to extract the text.

## Output
- `merged_output.pdf`: The merged PDF containing all selected files.
- `merged_output.md`: The Markdown file containing extracted text with page numbers.

## Notes
- If a page contains no text, OCR is applied automatically.
- If OCR fails to detect text, `[No text detected]` is added to the output.
- The script uses `Tkinter` for file selection, which requires a GUI environment.

## Licence
This project is licensed under the [MIT Licence](https://opensource.org/licenses/MIT) and is open source. Contributions are welcome.
