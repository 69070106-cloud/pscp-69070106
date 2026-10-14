"""113"""
def remove(text):
    """remove 113"""
    while "113" in text:
        text = text.replace("113", "")
    return text
ANS = remove(input())
print(ANS)
