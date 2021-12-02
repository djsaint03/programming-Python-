"""
this was written by Johnson Apanishile
"""


def main():
    question=5
    scores=[]
    counter= 1
    while counter<=5:
        marks= float(input(f"Enter the time for performance {counter}: "))
        counter+=1
        scores.append(marks)


    max1 = max(scores)
    scores.remove(max1)

    min1= min(scores)
    scores.remove(min1)


    avg = sum(scores)/3
    print(f"The official competition score is {avg:.2f} seconds.")


if __name__=="__main__":
    main()