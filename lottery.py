import random
from time import perf_counter

# function draw() by absolutezero #IStoleCode #Thanks
def draw():
    drawnNumbers = []
    while len(drawnNumbers) < 3:
    # while len(drawnNumbers) < 6:
        drawingNumber = random.randrange(1, 50)
        if drawingNumber not in drawnNumbers:
            drawnNumbers.append(drawingNumber)
    return drawnNumbers

def tippCheck(tipp_to_check, lastDrawn): 
    return (tipp_to_check == lastDrawn)

def main():
    print("Gambling..")
    # Use instead if maximum amount of loops preferred
    # for i in range(10000000):
    while True:
        drewNumbers.append(draw())
        if tippCheck(tippToCheck, drewNumbers[-1]):
            # use this print only with for loop
            # print(f"Runs: {i}")
            timerStop = perf_counter()
            print("Used time:", "{:.2f}".format(timerStop-timerStart), "seconds")
            break


tippToCheck = []
drewNumbers = []
#hard coded gamble try
#3 or 6 variant
tippToCheck += [1,2,3,
                ]
                #    4,5,6]
timerStart = perf_counter()

main()