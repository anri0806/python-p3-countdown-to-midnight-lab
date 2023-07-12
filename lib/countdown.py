# your code goes here!
from time import sleep

def countdown(n):
    
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1

    print("HAPPY NEW YEAR!")
    
    
def countdown_with_sleep(n):
    
    while n > 0:
        print(f"{n} SECOND(S)!")
        n -= 1
        
        sleep(1)
        
    print("HAPPY NEW YEAR!")
