def increment_array_map(arr, inc):
    return list(map(lambda x: x + inc, arr))

def main():
    line = input("Enter integers (space-separated): ")
    original = list(map(int, line.split()))
    
    inc_line = input("Enter increment: ")
    increment = int(inc_line)

    new_array = increment_array_map(original, increment)

    print("Original array:", original)
    print("Increment:", increment)
    print("New array:", new_array)

main()



