import base64

def woah(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def solve():
    b = "HxEMBxUAURg6I0QILT4UVRolMQFRHzokRBcmAygNXhkqWBw="
    xor1 = base64.b64decode(b, altchars=None).decode('utf-8')
    xor2 = "meownyameownyameownyameownyameownya"
    result = woah(xor1,xor2)
    print(result)

if __name__ == "__main__":
    solve()
