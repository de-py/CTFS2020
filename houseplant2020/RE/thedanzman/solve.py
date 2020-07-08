import base64
import codecs

def woah(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))

def solve():
    # Resembles base64 but not quite what we want due to the single ticks in the strings
    b = "'=ZkXipjPiLIXRpIYTpQHpjSQkxIIFbQCK1FR3DuJZxtPAtkR'o"
    key = "nyameowpurrpurrnyanyapurrpurrnyanya"
    
    # The value was reversed, we flip it back
    # b = b[::-1]
    print(b)

    # The value was also rot_13, we do rot_13 again to get it back. (Double rot_13).
    # A quick check shows that it is still in base64 and without going into it too 
    # I'm guessing this is the right track. b'ExgNCgkMWhQ3ES1XPDoSVVkxDFwcUDcGLVcEKVYvCwcvKxM='
    # b = codecs.encode(b, "rot_13")
    print(b)

    # Decode b64
    # b = base64.b64decode(b,altchars=None)
    print(b)
    
    

    # Key is only rot13, nothing fancy like the base64 value
    # key = codecs.encode(key,"rot_13")

    test = woah(key,b)
    print(test)
    # print(codecs.encode(test,"rot_13"))
    

if __name__ == "__main__":
    solve()
