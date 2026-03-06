def file_content():
    file_list = []
    file_path = r"C:\Users\nithi\Desktop\My Projects\Learning\PythonLearning1\Code_Verifier_Agent\RAG Tuturial\policy.txt"
    with open(file_path,'r') as file:
        for line in file:
            file_list.append(line)
    return file_list
