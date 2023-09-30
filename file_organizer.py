import os
import shutil

wow = {
    "documents": (".pdf", ".xslx", ".docx", ".pptx", ".txt"),
    "video": (".mkv", ".mp4", ".webm", ".mov", ".avi", ".m4v", ".m4a", ".hevc"),
    "audio": (".mp3", ".wav", ".opus", ".aac"),
    "photos": (".jpeg", ".png", ".jpg", ".webp", ".heic", ".gif"),
    "code": (
        ".html",
        ".css",
        ".py",
        ".js",
        ".php",
        ".rb",
        ".xml",
        ".json",
        ".pyw",
        ".c",
        ".sh",
        ".bat",
        ".cs",
        ".java",
        ".htm",
    ),
    "archives": (".zip", ".7z", ".rar"),
    "programs": (".exe", ".msi", ".jar", ".apk", ".iso", ".msu"),
}

os.chdir("D:\\Edge Downloads")


def move_files(folder_name, file_extension):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass

    for i in os.listdir():
        if os.path.isdir(i):
            if i not in wow.keys():
                try:
                    os.mkdir("Folders")
                    shutil.move(i, "Folders")
                except FileExistsError as e:
                    print("Folder was already there, continuing...")

        elif i.endswith(file_extension):
            try:
                shutil.move(i, folder_name)
            except Exception as e:
                os.remove(i)


for i, j in wow.items():
    try:
        move_files(i, j)
    except Exception as e:
        print(e)
