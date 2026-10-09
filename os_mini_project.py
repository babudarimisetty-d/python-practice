import os 
print("======== FILE MANAGER=======")
print("1.create folder")
print("2.show files and folder" )
print("3.create file")
print("4.rename file")
print("5.delete file")
print("6.exit")
while True:
    choice=input("Enter a choice:")
    if choice=="1":
        folder_name=input("Enter Folder name:")
        os.mkdir(folder_name)
    elif choice=="2":
        for item in os.listdir():
            print(item)
    elif choice =="3":
        file_name=input("Enter file name:")
        open(file_name,"w").close()
    elif choice=="4":
        file_name=input("Enter file name:")
        new_name=input("Enter new_name:")
        os.rename(file_name,new_name)
    elif choice=="5":
        file_name=input("Enter file name:")
        os.remove(file_name)
    elif choice=="6":
        print("exiting File Manager...")
        break  
    else:
        print("invalid choice")


