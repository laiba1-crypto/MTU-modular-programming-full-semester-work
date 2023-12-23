#Name: LAIBA ASIF
#StudentID: R00201303
from laiba_asif_Q4_class import ice_cream
def main():
    flavour = ice_cream("chocolate fudge", 6, 380)
    print(flavour.str())
    print(f"cal details: {flavour.describe_cal_per_scoop()}")

main()