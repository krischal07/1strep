import streamlit as st
import random

# List of amazing quotes
amazing_quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Your time is limited, don't waste it living someone else's life. – Steve Jobs",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt"
]

def get_random_quote():
    return random.choice(amazing_quotes)

def main():
    st.title("Glam Your Day")
    st.write("Every time you refresh the page, a new amazing quote will appear!")
    quote = get_random_quote()
    st.write(quote)

if __name__ == "__main__":
    main()
