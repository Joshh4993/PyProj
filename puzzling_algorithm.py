a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))

inp_a = a
inp_b = b

a = a + b
b = a - b
a = a - b

print(f"Input\nFirst: {inp_a} | Second: {inp_b}\n\nOutput\nFirst: {a} | Second: {b}")