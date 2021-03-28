import math
def main():
    cSet = 100 # change to match number of characters in charset
    numPass = pow(2, 128) # number of passwords needed
    i = 0 #represents the power that our charset is taken to in order to surpass numPass
    while (pow(cSet, i) <= numPass):
        i += 1
        print(i)
    return i

if __name__ == "__main__":
    main()