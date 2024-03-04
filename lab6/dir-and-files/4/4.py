def file_length(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i+1
print("Number of lines in the file:", {file_length("/Users/Aliyar/Desktop/lab6/dir-and-files/4.txt")})