from lib.word2number import w2n

next_text = "next"

number_text = "Number"


def sort_parsed_text(unordered_text):
    ordered_text = []
    n = len(unordered_text)
    for i in range(n):
        number, text = unordered_text[i]
        if number != -1 and number < len(ordered_text):
            ordered_text.insert(i, [number, text])
            ordered_text.pop(i + 1)
        else:
            ordered_text.append([number, text])
    return ordered_text


def convert_text_to_int(text):
    # Converts number text to integer
    if text == next_text:
        return -1
    return w2n.word_to_num(text)


def extract_number_and_index(text):
    # Extracts integer value and index of "Number n"
    idx = 8
    number_in_text = text.split(' ')[1]
    while idx < len(text) and text[idx] != ' ':
        idx += 1
    if number_in_text == next_text:
        return -1, idx
    return convert_text_to_int(number_in_text.strip()), idx


class TextParser:
    def __init__(self, text):
        self.text = text
        self.header = ''

    def find_delimiters_in_text(self):
        # Finds the delimiters in text
        number_indices = []
        idx = 0
        while idx < len(self.text):
            found_at_index = self.text.find(number_text, idx)
            if found_at_index == -1:
                break
            else:
                idx = found_at_index + 7
                number_indices.append(found_at_index)
        return number_indices

    def parse_text(self):
        # Returns if the text contains the "Number" delimiter and the split up text
        indices = self.find_delimiters_in_text()
        parsed_text = []
        if not indices:
            if self.text:
                self.header = self.text
            return self.text, False
        if indices[0] != 0:
            self.header = self.text[:indices[0]]
        if len(indices) == 1:
            if indices[0] == 0:
                return [self.text], True
            return [self.text[:indices[0]], self.text[indices[0]:]], True
        for i in range(len(indices) - 1):
            parsed_text.append(self.text[indices[i]:indices[i + 1]])
        parsed_text.append(self.text[indices[-1]:])
        return parsed_text, True

    def generate_transcription(self):
        # Generates transcription by extracting "Number n" and "Number next"
        parsed_text, contains_delimiters = self.parse_text()
        if not contains_delimiters:
            return ''
        transcription = []
        for i in range(len(parsed_text)):
            number, idx = extract_number_and_index(parsed_text[i].strip())
            transcription.append([number, parsed_text[i][idx:].strip()])
        ordered_transcription = sort_parsed_text(transcription)
        return ordered_transcription

    def print_transcription(self):
        # Prints transcription in desired format
        transcription = self.generate_transcription()
        if not transcription and not self.header:
            print("ERROR: Empty string")
        transcribed_text = ''
        if self.header:
            print(self.header)
            transcribed_text += self.header.strip()
        if transcription:
            for idx in range(len(transcription)):
                text = transcription[idx][1][0].upper() + transcription[idx][1][1:]
                numbered_text = str(idx + 1) + '. ' + text
                transcribed_text += ' ' + numbered_text.strip()
                print(numbered_text.strip())
        return transcribed_text
