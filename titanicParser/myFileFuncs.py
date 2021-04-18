def readFile(fileToRead):
    '''
    Returns the contents of a file in a list.
    Each element of the list is a line extracted from file inputted as an arg
    '''
    fileWordList = []
    
    if (isinstance(fileToRead, str)==False):
        raise Exception("Invalid file name. File name must be inputted as a string") 
        return 0
    
    try:
        
        f = open(fileToRead)
        for line in f:
            fileWordList.append(line)
        f.close()

        if len(fileWordList) < 1:
            print("File empty")
            return 0
        else:
            return fileWordList
    
    except FileNotFoundError:
        raise Exception('File does not exist')
        return 0

