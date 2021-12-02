import math
from math import sqrt


def mean(data_list):
    n= len(data_list)
    mean = sum(data_list)/n
    return mean

def variance(data_list):
    n= len(data_list)
    mean = sum(data_list) / n
    dev = [(x - mean) ** 2 for x in data_list]
    variance = sum(dev) / (n-1)
    return variance

def std(data_list):
    var = variance(data_list)
    std1 = math.sqrt(var)
    return std1

def graph(std, mean, data_list):
    graph_list = []
    for x in data_list:
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

    print("Enter the data, one value per line.\nEnd by entering empty line.")

    data_list = []
    while True:
        try:
            data = int(input())
        except ValueError:
            break
        data_list.append(data)
    if len(data_list) < 2:
        print("Error: needs two or more values.")
    else:
        print(f"The mean of given data was: {mean(data_list):.2f}")
        print(f"The standard deviation of given data was: {std(data_list):.2f}")
        graph(std(data_list),mean(data_list),data_list)


    #data_list1 = [5,4,2,3,1,4,5,2]

    #print(mean(data_list))
    #print(variance(data_list))
    #print(f"std result: {std(data_list):.2f}")
    #print(graph(std(data_list),mean(data_list),data_list))
    #print()
    """
        data_list = []
        dev_list= []
        while True:
            try:
                data = int(input())
            except ValueError:
                break
            data_list.append(data)

        if len(data_list) < 2:
            print("Error: needs two or more values.")

        else:
            mean = sum(data_list) / len(data_list)

            print(f"The mean of given data was: {mean:.2f}")

        for x in data_list:

            dev = x-(sum(data_list) / len(data_list))
            print(dev)
            dev_list.append(dev)
            variance = sum(dev_list) / len(data_list)
            sd= math.sqrt(variance)
            print(sd)
    """

    """
        data_list =[]
        while True:
            try:
                data = int(input())
            except ValueError:
                break
            data_list.append(data)



        if len(data_list) <2:
            print("Error: needs two or more values.")

        else:
            mean = sum(data_list)/len(data_list)
            sd =
            print(f"The mean of given data was: {mean:.2f}")

    """


if __name__=="__main__":
    main()

