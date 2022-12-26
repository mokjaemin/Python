

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


pwdata = []
iddata = []

# do
while(1):

    print("1. making email")
    print("2. log in")
    print("3. log out and end the system")
    a = input("select : ")
    if(a=="1"):
        while(1):
            b = input("id : ")
            if b in iddata:
                print("try another one")
            else:
                break
        while(1):
            f = 0
            g = 0
            print("pw constraint 1. upper than 10")
            print("pw constraint 2. include lower case in English")
            print("pw constraint 3. include upper case in English")
            print("pw constraint 4. include lexigram")
            c = input("password : ")

            for d in c:
                if(d.isupper() == True):
                    f = 1

            for e in c:
                if(e.islower() == True):
                    g = 1

            if(len(c) < 10):
                print("violate constraint 1")

            elif(g == 0):
                print("violate constraint 2")

            elif(f == 0):
                print("violate constraint 3")

            elif(c.isalnum() == True):
                print("violate constraint 4")

            else:
                print("success")
                iddata.append(b)
                break
        

        # make binary number
        bit = makebit(c)
        result = makehash(bit)
        pwdata.append(str(result))



    elif(a=="2"):

        id = input("id : ")
        pw = input("pw : ")

        i = 0
        j = 0

        l = 0
        k = 0
        
        for confirm1 in iddata:
            if(id == confirm1):
                j = 1
                break
            i += 1

        for confirm2 in pwdata:
            if(str(result) == confirm2):
                k = 1
                break
            l += 1

        print(j)
        print(k)
        print(i)
        print(l)

        if(j == 1):
            if(k == 1):
                if(i == l):
                    print("login success")
        else:
            print("login failure")


    elif(a=="3"):
        break

    else:
        print("wrong input")



    
    


