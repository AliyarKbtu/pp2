def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())
def main():
    path1="/Users/Aliyar/Desktop/lab6/dir-and-files/math.py"
    path2="/Users/Aliyar/Desktop/lab6/dir-and-files/7 2.txt"
    copy_file(path1,path2)
    print("Contents of the source file have been copied to the destination file")

if __name__=="__main__":
    main()