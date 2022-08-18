import time
def timer(seconds):
    while seconds > 0:
        mins = int(seconds/60)
        sec = int(seconds%60)
        counter = f'{mins}:{sec}'
        print(counter)
        seconds -= 1
print('Times Up')
seconds = input("How long would you like to set a timer for?") 
timer(int(seconds))
