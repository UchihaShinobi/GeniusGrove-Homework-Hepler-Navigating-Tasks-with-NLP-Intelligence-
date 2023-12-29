import streamlit as st
from fractions import Fraction
import statistics
import math
from streamlit_lottie import st_lottie
import json

# Existing code for mathematics problem solver

def basic_arithmetic_operation(operation, num1, num2):
    if operation == "Addition":
        result = num1 + num2
        steps = f"Expression: {num1} + {num2}\nResult: {result}"
    elif operation == "Subtraction":
        result = num1 - num2
        steps = f"Expression: {num1} - {num2}\nResult: {result}"
    elif operation == "Multiplication":
        result = num1 * num2
        steps = f"Expression: {num1} * {num2}\nResult: {result}"
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            steps = f"Expression: {num1} / {num2}\nResult: {result}"
        else:
            result = "Cannot divide by zero"
            steps = "Division by zero is undefined"
    else:
        result = "Invalid operation"
        steps = "Please select a valid operation"
    
    return result, steps

def square_and_square_root(num, operation):
    if operation == "Square":
        result = num ** 2
        steps = f"Expression: Square of {num} = {result}"
    elif operation == "Square Root":
        result = math.sqrt(num)
        steps = f"Expression: Square root of {num} = {result}"
    else:
        result = "Invalid operation"
        steps = "Please select a valid operation"
    
    return result, steps

def fraction_operation(operation, fraction1_numerator, fraction1_denominator, fraction2_numerator, fraction2_denominator):
    if fraction1_denominator == 0 or fraction2_denominator == 0:
        result = "Invalid input. Denominator cannot be zero."
        steps = "Invalid input"
    else:
        fraction1 = Fraction(fraction1_numerator, fraction1_denominator)
        fraction2 = Fraction(fraction2_numerator, fraction2_denominator)

        if operation == "Addition":
            result = fraction1 + fraction2
            steps = f"Expression: {fraction1} + {fraction2}\nResult: {result}"
        elif operation == "Subtraction":
            result = fraction1 - fraction2
            steps = f"Expression: {fraction1} - {fraction2}\nResult: {result}"
        elif operation == "Multiplication":
            result = fraction1 * fraction2
            steps = f"Expression: {fraction1} * {fraction2}\nResult: {result}"
        elif operation == "Division":
            if fraction2 != 0:
                result = fraction1 / fraction2
                steps = f"Expression: {fraction1} / {fraction2}\nResult: {result}"
            else:
                result = "Cannot divide by zero"
                steps = "Division by zero is undefined"
        else:
            result = "Invalid operation"
            steps = "Please select a valid operation"

    return result, steps

def location_statistics(data, statistic):
    mean = statistics.mean(data) if 'mean' in statistic else None
    mode = statistics.mode(data) if 'mode' in statistic else None
    median = statistics.median(data) if 'median' in statistic else None
    
    steps = ""
    if 'mean' in statistic:
        steps += f"Step 1: Calculate the mean of the dataset\nMean: {mean}\n\n"
    if 'mode' in statistic:
        steps += f"Step 2: Identify the mode of the dataset (the most frequent value)\nMode: {mode}\n\n"
    if 'median' in statistic:
        steps += f"Step 3: Find the median (the middle value when the dataset is sorted)\nMedian: {median}"
    
    return mean, mode, median, steps

def perimeter_circle(radius):
    perimeter = 2 * math.pi * radius
    steps = f"Expression: Perimeter = 2 * π * {radius}\nResult: {perimeter}"
    return perimeter, steps

def perimeter_rectangle(length, width):
    perimeter = 2 * (length + width)
    steps = f"Expression: Perimeter = 2 * ({length} + {width})\nResult: {perimeter}"
    return perimeter, steps

def perimeter_square(side):
    perimeter = 4 * side
    steps = f"Expression: Perimeter = 4 * {side}\nResult: {perimeter}"
    return perimeter, steps

