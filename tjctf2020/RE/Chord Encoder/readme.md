# Chord Encoder - 40 points
I tried creating my own chords, but my encoded sheet music is a little hard to read. Please play me my song!


# Solve
Well I'm not crazy about how I solved this but it got the flag. The organizers did drop a hint to possibly use a pathfinder algorithm. That seems like the right approach but I was also close to solving so I Just completed it manually which did not take too long either. 

So I thought I could write a script to decode it based on the the conversion performed, only in reverse. So true_solve.py was that attempt and it did partially help with a few things. It used a type of sliding window to check against the chords provided to us.

It successfully decoded the first letters where I could make out the letters fXagX or something to that effect. So with this, I could determine that it should say flag{ and map the missing hex values. As you will see, the "solver.py" only contains A-F and not a-f. So the X's in fXagX represented the missing key for letters a-f.

```l = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G'}```

With the text partially decoded, we could complete the rest of the key because these mapped to the hex values needed to complete the first part flag{.

```l = {'A':'1','B':'2','C':'3','D':'4','E':'5','F':'6','G':'7','c':'c','b':'b','a':'a','d':'d'}```

The problem after this is that certain values could be two different chords if using the sliding window method. For example 020 and 0200 or 010 and 0100. So this is where the pathfinder algorithm or some type of recursion might come in handy to try both paths and continue on. 

The last step to complete this manually was that I knew it would probably end in a bracket '}'. So I went to the end of the encoded notes to make sure this was the case after converting to hex and then ascii. 

After this, I slowly built the flag manually, confirming the write letters as I went along. 

# Flag
```666c61677b7a6174735f776f745f315f63616c6c5f615f6d656c6f447d```

```flag{zats_wot_1_call_a_meloD}```

# Key
To simplify some parts of this, you could replace chords A-F with the following to make you new key for decoding. a-f already mapped properly. Now you can just figure out the pathfinding method and/or do something recursively or concurrently.

```
1 0112
2 2110
3 1012
4 020
5 0200
6 1121
7 001
a 0122
b 2100
c 1002
d 010
e 0100
f 1011
g 000
```

