# Remove all the lines that contain the character "a" in file and write it to another file.

def main():
    with open("temp/input.txt", "r") as file:
        non = [i.strip() for i in file.readlines() if 'a' not in i]
    print(non)
    with open("temp/sample.txt", "w") as file, open("temp/input.txt", "w") as file2:
        for i in non:
            file2.writelines(f"{i}\n")
            file.writelines(f"{i}\n")  
    
main()