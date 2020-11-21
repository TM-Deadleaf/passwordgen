import random
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase=uppercase.lower()
numbers="0123456789"
symbol="!@#$%^&*()_+"
upper=False
lower=True
numb=False
symbols=True
all=""
if upper:
    all+=uppercase
if lower:
    all+=lowercase
if numb:
    all+=numbers
if symbols:
    all+=symbol
length=20
amount=10
password=""
for x in range(amount):
    password="".join(random.sample(all,length))
    print(password)
