"""
This was written and editted by Johnson Apanishile
Ohjelmointi 1 / Programming 1
Paracetamol/Panadol/Tylenol Dosing Advisor
"""

def calculate_dose(patients_weight, prev_dose_time, prev_day_ratio):
    """
    this function gets the calculation of dosage to
    be administed
    :param patients_weight:
    :param prev_dose_time:
    :param prev_day_ratio:
    :return:
    """
    patients_weight=int(patients_weight)
    prev_dose_time=int(prev_dose_time)
    prev_day_ratio= int(prev_day_ratio)
    amount = int()

    og_dose = patients_weight*15
    if prev_day_ratio + og_dose >= 4000 and prev_dose_time <= 6:
        amount = prev_day_ratio % og_dose


    if prev_day_ratio+og_dose <= 4000 and prev_dose_time <= 6:
        amount = og_dose

    return amount




def main():
    pw = input("Patient's weight (kg): ")
    pdt = input("How much time has passed from the previous dose (full hours): ")
    pdr = input("The total dose for the last 24 hours (mg): ")
    print(f"The amount of Parasetamol to give to the patient: ",calculate_dose(pw, pdt, pdr))

    # calculate_dose assumes parameters to be of type int
    # and they should be passed in the order: weight, time, total_doze_24
    # (or more like the automated tests assume this)


if __name__ == "__main__":
  main()
