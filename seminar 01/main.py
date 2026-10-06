import random


#===============================================================
#                        FUNCTIONS
#===============================================================


def create_city(city_name: str, city_pop: int, city_county: str) -> dict:
    return {"name": city_name, "population": city_pop, "county": city_county}


def get_city_name(city: dict) -> str:
    return city["name"]


def get_city_pop(city: dict) -> int:
    return city["population"]


def get_city_county(city: dict) -> str:
    return city["county"]


def menu():
    print("1. Sort the cities.")
    print("2. Display the list of cities.")
    print("3.Search for a city (using partial, case-insensitive).")
    print("4.Add a city from the console")
    print("5. Add a number of random cities to the list (the number is reafd from the console).")
    print("6.quit")


def display_cities(city_list:list) -> None:
    for city in city_list:
        print(city)


def add_city(city_list: list, city: dict) -> None:
    city_list.append(city)


def sort_by_pop(city_list: list) -> None:
    for i in range(len(city_list)):
        for j in range(i+1 , len(city_list)):
            if get_city_pop(city_list[i]) > get_city_pop(city_list[j]):
                city_list[i], city_list[j] = city_list[j], city_list[i]


def get_random(n: int, city_list: list) -> None:
    for i in range(n):
        city = create_city("name" + str(i), random.randint(1, 100) * 1000, "county" + str(i))
        add_city(city_list, city)

#===============================================================
#                         MAIN
#===============================================================


def main():
    city_list = [
        {"name": "Targu Neamt", "population": 20_000, "county": "Neamt"},
        {"name": "Cluj-Napoca", "population": 400000, "county": "Cluj"},
        {"name": "Brasov", "population": 250_000, "county": "Brasov"}  # am completat restul pentru Brașov
    ]
    while True:
        menu()
        op = int(input("Select an option: "))

        if op == 6:
            break

        elif op == 1:
            sort_by_pop(city_list)

        elif op == 2:
            display_cities(city_list)

        elif op == 3:
            print("To be done")

        elif op == 4:
            cname = input("City name: ")
            cpop = int(input("City population: "))
            ccounty = input("City county: ")
            city = create_city(cname, cpop, ccounty)
            add_city(city_list , city)
        elif op == 5:
            n = int(input("Give me a number of cities to add: "))
            get_random(n, city_list)



main()