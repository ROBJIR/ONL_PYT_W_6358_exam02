# answer3.py
# - exam2
# robert.jiranek@gmail.com

def dividers(number: int):
    divs=[]
    for i in range(1, number + 1):
        if number % i == 0:
            yield i    # generator

for i in dividers(12):
    print(i)