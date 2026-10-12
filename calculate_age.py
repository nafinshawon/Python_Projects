#take input from the user
#year month day
#input
#calculate age -> function
#   current date -> today()
#2 functions calculation of age taking input
# error handling

from datetime import date
#print("Enter Your Birthday: ")
def get_birthday():
    try:
        year = int(input("Enter your year: "))
        month = int(input("Enter your month: "))
        day = int(input("Enter your day: "))

        birthdate=date(year,month,day)
        #print(birthdate)
        return birthdate
    except Exception as e:
        print("Enter the valid date",e)

#Birthday = gate_birthday()
#print("Birthday: ",Birthday)


def get_age(Birthday):
    date_today = date.today()
    #print("Today: ",date_today)

    age = (
        date_today.year
        -Birthday.year
        -((date_today.month,date_today.day)<(Birthday.month,Birthday.day))
    )
    #print(age)
    return age

def main():
    print("-----------Age Calculator----------")
    Birthday = get_birthday()
    Age = get_age(Birthday)
    print("Age: ",Age)

if __name__=="__main__":
    main()