import Packer 
import Unpacker

print("1 - Start packing.\n 2 - Start unpacking.")
menu_value = input("Enter menu value: ")

if(menu_value == "1"):
    Packer.Start()
elif(menu_value == "2"):
    Unpacker.Start()
else:
    print("Wrong menu value.")