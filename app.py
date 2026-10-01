def process_input(value):
     if not value.strip():
       print("Error: input cannot be empty")
       return
     print(f"Input accepted: {value}")

user_input = input("Enter something: ")
process_input(user_input)

