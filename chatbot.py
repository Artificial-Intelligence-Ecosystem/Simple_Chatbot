import datetime
import random
from colorama import Fore, Style
import tkinter as tk


# Function to get a response based on user input
def get_response(user_input, user_name):
    user_input = user_input.lower()

    # array of motivational quotes for saddened users
    saddened_motivational_quotes = [
        "If you think you are too small to make a difference, try sleeping with a mosquito. -Ghandi",
        "There is no path to happiness. Happiness is the path. –Buddha",
        "The only way to find true happiness is to risk being completely cut open. -Chuck Palahniuk",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"]
    angry_motivational_quotes = [
        "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured. - Mark Twain",
        "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
        "Holding onto anger is like drinking poison and expecting the other person to die. - Buddha",
        "Anger makes dull men witty, but it keeps them poor. -Elizabeth I"]
    unhappy_motivational_quotes = [
        "There is no path to happiness. Happiness is the path. –Buddha",
        "The only way to find true happiness is to risk being completely cut open. -Chuck Palahniuk"]
    annoyed_motivational_quotes = [
        "Everything that irritates us about others can lead us to an understanding of ourselves. – Carl Jung",
        "The only way to get the best of an argument is to avoid it. - Dale Carnegie"]
    frustrated_motivational_quotes = [
        "Good decisions come from experience. Experience comes from making bad decisions. – Mark Twain",
        "The only way to do great work is to love what you do. - Steve Jobs"]
    lonely_motivational_quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Feeling sorry for yourself, and your present condition, is not only a waste of energy but the worst habit you could possibly have. – Dale Carnegie"]
    stressed_motivational_quotes = [
        "The greatest weapon against stress is our ability to choose one thought over another. – William James",
        "Don't stress. Do your best. Forget the rest."]
    tired_motivational_quotes = [
        "Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit. Then get back to work. - Ralph Marston",
        "The only way to do great work is to love what you do. - Steve Jobs"]
    happy_motivational_quotes = [
        "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
        "The only way to do great work is to love what you do. - Steve Jobs"]
    excited_motivational_quotes = [
        "Excitement is the fuel for achievement. Embrace it and let it drive you towards success!",
        "The only way to do great work is to love what you do. - Steve Jobs"]
    motivated_motivational_quotes = [
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt"]
    inspired_motivational_quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"]
    
    feeling_colors = {
    "happy": Fore.YELLOW,
    "sad": Fore.BLUE,
    "frustrated": Fore.MAGENTA,
    "angry": Fore.RED,
    "unhappy": Fore.CYAN,
    "annoyed": Fore.RED,
    "lonely": Fore.BLUE,
    "stressed": Fore.WHITE,
    "tired": Fore.BLUE,
    "excited": Fore.GREEN,
    "motivated": Fore.GREEN,
    "inspired": Fore.YELLOW
    # Add more feelings and colors as needed
}

    # Define responses based on specific keywords or phrases
    if "sad" in user_input:
        quotes_for_sadness = random.choice(saddened_motivational_quotes)
        feeling_color = feeling_colors["sad"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}! Your motivational quote is: {quotes_for_sadness}.  How else are you feeling?{Style.RESET_ALL}"
    elif "angry" in user_input:
        quotes_for_anger = random.choice(angry_motivational_quotes)
        feeling_color = feeling_colors["angry"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_anger}.  How else are you feeling?{Style.RESET_ALL}"
    elif "unhappy" in user_input:
        quotes_for_unhappiness = random.choice(unhappy_motivational_quotes)
        feeling_color = feeling_colors["unhappy"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_unhappiness}.  How else are you feeling?{Style.RESET_ALL}"
    elif "annoyed" in user_input:
        quotes_for_annoyance = random.choice(annoyed_motivational_quotes)
        feeling_color = feeling_colors["annoyed"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_annoyance}. How else are you feeling?{Style.RESET_ALL}"
    elif "frustrated" in user_input:
        quotes_for_frustration = random.choice(frustrated_motivational_quotes)
        feeling_color = feeling_colors["frustrated"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_frustration}.  How else are you feeling?{Style.RESET_ALL}"
    elif "lonely" in user_input:
        quotes_for_loneliness = random.choice(lonely_motivational_quotes)
        feeling_color = feeling_colors["lonely"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_loneliness}.  How else are you feeling?{Style.RESET_ALL}"
    elif "stressed" in user_input:
        quotes_for_stress = random.choice(stressed_motivational_quotes)
        feeling_color = feeling_colors["stressed"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_stress}.  How else are you feeling?{Style.RESET_ALL}"
    elif "tired" in user_input:
        quotes_for_tiredness = random.choice(tired_motivational_quotes)
        feeling_color = feeling_colors["tired"]
        return f"{feeling_color}I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_tiredness}  How else are you feeling?{Style.RESET_ALL}"
    elif "happy" in user_input:
        quotes_for_happiness = random.choice(happy_motivational_quotes)
        feeling_color = feeling_colors["happy"]
        return f"{feeling_color}I'm glad to hear that, {user_name}!  Your motivational quote is: {quotes_for_happiness}.  How else are you feeling?{Style.RESET_ALL}"
    elif "excited" in user_input:
        quotes_for_excitement = random.choice(excited_motivational_quotes)
        feeling_color = feeling_colors["excited"]
        return f"{feeling_color}I'm glad to hear that, {user_name}!  Your motivational quote is: {quotes_for_excitement}.  How else are you feeling?{Style.RESET_ALL}"
    elif "motivated" in user_input:
        quotes_for_motivation = random.choice(motivated_motivational_quotes)
        feeling_color = feeling_colors["motivated"]
        return f"{feeling_color}I'm glad to hear that, {user_name}!  Your motivational quote is: {quotes_for_motivation} How else are you feeling?{Style.RESET_ALL}"
    elif "inspired" in user_input:
        quotes_for_inspiration = random.choice(inspired_motivational_quotes)
        feeling_color = feeling_colors["inspired"]
        return f"{feeling_color}I'm glad to hear that, {user_name}!  Your motivational quote is: {quotes_for_inspiration}.  How else are you feeling?{Style.RESET_ALL}"
    elif "bye" in user_input or "goodbye" in user_input:
        return f"Goodbye, {user_name}! Have a great day!"
    else:
        return f"I'm sorry, {user_name}, I don't understand that. Can you please rephrase?"

# Function to get the current greeting based on the time of day
def get_greeting():
    now = datetime.datetime.now()
    current_hour = now.hour
    if current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"

# Main function to run the chatbot
def main():

    root = tk.Tk()
    root.title("Simple Chatbot")

    label = tk.Label(root, text="Hello! Welcome to the simple Python chatbot!")
    label.pack()

    nameLabel = tk.Label(root, text="What's your name?")
    nameLabel.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    button = tk.Button(root, text="Enter", command=lambda: show_quote(entry.get(), nameLabel))
    button.pack()

    greeting = get_greeting()

    responseLabel = tk.Label(root, text=f"{greeting}, {nameLabel}!  I'm here to motivate you.  How are you feeling today? I have quotes for the following moods or feelings: \nsad, angry, unhappy, annoyed, frustrated, lonely, stressed, tired, happy, excited, motivated, inspired.")
    responseLabel.pack()

    quoteLabel = tk.Label(root, text="")
    quoteLabel.pack()

    def show_quote(user_input, user_name):
        quote = get_response(user_input, user_name)
        quoteLabel.config(text=quote)

    root.mainloop()
    
    # print("Hello! Welcome to the simple Python chatbot!")
    
    # user_name = input("What's your name? ")
    # greeting = get_greeting()
    
    # print(f"{greeting}, {user_name}!  I'm here to motivate you.  How are you feeling today? I have quotes for the  following moods or feelings: \nsad, angry, unhappy, annoyed, frustrated, lonely, stressed, tired, happy, excited, motivated, inspired.")
    # print("Type 'bye' to exit.")
    
    # while True:
    #     user_input = input("You: ")
    #     if user_input.lower() in ["bye", "goodbye"]:
    #         print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
    #         break
    #     response = get_response(user_input, user_name)
    #     print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()