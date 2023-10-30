# Given sets of words
sequences = [
    {'1', '8', '5', '3', '4', '0', '2', '9', '7', '6'},
    {'October', 'January', 'August', 'February', 'June', 'July', 'November', 'December', 'May', 'March', 'April', 'September'},
    {'Sunday', 'Tuesday', 'Saturday', 'Thursday', 'Wednesday', 'Monday', 'Friday'},
    {'qwerty', 'zxcv', 'asdf'},
    {'ana', 'bob'},
    {'?', '!', '.'}
]

# Function to check if two passwords have common words from the same list
def have_common_words_from_list(password1, password2):
    modified_password1 = password1
    modified_password2 = password2
    for seq in sequences:
        count = 0
        for word in seq:
            if word in password1:
                modified_password1 = password1.replace(word, "")
                count += 1
            elif word in password2:
                modified_password2 = password2.replace(word, "")
                count += 1
            if count == 2:
                return True, modified_password1, modified_password2
    return False, modified_password1, modified_password2

# Example usage
password1 = input("Enter the first password: ")  # Split the input into words
password2 = input("Enter the second password: ")  # Split the input into words

result,pass1,pass2 = have_common_words_from_list(password1, password2)
print(pass1,pass2)

if result:
    print("The passwords contain words from the same list.")
else:
    print("The passwords do not contain words from the same list.")
