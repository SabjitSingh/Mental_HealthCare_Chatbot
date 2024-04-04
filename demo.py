def ask_name():
    return input("Hello! I'm here to assist you with your mental health. What's your name? ")

def verify_gender():
    gender = input("Please enter your gender (Male/Female): ").capitalize()
    while gender not in ['Male', 'Female']:
        print("Invalid input. Please enter 'Male' or 'Female'.")
        gender = input("Please enter your gender (Male/Female): ").capitalize()
    return gender

def ask_age():
    age = input("Please enter your age: ")
    while not age.isdigit():
        print("Invalid input. Please enter a valid age.")
        age = input("Please enter your age: ")
    return age

def ask_feelings():
    print("How are you feeling today?")
    feelings = input("Feelings: ")
    return feelings

def provide_support(feelings):
    if 'sad' in feelings.lower():
        print("I'm here to support you. It's important to take care of your mental health. Would you like to talk more about what's bothering you?")
    elif 'anxious' in feelings.lower():
        print("Feeling anxious can be tough. Remember to take deep breaths and try to focus on the present moment. Would you like some relaxation exercises?")
    else:
        print("It's great to hear that you're feeling good! Remember to practice self-care and reach out for support if you ever need it.")

def main():
    name = ask_name()
    print(f"Hello, {name}! Let's talk about your mental health.")
    
    gender = verify_gender()
    print(f"Great! Your gender is {gender}.")
    
    age = ask_age()
    print(f"Thank you for providing your age, {age}.")
    
    feelings = ask_feelings()
    provide_support(feelings)

if __name__ == "__main__":
    main()
