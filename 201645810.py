import os, re
import hashlib
import json

# save id, pw
global data
data = {}

# making input to ascii code and return binary number
def makebit(input):
    result = ''
    for i in range(0, len(input)):
        asc = ord(input[i])
        result_bin = bin(asc)
        result_bin = result_bin.replace('0b', '0')
        if(len(result_bin)>7):
            result_bin = result_bin[1:]
        result += result_bin
    return result

# making binary to hash
def makehash(bit):

    # default parameter
    folding_1 = ''
    folding_2 = ''
    reverse_folding_2 = ''
    result = 0

        
    # making first 32bit of input to first folding parameter
    for i in range(0, 32):
        folding_1 += bit[i]

        
    # making left bit to last folding parameter
    for i in range(32, len(bit)):
        folding_2 += bit[i]
    
        
    # if last folding parameter is upper than 64 bit, delete it
    if(len(folding_2)>32):
        folding_2 = folding_2[0:32]

        
    # making last folding parameter to 32bit and reverse it
    if(len(folding_2)<32):
        for i in range(len(folding_2), 32):
            folding_2 += '0'


    reverse_folding_2 = folding_2[::-1]

        
    # plus two parameter and making result of final hash parameter
    result = int(folding_1, 2) + int(reverse_folding_2, 2)

    return result

# menu
def view():
    try:
        print("MENU")
        print("1. making email")
        print("2) login")
        print("3) log out and end", end="\n\n")
        print("select : ", end="")
        inputs = int(input())

        if inputs < 1 or inputs > 3:
            print("wrong input")
        return inputs

    except Exception:
        print("wrong input\n")
        return 0

# making ID
def idcreate():
    try:
        print("\nid : ", end="")
        input_id = input()

        print("\npw : ", end="")
        input_pw = input()

        if checkid(input_id):
            if checkpw(input_pw):
                data[input_id] = makehash(makebit(input_pw))
                print("\nsuccess!\n")
            else:
                print("\nERROR Read and Try again")
                print("pw constraint 1. upper than 10")
                print("pw constraint 2. include lower case in English")
                print("pw constraint 3. include upper case in English")
                print("pw constraint 4. include lexigram")
        else:
            print("ERROR")
            print("Try another ID.\n")

    except Exception:
        pass

# login id
def IDlogin():
    try:
        print("\nid : ", end="")
        input_id = input()

        print("\npassword : ", end="")
        input_pw = input()

        if not checkid(input_id):
            tmp = makehash(makebit(input_pw))
            if tmp == data[input_id]:
                print("\nsuccess!\n")
            else:
                print("\nwrong password\n")
        else:
            print("\nwe don't have a this id\n")

    except Exception:
        pass
# load id
def IDloadDB():
    try:
        if os.path.exists("data.json"):
            with open("data.json", "r") as json_file:
                json_data = json.load(json_file)
                global data
                data = json_data['data']
        else:
            with open("data.json", "w") as json_file:
                json.dump({'data':{}},json_file)
    except Exception:
        pass

# save id
def IDsaveDB():
    try:
        with open("data.json", "w") as json_file:
            json.dump({'data':data},json_file)
        print("\nlogout and end\n")
    except Exception:
        pass


# check pw
def checkpw(pwd):
    reg = re.compile(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z0-9!@#$%^&*()]{10,16}$")
    mat = re.match(reg, pwd)
    if mat:
        return True
    else:
        return False
    
# check overlap
def checkid(id):
    return not (id in data.keys())


def main():
    IDloadDB()
    while(True):
        menu = view()
        if menu == 1:
            idcreate()
        elif menu == 2:
            IDlogin()
        elif menu == 3:
            IDsaveDB()
            break
        else:
            pass


if __name__ == "__main__":
    main()
