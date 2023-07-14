text = "This is a sample text with spaces"
replacement = ":"

# Find the index of the second space
index = text.find(" ", text.find(" ") + 1)

# Replace the second space with colon
new_text = text[:index] + replacement + text[index+1:]

print(new_text)