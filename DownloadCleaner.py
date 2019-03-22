import shutil
import os
import time

#Getting into the Downloads folder.
os.chdir(os.path.expanduser("~") + os.sep + "Downloads")


#Creating lists for the file-types.
vids = ['.mp4','.mkv','.avi','.mpg','.mov','.wmv']
pics = ['.gif','.jpg','.png','.jpeg','.cr2']
sounds = ['.aac', '.mp3','.wma' ,'.wav']
compressed = ['.zip','.rar','.tar','.tar.gz','.tgz','.bz','.7z','.tgz','.tar.bz2']
books = ['.pdf','.epub']
Documents = [".doc", ".docx", ".txt", ".ppt", ".pptx", ".pdf", ".rtf"]
programs = ['.exe','.msi']
VirtualDisk = [".vmdk", ".ova", ".iso",".img"]
Extras = [".html", ".c", ".cpp", ".torrent",".ino","ttf",'.otf',".ipa","apk"]
Adobe = [".xd",".ai",".psd",".svg",".eps"]
fileTypes = [vids,pics,sounds,compressed,books,Documents,programs,VirtualDisk,Extras,Adobe]

#Lists for putting the correct files in.
vidsList = []
picsList = []
soundsList = []
compressedList = []
booksList = []
programsList = []
DocumentsList = []
VirtualDiskList = []
ExtrasList = []
AdobeList = []
lists = [vidsList,picsList,soundsList,compressedList,booksList,programsList,DocumentsList,VirtualDiskList,ExtrasList,AdobeList]



#Creating directories if necessary.
def Directories(Type):
	if os.path.isdir(Type):
		print("-Directory '%s' already exists." % Type)
	else:
		print("Creating directory '%s'..." % Type)
		os.mkdir(Type)




#Getting the files.
def getFiles(Type,List):
	for file in os.listdir(os.getcwd()):
		for item in Type:
			if file.endswith(item):
				List.append(file)



#Showing and moving the files.
def Move(List,folder):
	moved = 0
	for item in List:
		print("Moving %r to %r..." % (item,folder))
		shutil.move(item,folder)
		time.sleep(0.1)
		moved += 1
	if moved == 0:
		print("No items needed to be moved.")
		time.sleep(3)

def Final():
	folders = ['Video','Pictures','Music','Compressed','Books','Documents','Programs','VirtualDisk','Extras','Adobe']
	for i in range(len(folders)):
		Directories(folders[i])
		getFiles(fileTypes[i],lists[i])
		Move(lists[i],folders[i])

Final()