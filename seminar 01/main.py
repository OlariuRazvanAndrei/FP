#===============================================================
#                        FUNCTIONS
#===============================================================


def create_city(city_name: str, city_pop:int, city_county:str) ->list:
    return[city_name, city_pop, city_county]


def get_city_name(city:list) -> str:
    return city[0]


def get_city_pop(city:list) -> int:
    return city[1]


def get_city_county(city:list) -> int:
    return city[2]


def menu():
    print("1. Sort the cities.")
    print("2. Display the list of cities.")
    print("3.Search for a city (using partial, case-insensitive).")
    print("4.Add a city from the console")
    print("5. Add a number of random cities to the list (the number is read from the console).")
    print("6.quit")


def display_cities(city_list:list) -> None:
    for city in city_list:
        print(city)


def add_city(city_list: list , city: str) -> None:
    city_list.append(city)


def sort_by_pop(city_list: list) -> None:
    for i in range(len(city_list)):
        for j in range(i+1 , len(city_list)):
            if get_city_pop(city_list[i]) > get_city_pop(city_list[j]):
                city_list[i], city_list[j] = city_list[j], city_list[i]


#===============================================================
#                         MAIN
#===============================================================


def main():
    city_list = [["Targu Neamt" , 20_000 , "Neamt"] , ["Cluj-Napoca" , 400000 , "Cluj"] , ["Brasov" , 300_000 , "Brasov"] ]
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
            print("To be done")


main()