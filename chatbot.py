import datetime
import random


# Function to get a response based on user input
def get_response(user_input, user_name):
    user_input = user_input.lower()

    # array of motivational quotes for saddened users
    saddened_motivational_quotes = [
        "If you think you are too small to make a difference, try sleeping with a mosquito. -Ghandi",
        "There is no path to happiness. Happiness is the path. –Buddha"]
    angry_motivational_quotes = [
        "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured. - Mark Twain",
        "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
        "Holding onto anger is like drinking poison and expecting the other person to die. - Buddha",
        "Anger makes dull men witty, but it keeps them poor. -Elizabeth I"]
    
    # Define responses based on specific keywords or phrases
    if "sad" in user_input:
        quotes_for_sadness = random.choice(saddened_motivational_quotes)
        return f"I'm sorry to hear that, {user_name}! Your motivational quote is: {quotes_for_sadness}.  How else are you feeling?"
    elif "angry" in user_input:
        quotes_for_anger = random.choice(angry_motivational_quotes)
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: {quotes_for_anger}.  How else are you feeling?"
    elif "unhappy" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: There is no path to happiness. Happiness is the path. –Buddha.  How else are you feeling?"
    elif "annoyed" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Everything that irritates us about others can lead us to an understanding of ourselves. – Carl Jung.  How else are you feeling?"
    elif "frustrated" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Good decisions come from experience. Experience comes from making bad decisions. – Mark Twain  How else are you feeling?"
    elif "lonely" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Feeling sorry for yourself, and your present condition, is not only a waste of energy but the worst habit you could possibly have. – Dale Carnegie  How else are you feeling?"
    elif "stressed" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: The greatest weapon against stress is our ability to choose one thought over another. – William James  How else are you feeling?"
    elif "tired" in user_input:
        return f"I'm sorry to hear that, {user_name}!  Your motivational quote is: Rest when you're weary. Refresh and renew yourself, your body, your mind, your spirit. Then get back to work. - Ralph Marston  How else are you feeling?"
    elif "happy" in user_input:
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is: Happiness is not something ready made. It comes from your own actions. - Dalai Lama  How else are you feeling?"
    elif "excited" in user_input:
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is: Excitement is the fuel for achievement. Embrace it and let it drive you towards success!  How else are you feeling?"
    elif "motivated" in user_input:
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is: Keep pushing yourself because no one else is going to do it for you. How else are you feeling?"
    elif "inspired" in user_input:
        return f"I'm glad to hear that, {user_name}!  Your motivational quote is: The only way to do great work is to love what you do. - Steve Jobs  How else are you feeling?"
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
    print("Hello! Welcome to the simple Python chatbot!")
    
    user_name = input("What's your name? ")
    greeting = get_greeting()
    
    print(f"{greeting}, {user_name}!  I'm here to motivate you.  How are you feeling today? I have quotes for the  following moods or feelings: \nsad, angry, unhappy, annoyed, frustrated, lonely, stressed, tired, happy, excited, motivated, inspired.")
    print("Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "goodbye"]:
            print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
            break
        response = get_response(user_input, user_name)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    main()