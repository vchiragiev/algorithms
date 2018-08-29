
def print_range_without_loop(n):
    if n > 0:
        print_range_without_loop(n-1)
        print(n)

if __name__ == "__main__":
    print_range_without_loop(10)