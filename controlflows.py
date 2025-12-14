# 1. IF-ELIF-ELSE
age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

# 2. FOR LOOP
for i in range(5):
    print(f"Count: {i}")

for j in ["apple", "banana", "cherry"]:
    print(f"Fruit: {j}")

# 3. WHILE LOOP
count = 0
while count < 3:
    print(f"Loop {count}")
    count += 1

# 4. BREAK STATEMENT
for i in range(10):
    if i == 5:
        break
    print(i)

# 5. CONTINUE STATEMENT
for i in range(5):
    if i == 2:
        continue
    print(i)

# 6. FOR-ELSE
for i in range(3):
    print(i)
else:
    print("Loop completed")

# 7. NESTED LOOPS
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 8. TERNARY OPERATOR
status = "Pass" if 85 >= 60 else "Fail"
print(status)