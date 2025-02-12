def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
    new_file = file_contents.lower()
    letters_dict = {}
    word_count = file_contents.split()
    for character in new_file:
        if character not in letters_dict:
            letters_dict[character] = 1
            
        elif character in letters_dict:
            letters_dict[character] += 1

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{len(word_count)} words found in the document')
    for letter in alphabet:
        print (f"The '{letter}' character was found {letters_dict[letter]} times")
    print('--- End report ---')

main()