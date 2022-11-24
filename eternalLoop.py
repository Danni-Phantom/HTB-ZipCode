
#!/usr/bin/env python3

from zipfile import ZipFile
import os

dirPath = "/Users/x/Desktop/EternalLoop/"
file_name_original = "EternalLoop.zip"
file_name_original_path = dirPath + file_name_original
file_name_next = ""
first_pass = "hackthebox"
next_passsword = ""

with ZipFile(file_name_original, 'r') as zip:
    file_name_next = zip.namelist()[0]
    zip.extract((file_name_next), path=dirPath, pwd=first_pass.encode())
    temp = os.path.splitext(dirPath+file_name_next)
    next_passsword = (os.path.basename(temp[0]))
    print("file_name_original:  " + file_name_original)
    print ("file_name_next: " + file_name_next)
    print ("next_passsword: " + next_passsword)
    zip.close()
while ((os.path.basename(temp[1])) == ".zip"):
    file_name_original = file_name_next
    print("next file_name_original:  " + file_name_original)
    with ZipFile(file_name_original, 'r') as zip:
        file_name_next = zip.namelist()[0]
        temp = os.path.splitext(dirPath+file_name_next)
        next_passsword = (os.path.basename(temp[0]))
        first_pass = next_passsword
        print ("next first_passsword: " + next_passsword)
        zip.extract((file_name_next), path=dirPath, pwd=first_pass.encode())
        print("file_name_original:  " + file_name_original)
        print ("file_name_next: " + file_name_next)
        print ("next_passsword: " + next_passsword)
        zip.close()
