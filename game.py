import webbrowser  # Library for opening websites
import pyttsx3     # Library for text-to-speech functionality
import random      # Library for random choices

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a given message
def speak(message):
    engine.say(message)  # Pass the message to the TTS engine
    engine.runAndWait()  # Start the TTS process and wait till it completes

# Function to open a website
def open_website():
    speak("Please enter the website you want to open")
    url = input("Enter the website URL (e.g., https://www.example.com): ")
    
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url
    
    webbrowser.open(url)
    speak(f"Opening {url} in your default browser")
    print(f"Opening {url} in your default browser...")

# Function for the trivia game
def trivia_game():
    questions = [
        {"question": "What is the capital of France?", "answer": "paris"},
        {"question": "What is 5 + 7?", "answer": "12"},
        {"question": "Which planet is known as the Red Planet?", "answer": "mars"},
    ]

    funny_responses = [
        "Wrong, bro! Don't even think about trying again!",
        "Wrong answer! I knew you wouldn't know this, now watch this!",
        "Hey dude, that's wrong! Forget it, just look at this!",
    ]

    punishment_urls = [
        "https://www.youtube.com/shorts/WIvqO8TGwL4/",
        "https://www.youtube.com/shorts/Fky7nSpNOr8",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    ]

    question = random.choice(questions)
    speak(question["question"])
    print(question["question"])
    
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == question["answer"]:
        speak("Correct! You're a genius!")
        print("Correct! You're a genius!")
    else:
        funny_response = random.choice(funny_responses)
        speak(funny_response)
        print(funny_response)
        
        punishment_url = random.choice(punishment_urls)
        webbrowser.open(punishment_url)
        speak("Enjoy your punishment!")

# Function for the word game
def word_game():
    words = {
        "python": "A popular programming language.",
        "apple": "A tech giant and a fruit.",
        "ocean": "A vast body of saltwater.",
    }
    funny_responses = [
        "Wrong, bro! Don't even think about trying again!",
        "Wrong answer! I knew you wouldn't know this, now watch this!",
        "Hey dude, that's wrong! Forget it, just look at this!",
    ]

    punishment_urls = [
        "https://www.youtube.com/shorts/WIvqO8TGwL4/",
        "https://www.youtube.com/shorts/Fky7nSpNOr8",
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    ]

    # Randomly select a word to scramble
    word, hint = random.choice(list(words.items()))
    scrambled_word = ''.join(random.sample(word, len(word)))

    speak(f"Guess the word: {scrambled_word}. Here is a hint: {hint}")
    print(f"Scrambled Word: {scrambled_word}")
    print(f"Hint: {hint}")

    attempts = 3
    while attempts > 0:
        user_guess = input("Your guess: ").strip().lower()
        if user_guess == word:
            speak("Congratulations! You guessed it right!")
            print("Congratulations! You guessed it right!")
            return
        else:
            attempts -= 1
            speak(f"Wrong answer! You have {attempts} attempt(s) left.")
            print(f"Wrong answer! You have {attempts} attempt(s) left.")

    funny_response = random.choice(funny_responses)
    punishment_url = random.choice(punishment_urls)
    speak(funny_response)
    print(funny_response)
    webbrowser.open(punishment_url)
    speak("Enjoy your punishment!")

# Function for the math challenge
def math_challenge():
    score = 0
    problems_to_solve = 5

    for i in range(problems_to_solve):
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(["+", "-", "*"])
        question = f"{num1} {operation} {num2}"

        correct_answer = eval(question)
        speak(f"Solve: {question}")
        print(f"Question {i + 1}: {question}")

        try:
            user_answer = int(input("Your answer: ").strip())
            if user_answer == correct_answer:
                speak("Correct! Well done!")
                print("Correct! Well done!")
                score += 1
            else:
                speak(f"Wrong! The correct answer was {correct_answer}.")
                print(f"Wrong! The correct answer was {correct_answer}.")
        except ValueError:
            speak("Invalid input! Moving to the next question.")
            print("Invalid input! Moving to the next question.")

    speak(f"Your final score is {score} out of {problems_to_solve}.")
    print(f"Your final score is {score} out of {problems_to_solve}.")

# Main menu function
def main_menu():
    while True:
        print("""
        What would you like to do?
        1. Open a website
        2. Play a trivia game
        3. Play a word game
        4. Try a math challenge
        5. Exit
        """)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            open_website()
        elif choice == "2":
            trivia_game()
        elif choice == "3":
            word_game()
        elif choice == "4":
            math_challenge()
        elif choice == "5":
            speak("Goodbye! Have a great day!")
            print("Goodbye! Have a great day!")
            break
        else:
            speak("Invalid choice, please try again.")
            print("Invalid choice, please try again.")

# Main program execution
if __name__ == "__main__":
    speak("Hello Fauzan! Batman reporting for duty!")
    print("Hello Fauzan, this is Batman!")
    main_menu()
