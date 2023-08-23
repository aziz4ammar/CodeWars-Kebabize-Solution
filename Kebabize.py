def kebabize(s):
    result = []
    for char in s:
        if char.isalpha():
            if char.isupper():
                result.append('-' + char.lower())
            else:
                result.append(char)
    return ''.join(result).lstrip('-')

# Example usage
input_string = "myCamelCasedString"
kebabized_string = kebabize(input_string)
print(kebabized_string)  # Output: "my-camel-cased-string"