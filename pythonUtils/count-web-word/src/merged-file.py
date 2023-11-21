import os
def merge_word_frequencies(file1, file2):
    # Read word frequencies from file1
    with open(file1, 'r', encoding='utf-8') as f1:
        word_freq1 = {}
        for line in f1:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            parts = line.split(': ')
            if len(parts) != 2:
                print(f'Invalid line in {file1}: {line}')
                continue
            word, freq = parts
            word_freq1[word] = int(freq)

    # Read word frequencies from file2 and update word_freq1
    with open(file2, 'r', encoding='utf-8') as f2:
        for line in f2:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            parts = line.split(': ')
            if len(parts) != 2:
                print(f'Invalid line in {file2}: {line}')
                continue
            word, freq = parts
            if word in word_freq1:
                word_freq1[word] += int(freq)
            else:
                word_freq1[word] = int(freq)

    # Sort word frequencies in descending order
    sorted_word_freq = sorted(word_freq1.items(), key=lambda x: x[1], reverse=True)

    # Write merged word frequencies to a new file
    merged_file = resource_directory + '/merged_word_frequencies.txt'
    with open(merged_file, 'w', encoding='utf-8') as output:
        for word, freq in sorted_word_freq:
            output.write(f'{word}: {freq}\n')

    print(f'Merged word frequencies have been written to {merged_file}.')

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    resource_directory = os.path.join(current_directory, '..', 'resource')
    file1 = resource_directory + '/api-word_frequencies.txt'
    file2 = resource_directory + '/step-word_frequencies.txt'
    print(file1)
    print(file2)
    merge_word_frequencies(file1, file2)