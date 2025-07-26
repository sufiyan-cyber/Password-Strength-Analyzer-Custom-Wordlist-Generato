import zxcvbn
import itertools
from datetime import datetime

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Part 1: Password Strength Analyzer
# This part of the script analyzes the strength of a user-provided password.
# It uses the zxcvbn library as recommended by the project tools.
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
def analyze_password_strength():
    """
    Analyzes the strength of a password provided by the user and prints the results.
    """
    password = input("\nEnter a password to analyze its strength: ")
    if not password:
        print("Password cannot be empty.")
        return

    # Use zxcvbn to analyze the password [cite: 64]
    results = zxcvbn.zxcvbn(password)
    score = results.get('score')
    feedback = results.get('feedback', {})
    suggestions = feedback.get('suggestions', [])
    warning = feedback.get('warning', '')

    print("\n--- Password Strength Analysis ---")
    print(f"Password: {'*' * len(password)}")
    print(f"Estimated time to crack (offline, fast hash): {results.get('crack_times_display', {}).get('offline_fast_hashing_1e10_per_second', 'N/A')}")
    print(f"Strength Score: {score}/4")

    if warning:
        print(f"Warning: {warning}")

    if suggestions:
        print("Suggestions for improvement:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    print("--------------------------------\n")


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Part 2: Custom Wordlist Generator
# This part generates a custom wordlist based on personal inputs,
# applies common mutations, and saves it to a file.
# It includes features like leetspeak and adding years[cite: 66].
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
def generate_custom_wordlist():
    """
    Generates a custom wordlist from user inputs and saves it to a file.
    """
    print("--- Custom Wordlist Generator ---")
    print("Enter some personal details to generate a wordlist. Press Enter to skip any field.")

    # Allow user inputs like name, date, and pet's name to generate the wordlist [cite: 65]
    name = input("Enter a first name (e.g., John): ").strip().lower()
    surname = input("Enter a surname (e.g., Doe): ").strip().lower()
    nickname = input("Enter a nickname: ").strip().lower()
    dob_str = input("Enter a date of birth (YYYY-MM-DD): ").strip()
    pet_name = input("Enter a pet's name: ").strip().lower()
    city = input("Enter a city: ").strip().lower()

    base_words = set(filter(None, [name, surname, nickname, pet_name, city]))

    # Extract year, month, day from DOB
    if dob_str:
        try:
            dob = datetime.strptime(dob_str, '%Y-%m-%d')
            base_words.add(str(dob.year))
            base_words.add(f"{dob.day:02d}")
            base_words.add(f"{dob.month:02d}")
            base_words.add(f"{dob.day:02d}{dob.month:02d}")
            base_words.add(f"{dob.month:02d}{dob.day:02d}")
        except ValueError:
            print("Invalid date format. Skipping date-based words.")

    if not base_words:
        print("\nNo base words provided. Cannot generate a wordlist.")
        return

    print(f"\nBase words collected: {', '.join(base_words)}")

    # Generate variations
    final_wordlist = set()
    leetspeak_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}

    for word in list(base_words):
        # 1. Add original word and capitalized version
        final_wordlist.add(word)
        final_wordlist.add(word.capitalize())

        # 2. Add leetspeak variations [cite: 66]
        leet_word = "".join([leetspeak_map.get(char, char) for char in word])
        if leet_word != word:
            final_wordlist.add(leet_word)
            final_wordlist.add(leet_word.capitalize())

    # 3. Add combinations of base words
    if len(base_words) > 1:
        for r in range(2, min(len(base_words) + 1, 4)): # Combinations of 2 and 3 words
            for combo_tuple in itertools.permutations(base_words, r):
                final_wordlist.add("".join(combo_tuple))
                final_wordlist.add("_".join(combo_tuple))

    # 4. Append years and special characters [cite: 66]
    current_year = datetime.now().year
    years_to_add = [str(y) for y in range(current_year - 5, current_year + 1)]
    spec_chars = ['!', '@', '#', '$', '%']

    # Use a temporary list to avoid changing set while iterating
    words_to_expand = list(final_wordlist)
    for word in words_to_expand:
        for year in years_to_add:
            final_wordlist.add(word + year)
        for char in spec_chars:
            final_wordlist.add(word + char)

    # 5. Export to .txt format [cite: 67]
    filename = "custom_wordlist.txt"
    with open(filename, 'w') as f:
        for word in sorted(list(final_wordlist)):
            f.write(word + "\n")

    print(f"\nSuccessfully generated {len(final_wordlist)} unique passwords.")
    print(f"Wordlist saved to '{filename}' [cite: 67]")
    print("---------------------------------\n")


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
# Main Menu
#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
def main():
    """
    Main function to display the menu and run the selected tool.
    """
    while True:
        print("===== Password Toolkit =====")
        print("1. Password Strength Analyzer")
        print("2. Custom Wordlist Generator")
        print("3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            analyze_password_strength()
        elif choice == '2':
            generate_custom_wordlist()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.\n")

if __name__ == "__main__":
    main()