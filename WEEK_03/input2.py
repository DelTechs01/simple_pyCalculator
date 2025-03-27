with open("input2.text", "w") as file:
    file.write(" Hello this is a sample text file.\n")
    file.write("Python is an amazing language.\n")
    file.write("File handling in python is simple and powerful.\n")
    file.write("Python is a high-level language.\n")
    file.write("Python is an interpreted language.\n")

with open("input2.text", "r") as file:
    content = file.readlines()

    processed_content = [line.upper() for line in content]
    word_count = sum([len(line.split()) for line in content])

    with open("output2.text", "w") as file:
        file.write("processed_content")
        file.write("word_count")