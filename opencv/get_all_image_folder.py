import os

def get_files_in_folder(folder_path):
    file_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))

    return file_list


folder_path = "C:\\Users\\leowu\\Documents\\source_code\\handout\\image_process\\opencv\\image"
files = get_files_in_folder(folder_path)

for f in files:
    print(f)
