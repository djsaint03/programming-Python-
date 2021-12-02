"""
COMP.CS.100 Programming 1
Project
This project was written by Johnson Apanishile and VU TU PHUONG NGUYEN
"""
import math

def mean(data_list):
    """
    this function collects a data list
    and calculates and returns the mean
    :param data_list: float, list number user inputs
    return: float, the mean value
    """
    n= len(data_list)
    mean = sum(data_list)/n
    return mean

def variance(data_list):
    """
    this function collects a data list
    and calculates and returns the variance
    :param data_list: float, from the data list user inputs
    return: float, the value of variance
    """
    n= len(data_list)
    mean = sum(data_list) / n
    dev = [(x - mean) ** 2 for x in data_list]
    variance = sum(dev) / (n-1)
    return variance

def std(data_list):
    """
    this function collects a data list
    and calculates and returns the standard deviation
    using import sqrt
    :param data_list: float, from the data list user inputs
    return: float, the value of standard deviation
    """
    var = variance(data_list)
    std1 = math.sqrt(var)
    return std1

def graph(std, mean, data_list):
    """
    this function collects a data list, standard dev
    and data list as parameters
    and calculates and returns the variance
    :param std: float, standard deviation that calcualted in the function std
    :param mean: float,mean value that calculated in the function mean
    :param data_list:float, the list is taken from the user inputs
    """
    graph_list = []
    for x in data_list:
        #abs function is used here
        graph_val = float(abs(x - mean))
        graph_list.append(graph_val)


    for category_number in range(0, 6):
        lower_bound = category_number * 0.5 * std
        upper_bound = (category_number + 1) * 0.5 * std
        count = 0
        if lower_bound == 0 and upper_bound == 0:
            print("Deviation is zero.")
            break

        else:
            for i in graph_list:
                if lower_bound <= i < upper_bound:
                    count+= 1

            print(f"Values between std. dev. {lower_bound:.2f}-{upper_bound:.2f}: {'*' * count}")

def main():
    """
    Gets the user input and stores it in a list
    """

    print("Enter the data, one value per line.\nEnd by entering empty line.")
    #this collects the values and stores them in a list, breaks with an empty space
    #using try and except
    data_list = []
    while True:
        try:
            data = float(input())
        except ValueError:
            break
        data_list.append(data)
    if len(data_list) < 2:
        print("Error: needs two or more values.")
    else:
        #returns mean value
        print(f"The mean of given data was: {mean(data_list):.2f}")
        #returns standard deviation
        print(f"The standard deviation of given data was: {std(data_list):.2f}")
        #return the graph function with all the neccessary parameters
        graph(std(data_list),mean(data_list),data_list)


if __name__=="__main__":
    main()