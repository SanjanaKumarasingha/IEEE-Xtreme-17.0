def main():
    n, m = map(int, input().split())
    rhyme_dict = {}
    
    # Read rhyming groups and create the dictionary
    for _ in range(n):
        words = input().strip().split()
        rhyme_label = chr(65 + len(rhyme_dict))
        for word in words:
            rhyme_dict[word] = rhyme_label

    # Read and analyze the passage to construct the rhyme scheme
    rhyme_scheme = ''
    for _ in range(m):
        line = input().strip().split()
        line_rhyme_labels = set(rhyme_dict.get(word.lower(), 'X') for word in line)
        rhyme_scheme += ''.join(line_rhyme_labels)

    # Output the rhyme scheme
    print(rhyme_scheme)

if __name__ == "__main__":
    main()
