import os
import pickle


def Start():
    directory_path = input("Enter directory path: ")

    with open(os.path.join('result.ble'), 'wb') as archive:
        fileCounter = 0
        for root, dirs, files in os.walk(directory_path):
            currentFolder = os.path.relpath(root, directory_path)
            for file in files:
                with open(os.path.join(root, file), 'rb') as f:
                    tmpdata = f.read()
                    fileStruct = {
                        'folder': currentFolder,
                        'name': os.path.splitext(file)[0],
                        'extension': os.path.splitext(file)[1],
                        'data': tmpdata
                    }
                    pickle.dump(fileStruct, archive)
            
