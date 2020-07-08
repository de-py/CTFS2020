# Squeezy - 50 points
Ok this time, you aren't getting anywhere near anything.

# Solve
Because of the associative property of xor, we can xor the input and the output to get the flag. So we xor'd each character of the base64 decoded string as well as the the key "meow..." to get the flag. If we put the result back into the original function to check pass it will xor each character in "meow" with the flag which would result in the base64'd value and thus confirms the flag is correct.


# Flag 
rtcp{y0u_L3fT_y0uR_x0r_K3y_bEh1nD!}