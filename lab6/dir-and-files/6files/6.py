import string, os
def generate_text_files(path):
    if not os.path.exists(path):
        os.makedirs(path)

    os.chdir(path)

    for letter in string.ascii_uppercase:
        filename=f"{letter}.txt"
        with open(filename, 'w') as file:
            pass

def main():
    path="/Users/Aliyar/Desktop/lab6/dir-and-files/6files"
    generate_text_files(path)
    print("Files named A.txt to Z.txt  have been generated.")

if __name__=="__main__":
    main()