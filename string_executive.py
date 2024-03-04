code_to_execute = """
def greet(name):
    print("Hello, " + name + "!")

greet("World")
"""

try:
    exec(code_to_execute)
except Exception as e:
    print(f"An error occurred: {e}")
