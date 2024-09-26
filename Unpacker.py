import os
import pickle
import tempfile
import gzip

def Start():
    archive_path = input("Введите путь к архиву: ")
    output_directory = input("Введите директорию для распаковки файлов: ")
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    # Декомпрессия RLE-архива во временный файл
    with tempfile.NamedTemporaryFile(delete=False) as temp_decompressed_file:
        decompress_gzip(archive_path, temp_decompressed_file.name)
        temp_decompressed_file_path = temp_decompressed_file.name

    with open(temp_decompressed_file_path, "rb") as f:
        while True:
            try:
                data = pickle.load(f)
                folder_path = os.path.join(output_directory, data["folder"])
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                file_path = os.path.join(folder_path, data["name"] + data["extension"])
                with open(file_path, 'wb') as tmpf:
                    tmpf.write(data["data"])
            except EOFError:
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
                break
    # Удаление временного файла
    os.remove(temp_decompressed_file_path)

def decompress_gzip(input_file, output_file):
    with gzip.open(input_file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        f_out.writelines(f_in)
