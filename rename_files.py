import os

def renaming():

    #variables
    savedPath = os.getcwd()

    print("Current Directory " + savedPath) 
    # 1) get the file name and open it
    fileList = os.listdir("/Users/jamekaechols/Desktop/PythonShenanigans/HiringManagersOpenME")
    print(fileList)
    os.chdir("/Users/jamekaechols/Desktop/PythonShenanigans/HiringManagersOpenME")
    # 2) get the files and rename them
    for fileNames in fileList:
        remove = "0123456789"
        table = str.maketrans('','',remove)
        os.rename(fileNames,fileNames.translate(table))
        print(fileNames)
renaming()
