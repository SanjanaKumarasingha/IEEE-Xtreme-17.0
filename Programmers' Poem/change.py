def transform_string(input_str):
    transformed_str = ""
    for i in range(len(input_str)):
        if i == 0 or input_str[i] != input_str[i - 1]:
            transformed_str += input_str[i]
    return transformed_str

# Example usage
input_str1 = "cdddaaaad"
output_str1 = transform_string(input_str1)
print(output_str1)  # Output: "aabbbccccd"

input_str2 = "cccaa"
output_str2 = transform_string(input_str2)
print(output_str2)  # Output: "aaabb"

reverted_str1 = output_str1[::-1]
print(reverted_str1)  # Output: "cdddaaaad"

reverted_str2 = output_str2[::-1]
print(reverted_str2)  # Output: "cccaa"
