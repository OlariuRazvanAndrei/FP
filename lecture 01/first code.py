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

#print, input are builtin python 3 functions
#input return a str
operator_name = input("What is your name?")

#using str concatenation
print("Welcome to the control tower " + operator_name)

#using python f-strings
print( f"Welcome again to the control tower {operator_name}")

landing_code = input("landing code : ")
landing_code = int(landing_code)
checksum = calculate_checksum(landing_code)
print(checksum, get_flight_status(checksum))

print(f"Flight with code {landing_code} has checksum {checksum} and status {get_flight_status(checksum)}")


