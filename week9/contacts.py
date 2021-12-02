"""
COMP.CS.100 Programming 1
Name: Johnson Apanishile

"""
import csv

def read_file(filename):

        file = open(filename, "r")
        contact_read=file.read()

        something=contact_read.split(";")
        print(something)

        contact_dict={ }
"""
        for lines in something:
            contact_dict[lines[0]]= {"name":lines[1],"phone":lines[2],"email":lines[3], "skype":lines[4]}
            print(contact_read)
"""

        fee = open("contacts.csv", "r")
        reader = csv.reader(fee)
        contact_csv = { }




#key;name;phone;email;skype


def main():
    read_file("contacts.csv")


if __name__ == "__main__":
        main()
