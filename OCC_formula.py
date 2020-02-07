import pyperclip

while True:

    def occ_function():
        num_1 = input("What OCC portal has: ")
        num_2 = input("What our spreadsheet has: ")
        try:
            pyperclip.copy((((float(num_1)-float(num_2))/1.5)))
            return ((float(num_1)-float(num_2))/1.5)
        except:
            return "Sorry I dont understand"

    print(occ_function())

