# Calculator Module - IT215 DevOps Demo
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Đã sửa lại đúng phép chia và xử lý ngoại lệ chia cho 0
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
