def main():
    # Takes as inputs the name of the city one is born and the name of their
    # pet to generate a band name from the combination of the two.
    print("Welcome to the Band Name Generator.")
    city_name = input("What's the name of the city you grew up in?\n")
    pet_name = input("What's your pet's name?\n")
    band_name = " ".join([city_name, pet_name])
    print("Your band name could be", band_name)


if __name__ == "__main__":
    main()
