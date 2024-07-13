import datetime
import random
from colorama import Fore, Style


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
        return f"I'm sorry to hear that, {user_name}! Your motivational quote is:\n {feeling_color}{quotes_for_sadness}.{Style.RESET_ALL}  \nHow else are you feeling?"
    elif "angry" in user_input:
        quotes_for_anger = random.choice(angry_motivational_quotes)
        feeling_color = feeling_colors["angry"]
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_anger}.{Style.RESET_ALL}  \nHow else are you feeling?"
    elif "unhappy" in user_input:
        quotes_for_unhappiness = random.choice(unhappy_motivational_quotes)
        feeling_color = feeling_colors["unhappy"]
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_unhappiness}.{Style.RESET_ALL}  \nHow else are you feeling?"
    elif "annoyed" in user_input:
        quotes_for_annoyance = random.choice(annoyed_motivational_quotes)
        feeling_color = feeling_colors["annoyed"]
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_annoyance}.{Style.RESET_ALL} \nHow else are you feeling?"
    elif "frustrated" in user_input:
        quotes_for_frustration = random.choice(frustrated_motivational_quotes)
        feeling_color = feeling_colors["frustrated"]
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_frustration}.{Style.RESET_ALL} \nHow else are you feeling?"
    elif "lonely" in user_input:
        quotes_for_loneliness = random.choice(lonely_motivational_quotes)
        feeling_color = feeling_colors["lonely"]
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_loneliness}.{Style.RESET_ALL}  \nHow else are you feeling?"
    elif "stressed" in user_input:
        quotes_for_stress = random.choice(stressed_motivational_quotes)
        feeling_color = feeling_colors["stressed"]
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_stress}. {Style.RESET_ALL} \nHow else are you feeling?"
    elif "tired" in user_input:
        quotes_for_tiredness = random.choice(tired_motivational_quotes)
        feeling_color = feeling_colors["tired"]
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_tiredness}{Style.RESET_ALL}  \nHow else are you feeling?"
    elif "happy" in user_input:
        quotes_for_happiness = random.choice(happy_motivational_quotes)
        feeling_color = feeling_colors["happy"]
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_happiness}.{Style.RESET_ALL}  \nHow else are you feeling?"
    elif "excited" in user_input:
        quotes_for_excitement = random.choice(excited_motivational_quotes)
        feeling_color = feeling_colors["excited"]
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_excitement}.{Style.RESET_ALL}  \nHow else are you feeling?"
    elif "motivated" in user_input:
        quotes_for_motivation = random.choice(motivated_motivational_quotes)
        feeling_color = feeling_colors["motivated"]
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_motivation}{Style.RESET_ALL} \nHow else are you feeling?"
    elif "inspired" in user_input:
        quotes_for_inspiration = random.choice(inspired_motivational_quotes)
        feeling_color = feeling_colors["inspired"]
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is:\n {feeling_color}{quotes_for_inspiration}.{Style.RESET_ALL}  \nHow else are you feeling?"
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


#def case insensitive
def case_insensitive(user_input):
    responses = ["sad", "angry", "unhappy", "annoyed", "frustrated", "lonely", "stressed", "tired", "happy", "excited", "motivated", "inspired"]
    
    # Calculate similarity based on matching characters and length difference
    def similarity(x, y):
        matching_chars = sum(1 for a, b in zip(x, y) if a == b)
        length_difference = abs(len(x) - len(y))
        return matching_chars - length_difference
    
    closest_match = max(responses, key=lambda x: similarity(x, user_input.lower()))
    
    if user_input.lower() != closest_match:
        print(f"Chatbot: Did you mean '{closest_match}'?")
    
    return closest_match

# Main function to run the chatbot
def main():

    print("Hello! Welcome to the simple Python chatbot!")
    
    user_name = input("What's your name? ")
    greeting = get_greeting()
    
    print(f"{greeting}, {user_name}!  I'm here to motivate you.  How are you feeling today? I have quotes for the  following moods or feelings: \nsad, angry, unhappy, annoyed, frustrated, lonely, stressed, tired, happy, excited, motivated, inspired.")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        # match case insensitive
        if user_input.lower() in ["bye", "goodbye"]:
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        else:
            user_input = case_insensitive(user_input)
        
        response = get_response(user_input, user_name)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()