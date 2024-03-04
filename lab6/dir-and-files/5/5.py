def write_list_to_file(file_path,list):
    with open(file_path,'w') as file:
        for item in list:
            file.write(str(item)+'\n')
def main():
    list=[1,2,3,4,5]
    file_path="/Users/Aliyar/Desktop/lab6/dir-and-files/5.txt"
    write_list_to_file(file_path, list)
    print("List has been written to the file")

if __name__=="__main__":
    main()