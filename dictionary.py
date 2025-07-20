"""
Project: 
    Spell Checker with Suggestion Logging
Author: 
    Rithvik Burri
Description:
    This interactive Python application performs spell checking by connecting to a MySQL
    dictionary database. When users enter a sentence, the program identifies misspelled
    or unrecognized words and provides intelligent correction suggestions based on similar
    matches in the database. Users can select from suggested corrections or skip words
    entirely, with all chosen corrections logged alongside timestamps for future analysis
    and reference.
Purpose:
    This project demonstrates practical database integration, string matching algorithms,
    and interactive user interface design in Python. By tracking user correction patterns
    through timestamped logs, the application creates valuable analytical data for
    understanding common spelling errors and continuously improving suggestion accuracy.
    The tool serves as both a functional spell checker and a learning platform for
    database-driven application development.
"""
import mysql.connector               # For connecting to the MySQL database
import difflib                       # For finding similar word matches
import string                        # For handling punctuation
from datetime import datetime        # For logging the current timestamp

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="192.168.4.41",
    user="Rithv",
    password="Rookie@123",
    database="dictionary",
    autocommit=True                  # Automatically saves changes (no need to call commit)
)

# Check if the connection was successful
if conn.is_connected():
    cursor = conn.cursor()

    # Fetch all valid words from the dictionary table
    cursor.execute("SELECT LOWER(TRIM(word)) FROM words_backup")
    dictionary_words = [row[0] for row in cursor.fetchall()]

    # Ask the user to enter a sentence
    user_input = input("Enter a sentence: ")
    corrected_sentence = []  # Store the corrected sentence as a list of words

    # Process each word in the input sentence
    for token in user_input.split():
        # Clean the word: remove punctuation and make it lowercase
        word = token.strip(string.punctuation).lower()
        
        # Extract any punctuation before and after the word
        prefix = token[:len(token) - len(token.lstrip(string.punctuation))]
        suffix = token[len(token.rstrip(string.punctuation)):]

        # Check if the word exists in the dictionary
        cursor.execute("SELECT EXISTS(SELECT 1 FROM words_backup WHERE LOWER(TRIM(word)) = %s)", (word,))
        if cursor.fetchone()[0]:
            # Word is valid, add it back to the sentence with original punctuation
            corrected_sentence.append(prefix + word + suffix)
        else:
            # Word is not found, try to find similar suggestions
            suggestions = difflib.get_close_matches(word, dictionary_words, n=3, cutoff=0.7)
            if suggestions:
                # Show suggestions to the user
                print(f"\n❌ '{word}' not found. Suggestions:")
                for i, s in enumerate(suggestions, 1):
                    ratio = round(difflib.SequenceMatcher(None, word, s).ratio() * 100)
                    print(f"  {i}. {s} (Similarity: {ratio}%)")

                # Let the user choose a suggestion
                choice = input("Pick 1/2/3 or press Enter to skip: ").strip()
                
                if choice in ['1', '2', '3'] and int(choice) <= len(suggestions):
                    corrected = suggestions[int(choice)-1]
                    corrected_sentence.append(prefix + corrected + suffix)

                    # Log the correction in the database
                    cursor.execute(
                        "INSERT INTO correction_log (word_entered, suggestion_chosen, timestamp) VALUES (%s, %s, %s)",
                        (word, corrected, datetime.now())
                    )
                else:
                    # User skipped correction
                    corrected_sentence.append(token)
            else:
                # No suggestions found, keep the original word
                corrected_sentence.append(token)

    # Display the final corrected sentence
    print("\n✅ Corrected Sentence:")
    print(" ".join(corrected_sentence))

    # Close the cursor
    cursor.close()

# Close the database connection
conn.close()
