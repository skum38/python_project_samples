"""
operators_examples.py

Simple, self-contained examples showing Python operators and their output.
Run this file to see examples of arithmetic, comparison, logical, assignment, bitwise,
membership, identity, ternary, chaining, and operator precedence.
"""

def arithmetic_examples():
    print("--- Arithmetic Operators ---")
    a, b = 7, 3
    print(f"a = {a}, b = {b}")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)
    print("a // b =", a // b)
    print("a % b =", a % b)
    print("a ** b =", a ** b)
    print()

def comparison_examples():
    print("--- Comparison Operators ---")
    x, y = 5, 10
    print("x =", x, "y =", y)
    print("x == y ->", x == y)
    print("x != y ->", x != y)
    print("x < y ->", x < y)
    print("x <= y ->", x <= y)
    print("x > y ->", x > y)
    print("x >= y ->", x >= y)
    print()

def assignment_examples():
    print("--- Assignment / Augmented Assignment ---")
    n = 4
    print("n initially ->", n)
    n += 3
    print("n after n += 3 ->", n)
    n *= 2
    print("n after n *= 2 ->", n)
    s = "hi"
    print("s initially ->", s)
    s += " there"
    print("s after s += ' there' ->", s)
    print()

def logical_examples():
    print("--- Logical Operators ---")
    print("True and False ->", True and False)
    print("True or False ->", True or False)
    print("not True ->", not True)
    # short-circuiting demonstration
    def truthy():
        print("truthy() called")
        return True
    print("False and truthy() ->", False and truthy())
    print("True or truthy() ->", True or truthy())
    print()

def bitwise_examples():
    print("--- Bitwise Operators ---")
    p, q = 5, 3  # 5 -> 0b0101, 3 -> 0b0011
    print("p =", p, "q =", q)
    print("p & q ->", p & q)
    print("p | q ->", p | q)
    print("p ^ q ->", p ^ q)
    print("~p ->", ~p)
    print("p << 1 ->", p << 1)
    print("p >> 1 ->", p >> 1)
    print()

def membership_identity_examples():
    print("--- Membership and Identity ---")
    lst = [1, 2, 3]
    print("2 in lst ->", 2 in lst)
    print("5 not in lst ->", 5 not in lst)
    a = b = [4, 5]
    c = [4, 5]
    print("a is b ->", a is b)
    print("a is c ->", a is c)
    print("a == c ->", a == c)
    print()

def ternary_and_chaining_examples():
    print("--- Ternary (conditional) and Chaining ---")
    val = 9
    print("'even' if val%2==0 else 'odd' ->", "even" if val % 2 == 0 else "odd")
    x = 3
    print("1 < x < 5 ->", 1 < x < 5)
    print()

def precedence_examples():
    print("--- Operator Precedence ---")
    print("Without parentheses: 2 + 3 * 4 =", 2 + 3 * 4)
    print("With parentheses: (2 + 3) * 4 =", (2 + 3) * 4)
    print()

if __name__ == '__main__':
    arithmetic_examples()
    comparison_examples()
    assignment_examples()
    logical_examples()
    bitwise_examples()
    membership_identity_examples()
    ternary_and_chaining_examples()
    precedence_examples()
