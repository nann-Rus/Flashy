"""
Flashcard Study Assistant | Stanford Code in Place final project

Students create custom word/meaning or question/answer pairs, reveal the
answers in study mode, and then type their answers in a quiz. Each round
reports the number correct and incorrect, a percentage, and any missed
prompts. If the student retries, they review the missed cards first and
then answer the entire deck again. A perfect round completes the session.

Run with Python 3: python3 flashcard_study_assistant.py
Or paste this entire file into a Python editor and run it.

Demo deck: كتاب = Book, جامعة = University, قلم = Pen,
مدرسة = School, طالب = Student.
Swap University and School in round 1 to score 3/5 (60.00%).
Review those two cards, then answer all five correctly for 5/5 (100.00%).

The dictionary holds one deck for the current run. Re-entering a prompt
updates its meaning. Grading ignores capitalization and surrounding
spaces but requires the stored wording. Future versions could save decks,
support alternative answers and multiple subjects, or add a graphical UI.
"""


def create_flashcards(flashcards):
    print("\n--- CREATE FLASHCARDS ---")
    print("Type 'done' when you finish adding words.")

    while True:
        word = input("\nEnter a word: ").strip()

        if word.lower() == "done":
            break

        if word == "":
            print("Please enter a word.")
            continue

        meaning = input("Enter its meaning: ").strip()

        while meaning == "":
            print("Please enter a meaning.")
            meaning = input("Enter its meaning: ").strip()

        flashcards[word] = meaning
        print("Flashcard added successfully!")

    print("Total flashcards:", len(flashcards))


def reveal_cards(words, flashcards):
    for word in words:
        print("\nWord:", word)
        input("Press Enter to reveal the meaning...")
        print("Meaning:", flashcards[word])


def study_flashcards(flashcards):
    if len(flashcards) == 0:
        print("Please create flashcards first.")
        return

    print("\n--- STUDY MODE ---")

    reveal_cards(flashcards, flashcards)

    print("\nYou have reviewed all your flashcards!")


def test_flashcards(flashcards):
    if len(flashcards) == 0:
        print("Please create flashcards first.")
        return

    round_number = 1

    while True:
        correct = 0
        wrong_words = []

        print("\n--- TEST ROUND", round_number, "---")

        for word in flashcards:
            print("\nWord:", word)
            answer = input("What is its meaning? ")

            if answer.strip().lower() == flashcards[word].lower():
                print("Correct!")
                correct += 1

            else:
                print("Incorrect!")
                print("Correct answer:", flashcards[word])
                wrong_words.append(word)

        incorrect = len(wrong_words)
        total = len(flashcards)
        percentage = correct / total * 100

        print("\n========== RESULTS ==========")
        print("Test round:", round_number)
        print("Total questions:", total)
        print("Correct answers:", correct)
        print("Incorrect answers:", incorrect)
        print(f"Score: {percentage:.2f}%")

        if incorrect == 0:
            print("\nCongratulations!")
            print("You answered every flashcard correctly in this round!")
            break

        print("\nWords you need to review:")

        for word in wrong_words:
            print(word)

        choice = input("\nStudy and try again? (yes/no): ")

        if choice.strip().lower() != "yes":
            break

        print("\n--- REVIEW YOUR MISTAKES ---")

        reveal_cards(wrong_words, flashcards)

        round_number += 1


def main():
    flashcards = {}

    print("Welcome to Flashcard Study Assistant!")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Create flashcards")
        print("2. Study flashcards")
        print("3. Test yourself")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            create_flashcards(flashcards)

        elif choice == "2":
            study_flashcards(flashcards)

        elif choice == "3":
            test_flashcards(flashcards)

        elif choice == "4":
            print("Thank you for studying!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
