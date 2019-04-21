import Image
image = Image.open("correct.jpg")
eng = ["same", "to give up", "alarm clock"]
jap = ["onaji", "akirameru", "mezamashidokei"]
i=0
while i< len(eng):
    print("Translate this into Japanese: " + eng[i])
    answer = input("Your answer: ")
    if jap[i] == answer:
        print("correct")
        image.show
    else:
        print("No, you dumb fuck, it's " + jap[i])

    i = i+1
