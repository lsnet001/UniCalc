#!/usr/bin/env python3

from colorama import Fore as color 


GREEN = color.GREEN
RED = color.RED
YELLOW = color.YELLOW
WHITE = color.WHITE

try:
    while True:
        print(f"{RED}")
        print("""
        ██╗░░░ ██╗███╗░░ ██╗██╗░█████╗░   █████╗    ██╗░░░░░    █████╗░
        ██║░░░ ██║████╗░ ██║██║██╔═══██  ██╔═══██╗██║░░░░░██╔═══██╗
        ██║░░░ ██║██╔ ██╗ ██║██║██║░░╚═╝  ███████║██║░░░░░██║░░╚═╝
        ██║░░░ ██║██║ ╚ ████║██║██║░░ ██  ██╔═══██║██║░░░░░██║░░ ██╗
        ╚ ██████╔╝ ██║░ ╚ ███║██║╚ █████╔╝██║░░ ██║███████╗ ╚█████╔╝
        ░ ╚══════╝░ ╚═╝ ░░  ╚══╝  ╚═╝    ░╚═════╝░╚═╝  ░░╚═╝   ╚════════╝░  ╚═════╝░""")
        #g = open('Uni.txt','r')
        #print(''.join(g))
        print('''_________________________________________________________________________________''')
        print(f"""{GREEN}Welcome!                                    Compiled By Lsnet001""")
        print("Instagram https://www.instagram.com/lsnet001/")                                               
        print("Github https://github.com/lsnet001")
        print('''
            A)HEX 
            B)DEC 
            C)OCT 
            D)BINARY 
            E)Text To Code(Encode!)
            ''')
        print("Ctrl+c To Exit")


        AA = str (input("Choose the type your converting: ")) 
        if AA == 'A':
            print("Using HEX!")
            #Working
            try:
                def hex(hex_string):
                    result = ""
                    for i in range(0, len(hex_string), 2):
                        hex_pair = hex_string[i:i+2]
                        decimal_value = int(hex_pair, 16)
                        print(f"{RED}",decimal_value,f"{YELLOW}",end="")
                        char = chr(decimal_value)
                        result += char
                    return result

                print("Enter HEX to convert")
                hex_string = input("").replace(" ", "")
  
                result_string = hex(hex_string)
                print()
                print(result_string)
                print(f"{WHITE}^^^Results On Bottom^^^")
                break
            except ValueError:
                print("Error! Number might not be base 16")
                

        elif AA == "B":
            print("Using DEC!")
            #Working
            try:
                print("Enter DEC to convert")
                b = input().split()
                print(f"{YELLOW}")
                for idx, num in enumerate(b):
                    b = int(num)
                    x = chr(b)
                    print(x, end="")
                print()
                print(f"{WHITE}^^^Results On Bottom^^^")
                break
            except ValueError:
                print("Error! Number might not be base 10")
                

        elif AA == "C":
            print("Using OCT!")
            #Working
            try:
                print("Enter OCT to convert")
                for idx, num in enumerate(input().split()):
                    x = int(num, 8)
                    z = chr(x)
                    print(z, end="")
                print()
                print(f"{WHITE}^^^Results On Bottom^^^")
                break
            except ValueError:
                print("Error! Number might not be base 8")
                

        elif AA == "D":
            print("Using BINARY!       Requires full 8 digit binary string!")
            #Working
            try:
                def bin(bin_string):
                    result = ""
                    for i in range(0, len(bin_string), 8):
                        bin_pair = bin_string[i:i+8]
                        decimal_value = int(bin_pair, 2)
                        print(f"{RED}",decimal_value,f"{YELLOW}",end="")
                        char = chr(decimal_value)
                        result += char
                    return result
                print("Enter BINARY to convert")
                bin_string = input("").replace(" ", "")

                result_string = bin(bin_string)
                print()
                print(result_string)
                print(f"{WHITE}^^^Results On Bottom^^^")
                break
            except ValueError:
                print("Error! Number might not be base 2")
                

        elif AA == "E":
            print("Using Text To Code!")
            print('''
            A)HEX 
            B)DEC 
            C)OCT 
            D)BINARY
            ''')
        
            while True:
                BB = str (input("Choose the type your converting to: "))
                if BB == "A":
                    print("Using Text to HEX!")
                    print("Enter Text to convert")
                    #Working
                    try:
                        with open("inputtext.txt", "w") as f:
                            for idx, num in enumerate(input()):
                                x = (num).encode("utf-8").hex()
                                z = str(x)
                                f.write(z + " ")
                        with open("inputtext.txt") as g:
                            for i in g:
                                print(f"{YELLOW}", i)
                                print(f"{WHITE}^^^Results On Bottom^^^")
                                quit()
                    except ValueError:
                        print("Error! Number might not be base 16")
                        
    
                elif BB == "B":
                    print("Using Text to DEC!")
                    print("Enter Text to convert")
                    #Working
                    try:
                        with open("inputtext.txt", "w") as f:
                            for idx, num in enumerate(input()):
                                x = ord(num)
                                z = str(x)
                                f.write(z + " ")
                        with open("inputtext.txt") as g:
                            for i in g:
                                print(f"{YELLOW}", i)
                                print(f"{WHITE}^^^Results On Bottom^^^")
                                quit()
                    except ValueError:
                        print("Error! Number might not be base 10")
                        
                
                elif BB == "C":
                    print("Using Text to OCT!")
                    print("Enter Text to convert")
                    #Working
                    try:
                        with open("inputtext.txt", "w") as f:
                            for idx, num in enumerate(input()):
                                w = oct(ord(num))
                                x = w[2:]
                                z = str(x)
                                f.write(x + " ")
                        with open("inputtext.txt", "r") as g:
                            for idx2, num2 in enumerate(g):
                                print(f"{YELLOW}",num2)
                                print(f"{WHITE}^^^Results On Bottom^^^")
                                quit()
                    except ValueError:
                        print("Error! Number might not be base 8")
                        
                
                elif BB == "D":
                    print("Using Text to BINARY!")
                    print("Enter Text to convert")
                    #Working
                    try:
                        t = input()
                        res = "".join(format(ord(i), '8b') for i in t)
                        bin_string = res
                        print(f"{YELLOW}",bin_string)
                        print(f"{WHITE}^^^Results On Bottom^^^")
                        quit()
                    except ValueError:
                        print("Error! Number might not be base 2")

                else:
                    print("Option does not exist!")
                        
                
        else:
            print("Option does not exist!", f"{WHITE}")

except EOFError:
    print("Exiting!")
except KeyboardInterrupt:
    print("Exiting!")


    
        
    


    