#!/usr/bin/env python3

version = "Alpha Build 118"                                             ##
print("\nCaravan Calculator - by The Caravan -- " + version)            ##
                                                                        ##
from datetime import *                                                  ##
from math import *                                                      ##
import random                                                           ##
                                                                        ##
supportedOps = {"FLOAT + FLOAT", "FLOAT - FLOAT",                       ## - This is so that if the user types "help", this data structure 
                "FLOAT * FLOAT", "FLOAT / FLOAT"}                       ##      is outputted
                                                                        ##
into = ""                                                               ##
prevInput = ""                                                          ##
outo = 0                                                                ##
ans = ""                                                                ##
toScreen = ""                                                           ##
inputString = ""                                                        ##
logLoc = ("/home/sb5060tx/Logs/caravanCalculator-py/"                   ##
          + str(datetime.now()) + ".txt")                               ##
                                                                        ##                                        
                                                                        ##
##########################################################################
'''    Plans: 

             >>> loop 9; 8 + 9
             >>> 

             Tkinter, Unix, Windows, iOS, Android

'''                                    
##########################################################################
                                                                        ## - This loop is so that the user can keep running the
while True:                                                             ##      calculator on more than one value. Until a ^C or anything like.
    try:                                                                ##
        file = open(logLoc, "w")                                        ##
        inputString = input("\nCARAVAN-CALCULATOR >>> ")                ## - User inputs here
                                                                        ##
        if inputString == "":                                           ##
            inputString = prevInput                                     ##
                                                                        ##
        elif "help" == into or "?" == into:                             ## --------------------------------
            print("\nList of supported operations. Note that FLOAT"     ##  Equivalent to typing --help in Bash
                    + " and INT are placeholders for the accepted "     ##      Basically output here all the supported operations in this build
                    + "value:\n")                                       ##                                    (refer to the data structure)              
            for op in supportedOps:                                     ##      Once done, complete the loop
                print("- " + op)                                        ##
            continue                                                    ##
                                                                        ##
        elif inputString in ["q", "Q", "exit", "Exit", "EXIT"]:         ##
            print("Goodbye!")                                           ##
            break                                                       ##
                                                                        ##
        prevInput = inputString                                         ##
        into = inputString                                              ##
                                                                        ##
        if "ans" in into and "=" not in into and into != "ans":         ##
            into = into.replace("ans", str(ans))                        ##
                                                                        ##
            if isinstance(outo, int):                                   ##
                print("\nans <-- " + format(ans, ","))                  ##
            else:                                                       ##
                print("\nans <-- " + str(ans))                          ##
                                                                        ##
        file.write("A new loop:")                                       ##
        file.write("prevInput = " + str(prevInput))                     ##
        file.write("intoInit = " + str(into))                           ##
                                                                        ##
        if "=" in into:                                                 ##
            raise NameError                                             ##
                                                                        ##    
        else:                                                           ##
            outo = (eval(into))                                         ##
            ans = outo                                                  ##
                                                                        ##
            if inputString.isnumeric():                                 ##
                toScreen = "\n" + format(outo, ",")                     ##
            elif isinstance(outo, int):                                 ##
                toScreen = ("\n" + str(inputString) + " = " +           ##
                            format(outo, ","))                          ##
            else:                                                       ##
                toScreen = ("\n" + str(inputString) + " = " +           ##
                            str(outo))                                  ##
                                                                        ##
        file.write("intoNew = " + str(into))                            ##
        file.write("outo = " + str(outo))                               ##
        file.write("toScreen = " + str(toScreen))                       ##
        file.close()                                                    ##
                                                                        ##
        print(toScreen)                                                 ##
                                                                        ##
    except NameError as e:                                              ##
        try:                                                            ##
            exec(inputString)                                           ##
            toScreen = "\n" + inputString                               ##
                                                                        ##
        except Exception as e:                                          ##
            print(e)                                                    ##
            pass                                                        ##
                                                                        ##
    except Exception as e:                                              ##
        try:                                                            ##
            print(e)                                                    ##
            file.write("Exception-L1 = " + str(e))                      ##
            pass                                                        ##
                                                                        ##
        except Exception as f:                                          ##
            print(f)                                                    ##
            pass                                                        ##
                                                                        ##
