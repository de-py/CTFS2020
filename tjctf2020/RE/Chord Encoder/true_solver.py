import bytes
f = open("encoded2.txt").read()

first = 0
two = 1

chords = {}
for i in open('chords.txt').readlines():
	c, n = i.strip().split()
    # Old way, swap keys
    # chords[c] = n
	chords[n] = c

# Swap keys
# l = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G'}
l = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','c':'c','b':'b','a':'a','d':'d'}

s = ''

while (two < len(f)):
    sample = f[first:two]
    if sample in chords:
        c = chords[sample]
        first = two
        two = first+1
        if c in l:
            s += l[c]
        else:
            print(c)
            s += 'x'
        
    else:
        two += 1
print(s)



    # print(sample)
    # print(f[first:two])
    


