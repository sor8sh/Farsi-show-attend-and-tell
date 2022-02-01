import json

english_dict = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def has_english_word(caption):
    caption = caption.replace("'\n'", "")
    check1 = caption.upper() == caption
    check2 = caption.lower() == caption
    if check1 and check2:
        return False
    return True


def find_english_word(caption):
    caption = caption.replace("'\n'", "")
    found = []

    c1 = caption.upper()
    cap1 = c1.split(' ')

    c2 = caption.lower()
    cap2 = c2.split(' ')

    for i in range(len(cap1)):
        if cap1[i] != cap2[i]:
            found.append(cap2[i])
    return found


# Train
# Read Farsi captions
with open('./captions/captions_train2014_farsi.txt', mode='r') as f:
    translation = []
    for i in range(414113):
        translation.append(f.readline())

# Replace english captions with Farsi
with open('./captions/captions_train2014.json', mode='r') as f:
    coco = json.load(f)
    counter = 0
    wrong_captions = []
    for item in coco['annotations']:
        if has_english_word(translation[counter]) or "*" in translation[counter]:
            wrong_captions.append(item['id'])
        item['caption'] = translation[counter]
        counter += 1

# Write new JSON file with Farsi captions
with open('./captions/captions_train2014_farsi.json', mode='w') as f:
    json.dump(coco, f)

print("Training set wrong caption (including english words or *):")
print(wrong_captions)

# Validation
# Read Farsi captions
with open('./captions/captions_val2014_farsi.txt', mode='r') as f:
    translation = []
    for i in range(202654):
        translation.append(f.readline())

# Replace english captions with Farsi
with open('./captions/captions_val2014.json', mode='r') as f:
    coco = json.load(f)
    counter = 0
    wrong_captions = []
    for item in coco['annotations']:
        if has_english_word(translation[counter]) or "*" in translation[counter]:
            wrong_captions.append(item['id'])
        item['caption'] = translation[counter]
        counter += 1

# Write new JSON file with Farsi captions
with open('./captions/captions_val2014_farsi.json', mode='w') as f:
    json.dump(coco, f)

print("Validation set wrong caption (including english words or *):")
print(wrong_captions)
