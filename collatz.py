import matplotlib.pyplot as plt

def collatz_seq():
    x = int(input("Enter the number: "))
    print("The number you've entered is: ",x)


    y_points = [x]
    x_points = [1]
    i = 2
    while x != 1:
        x_points.append(i)
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3*x+1
        y_points.append(int(x))
        i += 1
    print("No of terms in this sequence is: ", len(y_points))
    print("The sequence is: \n",y_points)


    plt.plot(x_points, y_points)
    plt.show()

    print("Highest point of this curve is {} ".format(max(y_points)))
    
collatz_seq()
