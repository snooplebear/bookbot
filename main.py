def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()

    word_count = count_words(file_contents)

    print(f'--- Begin report of {path_to_file} ---')
    print(f'{word_count} words found in the document')
    print('')

    results = count_letters(file_contents)
    for letter, count in results:
        print(f'The \'{letter}\' character was found {count} times')

    print('--- End report ---')

def count_words(file_contents):
    word_count = len(file_contents.split())
    return word_count

def sort_dict_on(count_letter_dict):
    return count_letter_dict["num"]

def count_letters(file_contents):
    count_letter_dict = {}
    file_contents_lowercase = file_contents.lower()

    for letter in file_contents_lowercase:
        if letter.isalpha():
            if letter not in count_letter_dict:
                count_letter_dict[letter] = 1
            else:
                count_letter_dict[letter] += 1
    
    # Sort dictionary by occurrence
    # count_letter_dict.sort(reverse=True, key=sort_dict_on)
    count_letter_list = list(count_letter_dict.items())
    count_letter_list.sort(reverse=True, key=lambda item: item[1])
    # print(count_letter_list)
    
    return count_letter_list
        
    

main()