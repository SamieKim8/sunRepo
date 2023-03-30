# Name: Sunmi Kim
# Date: 03/19/2023
# Title: NLP Sentiment Analysis using NLTK and OpenCV

import cv2
from colorama import Fore
import nltk
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

sentiment_img = [
"""
    |    O  (ㅠ ㅠ)
    |   /|\\
    |    |
    |   / \\
""",
"""
    |    O  (o  o)
    |  --|--
    |    |
    |   / \\
""",
"""
    |    O  (^  ^)
    |   \|/
    |    |
    |   / \\
"""
]

# display title of the app
def display_title():
    print(Fore.RED + "=====*=====*=====*=====*=====*=====*=====*=====")
    print(Fore.GREEN + "======== Sentiment Analysis Application =======")
    print(Fore.BLUE + "=====*=====*=====*=====*=====*=====*=====*=====")
    print()
    #print(Fore.WHITE + f"{sentiment_img[2]} {sentiment_img[1]} {sentiment_img[0]}")

# define a function to analyze sentiment
def get_sentiment(text):
    # use the polarity_scores() method to get a sentiment score
    score = sia.polarity_scores(text)
    # extract the emotion score, which ranges from -1 to 1
    emotion_score = score['compound']
    # classify the sentiment as positive, negative, or neutral
    if emotion_score > 0.05:
        sentiment = 'Positive'
        print(sentiment_img[2])
    elif emotion_score < -0.05:
        sentiment = 'Negative'
        print(sentiment_img[0])
    else:
        sentiment = 'Neutral'
        print(sentiment_img[1])
    # return the sentiment and the emotion score
    return sentiment, emotion_score

# get user input to test sentiment analysis 
def get_user_input():
    text = input(Fore.WHITE + "Write a sentence. How do you feel now? ") 
    sentiment, score = get_sentiment(text)
    print('What you wrote:', text)
    print('Sentiment:', sentiment)
    print('Emotion Score:', score)
    print()

def main():
    print()
    display_title()
    # image display using openCV module
    img = cv2.imread("sentiment_images.JPG", cv2.IMREAD_COLOR)
    cv2.imshow("Emotions", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    answer = input(Fore.WHITE + "Would you like to check your emotion? (y/n)\n")
    
    while answer.lower() == "y":
        get_user_input()
        answer = input(Fore.WHITE + "Would you like to check your emotion? (y/n)\n")
    else:
        print("Have a nice day!")
        
    print()

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
