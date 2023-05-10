from temperature import Temperature

def main():
    print("The Convert Temperatures program")

    again = "y"
    while again.lower() == "y":
        # instantiate temp with initial values of 32F and 0C
        temp = Temperature(32, 0)
        # prompt the user to convert a temperature
        temp.convert_temp()

        print()
        again = input("Convert another temperature? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()
