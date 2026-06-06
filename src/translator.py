from model import translate_text

text = input("Enter English text: ")

result = translate_text(text)

print("\nTamil Translation:")
print(result)