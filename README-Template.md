
# Download Directory Organizer

  

Organizes files in downloads directory by classifying them into different folders according to their file types.

This project is inspired by http://dropit.sourceforge.net/.

Written in Python 3

My Download folder was cluttered and it need to be organized instead of doing it manually I wrote a basic python script to do it for me.
  

## Getting Started

  

Just download the project as zip and run python command

```

python DownloadCleaner.py

```
### To add more folders and filetypes
* Simply create a list under List for File Types and define your file types.
 ```eg - Adobe = [".xd",".ai",".psd",".svg",".eps"]```
* Add Name of the list in 'lists'.
``` 
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
```
* And finally add the name of the folder you want the file types to go in to the folders list.
``` folders = ['Video','Pictures','Music','Compressed','Books','Documents','Programs','VirtualDisk','Extras','Adobe']```

### Prerequisites

  

Make sure you have python 3 installed.

  

## Authors

  

*  **Sparsh Bajaj** - *Initial work* - [iTunes Artwork Downloader](https://reviewitnerd.com/artwork)

