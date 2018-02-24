def write_file():
    file_write = open("exception.txt", "w+")   #Write using exception
    try:
        file_write.write("This Exception Handling File!!!")
    except IOError:
        print("Error: can't find file")
        file_write.close()
def read_file():                           #Read file using exception

    try:
        file_read = open("excpion.txt", "r")   #File name is wrong in order to check exception 
        print(file_read.read())
    except IOError:
        print("Error: can't find folder on pesent directory")


def read_final_exception() :                                         #Read File
    file_read = open("exception.txt", "r")  
    try:
        print(file_read.readline())
    finally:
        print("---DONE---")
        file_read.close()


write_file()
read_file()
read_final_exception()
