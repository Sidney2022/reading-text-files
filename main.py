# Read text from a file, and count the occurrence of words in that text

def read_file_content(filename):
    f = open(filename, 'r')
    read_file = f.read()

    return read_file


def count_words():
    try:
        file = read_file_content('story.txt')
        words = file.split(' ')
        word_counts = {}
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return word_counts

    except FileNotFoundError:
        print('file or file path does not exist')


print(count_words())
