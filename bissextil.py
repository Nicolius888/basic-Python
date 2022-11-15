#Write a function that can tell if a year is bissextile or not.

year = int(input("input a year: "))

def isBissextile(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"The year {year} is bissextil"
    else: 
        return f"The year {year} in not bissextile"

print(isBissextile(year))


