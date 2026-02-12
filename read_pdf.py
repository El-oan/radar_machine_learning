from pypdf import PdfReader
import sys

def read_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        print(f"Reading {file_path}...")
        print(f"Number of Pages: {len(reader.pages)}")
        
        # Read first 2 pages to get Abstract and Intro
        text = ""
        for i in range(min(2, len(reader.pages))):
            page = reader.pages[i]
            text += page.extract_text() + "\n"
            
        print("\n--- Content Snippet ---")
        print(text)
        
    except Exception as e:
        print(f"Error reading PDF: {e}")

if __name__ == "__main__":
    read_pdf("papers/pointnet.pdf")
