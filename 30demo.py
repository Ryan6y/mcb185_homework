import sys

while True:
    ans = input("Enter your age:")
    try:
        age = int(ans)
        if 0 < age < 120:
            break
    except ValueError:
        pass
print(age, "its a great age")