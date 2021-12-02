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

def graph(std,mean,data_list):
    graph_val= []
    counter0 = 0
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    counter5 = 0

    for x in data_list:
        graph_val1 = abs(x - mean)
        graph_val.append(graph_val1)

    counter_list = []
    for checker in graph_val:

        if checker <= 0.5*std:
            counter0 +=1
            counter_list.append(counter0)

        elif 0.5*std<=checker<=1.0*std:
           counter1 +=1
           counter_list.append(counter1)

        elif 1.0*std<=checker<=1.5*std:
            counter2 +=1
            counter_list.append(counter2)

        elif 1.5*std<=checker<=2.0*std:
            counter3 +=1
            counter_list.append(counter3)

        elif 2.0*std<=checker<=2.5*std:
            counter4+=1
            counter_list.append(counter4)

        elif 2.5*std<=checker<=3.0*std:
            counter5+=1
            counter_list.append(counter5)

            for mark in counter_list:
                new_val = mark * "*"

    for category_number in range(0, 6):
            lower_bound = category_number * 0.5 * std
            upper_bound = (category_number + 1) * 0.5 * std

            something= counter2 * "*"
            print(f"Values between std. dev. {lower_bound:.2f}-{upper_bound:.2f}: {counter_list[4]}")





def main():

    data_list = [5,4,2,3,1,4,5,2]

    print(mean(data_list))
    print(variance(data_list))
    print(f"std result: {std(data_list):.2f}")
    print(graph(std(data_list),mean(data_list),data_list))
    print()


if __name__=="__main__":
    main()

