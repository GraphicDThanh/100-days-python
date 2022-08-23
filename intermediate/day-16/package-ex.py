# Note: Need to install package "prettytable"
# https://pypi.org/project/prettytable/
# https://github.com/jazzband/prettytable
from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Pokemon Name", "Type"]
x.add_row(["Chespin", "Grass"])
x.add_row(["Fennekin", "Fire"])
x.add_row(["Froakie", "water"])

print(x)