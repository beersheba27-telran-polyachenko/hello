#tuple
"""
     0.  1.  2.  3. 4
a = [9, 23, 98, 12, 7]

tuple
     0. 1. 2.  3. 4
t = (8, 2, 9, 12, 6)

"""
#             0.      1.      2.      3
names = ("Hanna", "Adam", "Alex", "Oleg")
first, second, third, fourth = names
print(first)
print(second)
print(third)
print(fourth)

names_list: list = list(names)
names_list[0] = "Kirill"
names_list.insert(1, "Liliya")
print(names_list)
print(names)
names = tuple(names_list)
print(names)

def salary(hours: float, wage: float, tax: float):
    salary_gross = hours * wage
    tax_value = (salary_gross * tax) / 100
    salary_netto = salary_gross - tax_value
    return salary_netto, tax_value, salary_gross

netto, tx, gross = salary(200, 100, 20)
print(f"gross: {gross: .2f} NIS")
print(f"tax: {tx: .2f} NIS")
print(f"netto: {netto : .2f} NIS")

a = 3.234
print("a =", a) #concat
print(f"a = {a:.2f}") # format