def file_list_loader(filename):
    fileList = []
    try:
        f = open(filename, "rt", encoding = "UTF-8")
        for line in f:
            file = line.strip('\n')
            fileList.append(file)
    except FileNotFoundError:
        print("File not found.")
    except EOFError:
        f.close()
    return fileList