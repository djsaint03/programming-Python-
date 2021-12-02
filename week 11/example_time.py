



class Time:
    def __init__(self, hh = 0, mm = 0):
        self.__hh = hh
        self.__mm = mm

    def printout(self):
        print(f"{self.__hh:d}:{self.__mm:02d}")

    def minutes_from_midnight(self):
        """
        calculates and returns the hours before midnight
        """
        return self.__mm + self.__hh * 60

    def difference_in_minutes(self, time_object):
        """
        introduces an object as parameter
        this object which is a parameter gets used "time_object.minutes_from_midnight()"
        and is subtracted by the value of the main object itself  and the value is returned.
        """
        return time_object.minutes_from_midnight() - self.minutes_from_midnight()

    def difference_as_time_object(self, time_object):
        """
        note: calls a fellow method

        """
        time_difference = self.difference_in_minutes(time_object)
        hours = time_difference // 60
        minutes = time_difference % 60

        result_object = Time(hours, minutes)
        return result_object


    def is_earlier_than(self, time_object):
        return self.difference_in_minutes(time_object) > 0



def main():
    wakeup = Time(7, 15)
    bus_departure = Time(8, 18)
    time_for_morning_activities = wakeup.difference_in_minutes(bus_departure)
    #print(time_for_morning_activities)
    see = wakeup.difference_in_minutes(bus_departure)
    #print(see/60)
    a_val =wakeup.difference_as_time_object(bus_departure)
    a_val.printout()





if __name__ == "__main__":
    main()