def logarithmic_operations(num, operation, base):
    if num <= 0 or base <= 0 or base == 1:
        result = "Invalid input. Please ensure the number and base are positive and the base is not equal to 1."
        steps = "Invalid input"
    else:
        if operation == "Logarithm":
            result = math.log(num, base)
            steps = f"Expression: Log base {base} of {num} = {result}"
        elif operation == "Exponentiation":
            result = base ** num
            steps = f"Expression: {base} raised to the power of {num} = {result}"
        else:
            result = "Invalid operation"
            steps = "Please select a valid operation"

    return result, steps

def main():
    st.header("MathMinder🤖")

    operation = st.selectbox("Select Operation", ["Basic Arithmetic", "Fractions", "Square and Square Root", "Logarithmic Operations", "Location Statistics", "Geometric Properties"])

    if operation == "Basic Arithmetic":
        num1 = st.number_input("Enter the first number", step=1)
        num2 = st.number_input("Enter the second number", step=1)
        selected_operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])
        result, steps = basic_arithmetic_operation(selected_operation, num1, num2)
        st.success(f"Result of {selected_operation}: {result}")
        st.write(f"Steps:\n{steps}")

    elif operation == "Fractions":
        fraction1_numerator = st.number_input("Enter the numerator of the first fraction", step=1)
        fraction1_denominator = st.number_input("Enter the denominator of the first fraction", step=1)
        fraction2_numerator = st.number_input("Enter the numerator of the second fraction", step=1)
        fraction2_denominator = st.number_input("Enter the denominator of the second fraction", step=1)
        selected_operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])
        
        result, steps = fraction_operation(selected_operation, fraction1_numerator, fraction1_denominator, fraction2_numerator, fraction2_denominator)
        st.success(f"Result of {selected_operation}: {result}")
        st.write(f"Steps:\n{steps}")

    elif operation == "Square and Square Root":
        num = st.number_input("Enter a number")
        selected_operation = st.radio("Select Operation", ["Square", "Square Root"])
        result, steps = square_and_square_root(num, selected_operation)
        st.success(f"Result of {selected_operation}: {result}")
        st.write(f"Steps:\n{steps}")

    elif operation == "Logarithmic Operations":
        num = st.number_input("Enter a number")
        selected_operation = st.selectbox("Select Operation", ["Logarithm", "Exponentiation"])
        base = st.number_input("Enter the base for logarithm/exponentiation", min_value=2)
        result, steps = logarithmic_operations(num, selected_operation, base)
        st.success(f"Result of {selected_operation} with base {base}: {result}")
        st.write(f"Steps:\n{steps}")

    elif operation == "Location Statistics":
        data_input = st.text_area("Enter a list of numbers separated by commas (e.g., 1, 2, 3, 4)")
        data = [float(x.strip()) for x in data_input.split(",") if x.strip()]
        
        statistic_options = st.checkbox("Choose Statistics to Calculate", ['mean', 'mode', 'median'])
        if statistic_options:
            selected_statistics = st.multiselect("Select statistics to calculate", ['mean', 'mode', 'median'])
            mean, mode, median, steps = location_statistics(data, selected_statistics)
            st.success("Statistics:")
            if 'mean' in selected_statistics:
                st.write(f"Mean: {mean}")
            if 'mode' in selected_statistics:
                st.write(f"Mode: {mode}")
            if 'median' in selected_statistics:
                st.write(f"Median: {median}")
            st.write(f"Steps:\n{steps}")

    elif operation == "Geometric Properties":
        geometric_shape = st.selectbox("Select Geometric Shape", ["Circle", "Rectangle", "Square"])
        if geometric_shape == "Circle":
            radius = st.number_input("Enter the radius of the circle")
            perimeter, steps = perimeter_circle(radius)
            st.success(f"Perimeter of the circle: {perimeter}")
            st.write(f"Steps:\n{steps}")
        elif geometric_shape == "Rectangle":
            length = st.number_input("Enter the length of the rectangle")
            width = st.number_input("Enter the width of the rectangle")
            perimeter, steps = perimeter_rectangle(length, width)
            st.success(f"Perimeter of the rectangle: {perimeter}")
            st.write(f"Steps:\n{steps}")
        elif geometric_shape == "Square":
            side = st.number_input("Enter the side length of the square")
            perimeter, steps = perimeter_square(side)
            st.success(f"Perimeter of the square: {perimeter}")
            st.write(f"Steps:\n{steps}")

if __name__ == "__main__":
    main()
