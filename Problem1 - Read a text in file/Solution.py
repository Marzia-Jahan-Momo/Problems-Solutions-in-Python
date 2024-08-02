def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError():
        print(f"{file_path} was not find")
        
        
read_file('example.txt')