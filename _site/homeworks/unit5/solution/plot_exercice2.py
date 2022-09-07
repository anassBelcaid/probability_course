import numpy as np
import matplotlib.pyplot as plt

def prob(n):


    value = 1
    for v in range(365 - n + 1, 366):
            value *= v
    return value / (365**n)

def main():
    
    A = np.zeros((81,1))
    for i in range(81):
        A[i] = prob(i)

    plt.plot(A,'go')
    plt.grid()
    # plt.show()
    plt.savefig('birthday.png')

if __name__ == "__main__":
    main()
    print(prob(40))
