import streamlit as st
import math

# App Title
st.title("🧮 Advanced Calculator App")

# Description
st.write("Perform basic, scientific, and expression-based calculations easily!")

# Calculator modes
mode = st.radio("Select Mode:", ["Basic", "Scientific", "Expression"])

# Basic Calculator
if mode == "Basic":
    num1 = st.number_input("Enter first number:", value=0.0)
    num2 = st.number_input("Enter second number:", value=0.0)

    operation = st.selectbox(
        "Select Operation:",
        ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (x^y)")
    )

    if st.button("Calculate"):
        if operation == "Addition (+)":
            result = num1 + num2
        elif operation == "Subtraction (-)":
            result = num1 - num2
        elif operation == "Multiplication (×)":
            result = num1 * num2
        elif operation == "Division (÷)":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Division by zero is not allowed!")
                result = None
        elif operation == "Power (x^y)":
            result = num1 ** num2

        if result is not None:
            st.success(f"Result: {result}")

# Scientific Calculator
elif mode == "Scientific":
    operation = st.selectbox(
        "Select Scientific Function:",
        ("Square Root", "Percentage", "sin(x)", "cos(x)", "tan(x)", "log(x)", "exp(x)")
    )
    num = st.number_input("Enter number:", value=0.0)

    if st.button("Calculate"):
        try:
            if operation == "Square Root":
                result = math.sqrt(num)
            elif operation == "Percentage":
                result = num / 100
            elif operation == "sin(x)":
                result = math.sin(math.radians(num))
            elif operation == "cos(x)":
                result = math.cos(math.radians(num))
            elif operation == "tan(x)":
                result = math.tan(math.radians(num))
            elif operation == "log(x)":
                result = math.log(num)
            elif operation == "exp(x)":
                result = math.exp(num)

            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Error: {e}")

# Expression Calculator
elif mode == "Expression":
    st.write("Enter a full mathematical expression like:")
    st.code("2 + 3 * 4 / 2 - (5 ** 2)", language="python")

    expression = st.text_input("Enter Expression:")

    if st.button("Evaluate"):
        try:
            result = eval(expression)
            st.success(f"Result: {result}")
        except Exception as e:
            st.error(f"Invalid Expression! Error: {e}")
