words=["evolution","temporary","voluntary","execute"]
length = 0;
for word in words:
    if len(word) > length:
        length = len(word)
        largest = word
print("here the largest word is",largest,"with ",len(largest),"characters")