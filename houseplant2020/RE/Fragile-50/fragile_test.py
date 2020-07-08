

# Converted from Java
def check(s):
    h = False
    flag = 'h1_th3r3_1ts_m3'
    theflag = ""
    if len(s) != len(flag):
        return False
    for i in range(len(flag)):
        theflag += chr(ord(flag[i])+ord(s[i]))

    if theflag == "ÐdØÓ§åÍaèÒÁ¡":
        return True
    else:
        return False
        

# Does the reverse of the check function
def create_flag(s):
    flag = "h1_th3r3_1ts_m3"
    theflag = ""
    if len(s) != len(flag):
        print('hi')
        return 'Length mismatch'

    for i in range(len(flag)):
        theflag += chr(ord(s[i])-ord(flag[i]))
    

    
    if check(theflag):
        return theflag
    
    else:
        return 'Flag Not Found'



def main():
    equals = "ÐdØÓ§åÍaèÒÁ¡"
    result = create_flag(equals)
    print(result)


if __name__ == "__main__":
    main()