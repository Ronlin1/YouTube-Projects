import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(f"-----{timer}-----", end="\r")
        
        time.sleep(1)
        t -= 1
    print("LIFT OFF", end="\r")
        
time_ = input("Please enter time in minutes: ")  
# print(end=2*"\n")     
countdown(int(time_))
        