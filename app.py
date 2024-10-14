import streamlit as st
import math

# Function definitions for scientific calculator
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    return math.sqrt(x)

def log(x):
    return math.log(x)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Streamlit app interface
st.title("Scientific Calculator")

# Number inputs
num1 = st.number_input("Enter the first number", value=0.0)
num2 = st.number_input("Enter the second number (if required)", value=0.0)

# Select operation
operation = st.selectbox("Select operation", [
    "Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent"
])

# Perform calculation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
        st.write(f"Result: {num1} + {num2} = {result}")
    elif operation == "Subtract":
        result = subtract(num1, num2)
        st.write(f"Result: {num1} - {num2} = {result}")
    elif operation == "Multiply":
        result = multiply(num1, num2)
        st.write(f"Result: {num1} * {num2} = {result}")
    elif operation == "Divide":
        result = divide(num1, num2)
        st.write(f"Result: {num1} / {num2} = {result}")
    elif operation == "Power":
        result = power(num1, num2)
        st.write(f"Result: {num1} ^ {num2} = {result}")
    elif operation == "Square Root":
        result = sqrt(num1)
        st.write(f"Result: √{num1} = {result}")
    elif operation == "Logarithm":
        result = log(num1)
        st.write(f"Result: log({num1}) = {result}")
    elif operation == "Sine":
        result = sin(num1)
        st.write(f"Result: sin({num1}°) = {result}")
    elif operation == "Cosine":
        result = cos(num1)
        st.write(f"Result: cos({num1}°) = {result}")
    elif operation == "Tangent":
        result = tan(num1)
        st.write(f"Result: tan({num1}°) = {result}")
