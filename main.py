from encryption import encryption

if __name__ == "__main__":
    massage1 = input("Enter a massage")
    enc = encryption(massage1)

    with open("encrypt.txt", "w") as f:
        f.write(enc)

    with open("encrypt.txt", "r") as f:
        print(f.read())

    with open("encrypt.txt", "r") as f:
        print(encryption(f.read()))


    story_1 = ""
    story_2 = ""
    with open("story.txt","r") as f:
        counter = 0
        for line in f:
            if counter % 2 == 0:
                story_1 += line
                counter += 1
            elif counter % 2 != 0:
                story_2 += line
                counter +=1

    with open("story1.txt","w") as f:
        f.write(story_1)

    with open("story2.txt","w") as f:
        f.write(story_2)


    with open("story1.txt","r")as f:
        print("story 1:\n ",f.read())

    with open("story2.txt","r")as f:
        print("story 2:\n ",f.read())