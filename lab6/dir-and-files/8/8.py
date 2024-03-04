import os
def check_for_access(path):
    access_info={
        'existence':os.path.exists(path),
        'readability':os.access(path, os.R_OK),
        'writability':os.access(path,os.W_OK),
        'executability':os.access(path, os.X_OK)
    }
    return access_info
def delete_file(path):
    try:
        os.remove(path)
        print("File deleted.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Peermission denied.")
def main():
    path="/Users/Aliyar/Desktop/lab6/dir-and-files/8.py"
    access_info=check_for_access(path)
    if access_info['existence'] and access_info['writability']:
        delete_file(path)
    else:
        print("File cannot be deleted")

if __name__=="__main__":
    main()
