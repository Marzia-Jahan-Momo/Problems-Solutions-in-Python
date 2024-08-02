# Problem1 - Read a text in file

## Write a Python script to read a text file and print its contents line by line.

# Solution 1 - Read a text in file
```python 
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError():
        print(f"{file_path} was not find")
        
        
read_file('example.txt')
```
