"""
this was written by Johnson apanishile
"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    all_list = dict()
    lines = []
    while True:
        message_line = input()
        if message_line == "":
            break
        lines.append(message_line)

    for line in lines:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in all_list:
                all_list[word] += 1
            else:
                all_list[word] = 1
    #getting the keys values
    keylist = all_list.keys()
    #sorting just the keys
    complete_key=sorted(keylist)
    for key in list(complete_key):
        print(key, ":", all_list[key], "times")


if __name__ == "__main__":
    main()