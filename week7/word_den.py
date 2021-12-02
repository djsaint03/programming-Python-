"""
this was written by Johnson apanishile
"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    all_list = dict()
    text = []

    while True:
        message_text = input()
        if message_text == "":
            break
        text.append(message_text)

    for words in text:
        words = words.strip()
        words = words.lower()
        text_words = words.split(" ")
        for word in text_words:
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