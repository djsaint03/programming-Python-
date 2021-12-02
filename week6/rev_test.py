def reverse_name(names):
    """
    this function reverses the order of
    name if furfilled by conditions
    """
    new = names.split(",")


    if names == ",":
        return ""

    elif "," in names:
        new = names.split(",")
        return new[1].strip() + " " + new[0].strip()


    elif " " in names:
        new = names.split(" ")
        return new[0].strip() + " " + new[1].strip()

    else:
        return names




def main():
    print(reverse_name("Bond,James"))
    print(reverse_name(",James"))
    print(reverse_name("    Bond    ,     James"))
    print(reverse_name("Bond,  "))
    print(reverse_name("Bond James"))
    print(reverse_name(","))
    print(reverse_name("Mando"))




if __name__=="__main__":
    main()

"""
  #letter=sentence[0].capitalize()
  for letter in range(len(sentence)):
      if sentence[letter]== " ":
          first_letter=sentence[0].capitalize()
          letter = sentence[0].capitalize(),sentence[letter+1].capitalize()
          #print(first_letter)
          print(letter)


  compound = wordss.split()
  print(compound)
  for words in range(len(compound)):
      compound[words]=

      print makes it loop through all words
      but if you define that variable it gives
      the first or the last 
      print(words[0],end="")

          #single = list(words)
          #first_letter = single[0].upper()
          return #first_letter
  """