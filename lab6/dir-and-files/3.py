import os
def test_path(path):
    if os.path.exists(path):
        filename=os.path.basename(path)
        directory=os.path.dirname(path)
        return True, filename, directory
    else:
        return False, None, None
    
def main():
    path="/Users/Aliyar/Desktop/lab6/dir-and-files/3.py"
    exists, filename, directory=test_path(path)
    if exists:
        print("Path exists.")
        print("Filename:",filename)
        print("Directory:",directory)
    else:
        print("Path does not exist.")

if __name__=="__main__":
    main()