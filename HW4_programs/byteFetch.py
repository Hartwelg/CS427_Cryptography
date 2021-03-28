import random

def main():
    guesses = [] #stores the strings already generated
    iterations = 0 #number of guesses so far
    num = 0 #initialize byte value
    while (True):
        num = random.getrandbits(16) #random 16 bits
        if (num not in guesses): #check if num has already been generated
            guesses.append(num) #if not, append to guesses
            iterations += 1 #increment number of guesses
        else:
            break #break when collision occurs
    print (iterations)
    return

if __name__ == "__main__":
    main()