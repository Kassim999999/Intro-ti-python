num1, num2 = 200, 123

if num1 < num2:
    print(f"Sure ${num1} is less than ${num2}")
elif (num1 == num2):
    print(f"Sure ${num1} is equal to ${num2}")
else:
    print(f"Sure ${num1} is greater than ${num2}")

    sentence = "This is a sample sentence to check words."

    if "have" in sentence:
        print("The word 'have' is in the sentence")

    if "monumental" not in sentence:
        print("The word 'monumental' is not in the sentence")

    if len(sentence) > 10:
        print("This is a very long sentence")

        print("This is an extremely long sentence ") if len (sentence)> 10 else print("Goddamn!")