##########################################################################

        
    '''                                                        ## 
                                                                    ## ---------------------------------
    if into == "" and prevInput != "":                              ##  In the case the user presses enter after entering nothing for the second time,
        into = prevInput                                            ##      this repeats the previous operation.
                                                                    ##      Good if the user uses "ans", for ans keeps changing on press of enter
                                                                    ## ---------------------------------            
                                                                    ##  Otherwise, split the input to a list -- Divide and Conquer
    else:
        into = into.split(" ")

        ## To prevent digits from being seperate (2 3 4 --> 234) without an operation
        for char in into:
            ind = into.index(char)
            try: 
                if isinstance(int(into[ind]), int) and isinstance(int(into[ind + 1]), int):
                    into.insert(str(into[ind]) + str(into[ind + 1], ind))
                    into[ind + 1] = ""          ## Zeros this rather than deleting so as not to mess up the for loop
                    into[ind + 2] = ""
                    
                    
            except ValueError:
                pass
            except IndexError:
                break
            
    outo = ""

    index = -1
    for char in into:
            index += 1
            outo += str(char) + " "

            if char == "ans":
                ans = ans
                print("TEST: " + str(ans))
                continue
            
            try:
                if int(char) == int(char):
                    ans = int(into[index])
                    continue

            except ValueError:
                pass

            except IndexError:
                break

            if char == "+" or char == "plus":
                ans += float(into[index + 1])
                index += 1

            elif char == "-" or char == "minus":
                ans -= float(into[index + 1])
                index += 1

            elif char == "*" or char == "times":
                ans *= float(into[index + 1])
                index += 1

            elif char == "/" or char == "over":
                ans /= float(into[index + 1])
                index += 1

            elif char == "%" or char == "mod":
                ans %= float(into[index + 1])
                index += 1

            elif char == "&&" or char == "and":
                ans = ans and int(into[index + 1])
                index += 1

            elif char == "||" or char == "or":
                ans = ans or int(into[index + 1])
                index += 1

            elif char == "<" or char == "lessthan":
                ans = ans < float(into[index + 1])
                index += 1
                
            elif char == ">" or char == "greaterthan":
                ans = ans > float(into[index + 1])
                index += 1
                
            elif char == "<=" or char == "lessthanorequalto":
                ans = ans <= float(into[index + 1])
                index += 1
                
            elif char == ">=" or char == "greaterthanorequalto":
                ans = ans >= float(into[index + 1])
                index += 1

            elif char == "==" or char == "equalto":
                ans = ans == float(into[index + 1])
                index += 1

            elif char == "!=" or char == "notequalto":
                ans = ans != float(into[index + 1])
                index += 1

            elif char == "sqrt" or char == "root":
                ans = math.sqrt(float(into[index + 1]))
                index += 1

            elif char == "sin":
                ans = math.sin(math.radians(float(into[index + 1])))
                index += 1

            elif char == "cos":
                ans = math.cos(math.radians(float(into[index + 1])))
                index += 1

            elif char == "tan":
                if float(into[index + 1]) == 90: raise Exception("0x22")
                ans = math.tan(math.radians(float(into[index + 1])))
                index += 1

            elif char == "log":
                ans = math.log10(float(into[index+1]))
                index += 1

            elif char == "log2":
                ans = math.log2(float(into[index+1]))
                index += 1

            elif char == "**" or char == "exponential" or char == "tothe":
                ans = ans ** int(into[index+1])
                index += 1

            elif char == "rad":
                ans = math.radians(float(into[index + 1]))
                index += 1

            elif char == "deg":
                ans = math.degrees(float(into[index + 1]))
                index += 1
            
            elif char == "^" or char == "xor":
                if ans == int(into[index + 1]):
                    ans = 0
                else:
                    ans = 1
                index += 1
                
            elif char == "not":
                ans = not ans
                index += 1

            elif char == "!" or char == "factorial":
                ans = math.factorial(int(into[index - 1]))
                index += 1
                
            elif char == "":
                continue

            else:
                raise Exception("0x35")
            
              
    except Exception as e:
    print("\nError " + str(e) + ": ", end="")

    if str(e) == "0x11": print("A space is required for operation")
    if str(e) == "0x22": print("The tangent of 90 degrees is undefined")
    if str(e) == "0x35": print("Unknown Character " + str(char))
     
    continue 

    ## Convert Answer to known fractions or values of possible

    if ans == 0.7071067811865475:
        ans = "square root of 2 over 2"

    elif ans == 0.8660254037844386:
        ans = "square root of 3 over 2"

    elif ans == 3.1415926535897932384:
        ans = "pi"

    elif ans == 0.3333333333333333333:
        ans = "1 / 3"

    elif ans == 0.6666666666666666666:
        ans = "2 / 3"

    elif ans == 0.1111111111111111111:
        ans = "1 / 9"

    elif ans == int(ans):
        ans = int(ans)
    '''
            
            
        
