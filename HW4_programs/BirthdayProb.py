import math
def main():    
    # days = pow(2, 16)
    days = 356
    not_sharing = 1
    for i in range(1, days):
        print ("{0} - {1:.16f}".format(i+1, (1-(1-(i/days)))))
        if (i == 1000):
            break
 
if __name__== "__main__":
    main()