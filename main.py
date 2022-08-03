import subprocess
from service.parse_text import TextParser

# Add test cases below in the test_cases array

test_cases = [
    "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit. Number "
    "next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a "
    "persistent cough that hasn’t improved for last 4 weeks. ",
    "Number one stuff stuff stuff",
    "Patient presents today with several issues.",
    ''
]

if __name__ == '__main__':
    for test in range(len(test_cases)):
        text_parser = TextParser(test_cases[test])
        print("________________________________")
        print("TEST CASE #" + str(test + 1))
        print("Input:")
        print(test_cases[test])
        print("\nOutput: ")
        text_parser.print_transcription()
