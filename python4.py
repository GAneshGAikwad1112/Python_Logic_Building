# Creating an automatic folder cleaner in python..........

import os

def crateIfNotExist(folder):
   if not os.path.exists(folder):
    os.makedirs(folder) 

def move(folderName, files):
  for file in files:
    os.replace(file,f"{folderName}/{file}")

if __name__=="__main__":

    files = os.listdir()
    files.remove("main.py")


    crateIfNotExist('Images')
    crateIfNotExist('Docs')
    crateIfNotExist('Media')
    crateIfNotExist('Others')

    imgExts = [".jpg",".png","jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    print(images)

    docExts = [".pdf",".docx",".txt","doc"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    print(docs)

    mediaExts = [".mp4",".mp3","flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    print(medias)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and  (ext not in docExts) and (ext not in imgExts) and os.path.isfile(files) :
            others.append(file)


    print(others)

    move("media",medias)
    move("image",images)
    move("doc",docs)
    move("Other",others)