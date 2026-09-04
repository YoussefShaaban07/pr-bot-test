import os

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def get_user_data(user_id):
    password = "admin123"
    query = "SELECT * FROM users WHERE id = " + user_id
    return query
