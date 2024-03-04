import os
def list_directories(path):
    dir=[d for d in os.listdir(path) if os.path.isdir(os.path.join(path,d))]
    return dir
def list_files(path):
    files=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f))]
    return files
def list_all(path):
    all=os.listdir(path)
    return all
def main():
    path="/Users/Aliyar/Desktop/lab6/dir-and-files/"
    print(f"Directories: {list_directories(path)}")
    print(f"Files: {list_files(path)}")
    print(f"All directories and files: {list_all(path)}")

if __name__=="__main__":
    main()