words = ["abc","car","ada","racecar","cool"]
new_word=[]
for i in words:
    new_word = i[::-1]
    if new_word==i:
        print(f"{i} is a Palindrome")
        break
    else:
        new_word = ""