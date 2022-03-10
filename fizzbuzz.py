#!/usr/bin/env python3



def main():
    
    x=1
    
    while x <= 100000:
        
        if(x%3 == 0 and x%5 == 0):
            print(x, " FizzBuzz")
        
        elif(x%3 == 0):
            print(x, " fizz")
        
        elif(x%5 == 0):
            print(x, " buzz")
        
        else:
            print(x)

        x += 1


main()
