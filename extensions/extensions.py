#prompt the user for file name

file_name = input("File name: " ).strip().capitalize()

#To check if file has .extension or not
if file_name.find(".") == -1:
    extension = file_name
else:
    extension = file_name.rpartition(".")[2] #partition splits the string at the last separator and returns a tuple of 3

#print file extension type
match extension:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")


