from pathlib import Path
def file_content():
    document = []
    folder_path = Path(
        r"C:\Users\nithi\Desktop\My Projects\Learning\PythonLearning1\RAG Tuturial\HR_Policy_Documents"
    )
    for file in folder_path.iterdir():
        if file.is_file():
            print(file.name, file.suffix)
            try:
                if file.suffix == ".txt":
                    with open(file, 'r') as f:
                        doc_text = f.read()
                document.append(
                    {
                        "text": doc_text,
                        "Source": file.name,
                        "Type": file.suffix
                    }
                )
            except Exception as e:
                print(f"{file.name} skipped {e}")
    return document

file_content()







