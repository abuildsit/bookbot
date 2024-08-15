booksLocation = "books/"
book1Filename = "frankenstein.txt"


def count_words(contents):
    words = contents.split()
    wordCount = len(words)
    return wordCount

def count_characters(contents):
    charCount = {chr(i): 0 for i in range(97, 123)}
    # contents = contents.lower()
    
    for char in contents.lower():
        if 'a' <= char <= 'z':
            charCount[char] += 1
    
    return charCount
    

def main():
    with open(f"{booksLocation}{book1Filename}") as f:
        file_contents = f.read()

    wordCount = count_words(file_contents)
    print(f"Book contains {wordCount} words")
    
    charCount = count_characters(file_contents)
    
    print(f"Character Counts are:\n{charCount}")
    return


main()