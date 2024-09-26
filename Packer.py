import os
import pickle
import gzip

def Start():
    directory_path = input("Enter directory path: ")

    if not os.path.isdir(directory_path):
        print("Указанный путь не является директорией или не существует.")
        return

    with open('result.ble', 'wb') as archive:
        for root, dirs, files in os.walk(directory_path):
            currentFolder = os.path.relpath(root, directory_path)
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'rb') as f:
                        tmpdata = f.read()
                        fileStruct = {
                            'folder': currentFolder,
                            'name': os.path.splitext(file)[0],
                            'extension': os.path.splitext(file)[1],
                            'data': tmpdata
                        }
                        pickle.dump(fileStruct, archive)
                except Exception as e:
                    print(f"Ошибка при обработке файла {file_path}: {e}")
    compress_gzip('result.ble', 'result.blezip')

def compress_gzip(input_file, output_file):
    with open(input_file, 'rb') as f_in, gzip.open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)
