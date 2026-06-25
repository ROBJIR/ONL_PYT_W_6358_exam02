# answer3.py
# - exam2
# robert.jiranek@gmail.com

def dividers(number: int):
    for i in range(1, ( number // 2 ) +1 ):
        if number % i == 0:
            yield i    # generator
    yield number

if __name__ == '__main__':
    for i in dividers(33):
       print(i)