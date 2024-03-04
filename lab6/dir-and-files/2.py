import os
def check_access(path):
    access_info={
        'existence':os.path.exists(path),
        'readability':os.access(path, os.R_OK),
        'writability':os.access(path,os.W_OK),
        'executability':os.access(path, os.X_OK)
    }
    return access_info
def main():
    path="/Users/Aliyar/Desktop/lab6/dir-and-files/"
    access_info=check_access(path)
    print(f"Existence: {access_info['existence']}"),
    print(f"Readability: {access_info['readability']}"),
    print(f"Writability: {access_info['writability']}"),
    print(f"Executability: {access_info['executability']}")

if __name__== "__main__":
    main()