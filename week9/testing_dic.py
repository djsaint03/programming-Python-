



def main():
    network = { }
    filename = "friendships1.txt"
    file = open(filename, mode="r")

    for line in file:
        line = line.rstrip()

        # Any line in the input file which begins with # is
        # considered a comment line and is skipped.  You can
        # therefore add # characters in the beginning of the
        # lines to temporarily ignore some lines for testing
        # purposes.
        if len(line) > 0 and line[0] == "#":
            continue

        fields = line.split(";")

        #print(fields)
        for name in fields:
            if not name.isalpha():
                print(f"Fatal Error: '{name}' is not a valid name.")
                print(f"{name}------------------------------------")
                return None

        # "who" is the first name in the list eg.Helen in ['Helen', 'Greta', 'Florian', 'Irina']
        who = fields[0]
        for friend in fields[1:]:  # [0,'Greta', 'Florian', 'Irina']
            # Remember: add_friendship automatically records the
            # friendships in two ways: <friend> will be <who>'s friend,
            # and <who> will be <friend>'s friend.
            #print(f"{network},who: {who},whos friend: {friend}")
            network[who]=friend
            #print(f"who:{who} freinds::::{friend, sep= )
            #print(f"friends::::::{friend}")

        #for name in network:
            #print the name in the network
            #print(name)
            ##print the fact key that in name

            #print("-", network[name])

        #print(f"this is the network dict: {network}")


        #for connection in network.items():
            #print(connection)

    network101 = {"helen": ["greta", "helen", "florian"]}
    for friends in network101["helen"]:
        if friends =="helen":
            pass
        print(f"- {friends}")




if __name__ == "__main__":
    main()



