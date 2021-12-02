"""
this was written by Johnson Apanishile
"""

def main():
    month_num = 12
    for x in range(1):
        do_main_loop = True
        while do_main_loop:
            for month_num in range(1, month_num + 1):
                if (month_num == 2):
                    day_num = 28
                elif (month_num == 4) or (month_num == 6) or (month_num == 9) or (
                        month_num == 11):
                    day_num = 30
                else:
                    day_num = 31
                for day in range(1, day_num + 1):
                    print(f"{day}.{month_num}.")

                do_main_loop = False

if __name__ == "__main__":
    main()