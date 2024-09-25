import os
import pickle


def Start():
    archive_path = input("Enter path to archive: ")

    with open(archive_path, "rb") as f:
        trigger = True
        while trigger:
            try:
                data = pickle.load(f)
                if not os.path.exists("Unpacked"):
                    os.makedirs("Unpacked")
                if(not os.path.exists("Unpacked\\" + data["folder"])):
                    os.makedirs("Unpacked\\" + data["folder"])
                with open("Unpacked\\" + data["folder"] + "\\" + data["name"] + data["extension"],'wb') as tmpf:
                    tmpf.write(data["data"])
            except EOFError:
                trigger = False