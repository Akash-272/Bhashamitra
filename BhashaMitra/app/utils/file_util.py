
import os

def save_uploaded_file(uploaded_file, save_dir="uploads"):
    """Save uploaded file to a specified directory."""
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    file_path = os.path.join(save_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

def read_file(file_path):
    """Read content from a text or PDF file."""
    if file_path.endswith(".txt"):
        with open(file_path, "r") as file:
            return file.read()
    elif file_path.endswith(".pdf"):
        from app.services.document_processing import extract_text_from_pdf
        return extract_text_from_pdf(file_path)
    else:
        raise ValueError("Unsupported file type")

def delete_file(file_path):
    """Delete a file from the system."""
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False
