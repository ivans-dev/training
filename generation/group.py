from model.group import Group
from faker import Faker
import os
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n = 5
f = "groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

fake = Faker('ru_RU')
data = [Group(name="", header="", footer="")] + [
    Group(name=fake.unique.name(), header=fake.unique.job(), footer=fake.unique.bs())
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."+f)

with open(file, "w") as f:
    f.write(json.dumps(data, default=lambda x: x.__dict__, indent=2))
