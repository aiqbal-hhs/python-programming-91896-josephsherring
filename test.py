def addition():
    value_one = int(input("Pick a number: "))
    value_two = int(input("Pick another number: "))
    print("Adding these two values will get you", value_one + value_two)
import time
print("1*10 = ", 1*10)

addition()

i=0
print("here is a loop which counts us from 0 every 0.2 seconds")
while i <= 10000000:
    print(i)
    i += 1
    time.sleep(0.2)
