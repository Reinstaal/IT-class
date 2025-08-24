import random
from time import perf_counter

def tippCheck(tipp_to_check, lastDrawn): 
    return (tipp_to_check == lastDrawn)

def main():
    runs = 0
    print("Gambling..")
    # Use instead if maximum amount of loops preferred
    # for i in range(1000000000):
    while True:
        runs += 1
        drewNumbers = []
        # while len(drewNumbers) by absolutezero #IStoleCode #Thanks
        # hard coded variants: 3 or 6
        # while len(drewNumbers) < 3:
        while len(drewNumbers) < 6:
            drawingNumber = random.randrange(1, 50)
            if drawingNumber not in drewNumbers:
                drewNumbers.append(drawingNumber)
        if tippCheck(tippToCheck, drewNumbers):
            print(f"Runs needed to win: {runs}")
            timerStop = perf_counter()
            print("Used time:", "{:.2f}".format(timerStop-timerStart), "seconds")
            break


tippToCheck = []
drewNumbers = []
#hard coded gamble try
#3 or 6 variant
tippToCheck += [1,2,3,
                # ]
                   4,5,6]
timerStart = perf_counter()

main()