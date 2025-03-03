@echo off
echo ==========================================
echo PDF to Markdown Converter - Setup Script
echo ==========================================
echo.
echo Step 1: Installing required Python packages...
pip install pymupdf pytesseract pillow pypdf2
echo.
echo Step 2: Downloading Tesseract OCR
echo ------------------------------------------
echo Tesseract OCR is required for OCR processing.
echo The official download page will now open.
echo Please download and install it before proceeding.
start "" "https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.0"
echo.
echo Step 3: Configuring Tesseract OCR
echo ------------------------------------------
echo After installation, ensure Tesseract is installed in:
echo C:\Program Files\Tesseract-OCR\
echo If installed elsewhere, update the script path in pdf-md.py.
echo.
echo Setup complete. Press any key to exit...
pause
