import time
def countdownTime(seconds):
    while seconds>0:
     minutes=seconds//60
     sec=seconds%60
     timer=f'{minutes}:{sec}'
     time.sleep(1)
     print(timer)
     seconds=seconds-1
    print("Time is up")
seconds=int(input("Enter a number"))
countdownTime(seconds)