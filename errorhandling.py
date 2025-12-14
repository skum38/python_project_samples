# 1. Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# 2. Multiple exceptions
try:
    data = int("abc")
except ValueError:
    print("Invalid integer format")
except TypeError:
    print("Type error occurred")

# 3. Catch all exceptions (not recommended)
try:
    x = some_undefined_variable
except Exception as e:
    print(f"Error: {e}")

# 4. Finally clause (always executes)
try:
    file = open("test.py")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    if 'file' in locals():
        file.close()

# 5. Else clause (executes if no exception)
try:
    num = int("42")
except ValueError:
    print("Invalid number")
else:
    print(f"Successfully converted: {num}")

# 6. Raising custom exceptions
class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong")
except CustomError as e:
    print(f"Caught custom error: {e}")

# 7. Using context managers (with statement)
with open("test.py", "a+", encoding="utf-8") as f:
    f.write("New appended line.\n")
    f.flush()
    f.seek(0)
    content = f.read()
    print(content)
# File automatically closes here