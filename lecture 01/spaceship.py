"""
basic git operations
    1. clone -> download the git repository locally (on my laptop)
    2. add -> tells git add the file to the repository
    3. commit -> tells git commit the file to the repository
    4. push -> synchronizes all the local commits to the server copy of the git repository
    5. pull -> download the changes that other people have pushed to the server git repository
"""

def calculate_checksum(flight_code : int) -> int :

    code = 0

    while flight_code >0:
        last_digit = flight_code % 10
        code += last_digit
        # / is real number division (result is float) , // is integer division (result is an int)
        flight_code //= 10
    return code

def get_flight_status(checksum : int) -> str:
    if checksum % 3 == 0:
        return "CLEARED"
    elif checksum % 3 == 1:
        return "MANULA CHECK"
    else:
        # none of the condition above
        return "CHECK"

def create_report(flight_code : int,checksum : int,status : int) ->dict:
    #python's dict is a collection of kye , value pairs, where keys are unique
    return {"CODE" : flight_code, "CHECK" : checksum, "STATUS" : status}


#print, input are builtin python 3 functions
#input return a str
operator_name = input("What is your name?")

#using str concatenation
print("Welcome to the control tower " + operator_name)

#enoty python list
flight_reports_list = []

while True:
    print()
    print("1. read landing code information")
    print("2. exit")

    option = input(">")
    if option == "1":
        landing_code = int(input("Landing code: "))
        checksum = calculate_checksum(landing_code)
        status = get_flight_status(checksum)

        flight_report = create_report(landing_code,checksum,status)
        flight_reports_list.append(flight_report)

        print(f"Landing code: {landing_code}, checksum: {checksum}, status: {status}")
        pass
    elif option == "2":
        break
    else:
        print("Invalid option")

""""
#using python f-strings
print( f"Welcome again to the control tower {operator_name}")

landing_code = input("landing code : ")
landing_code = int(landing_code)
checksum = calculate_checksum(landing_code)
print(checksum, get_flight_status(checksum))

print(f"Flight with code {landing_code} has checksum {checksum} and status {get_flight_status(checksum)}")
"""

