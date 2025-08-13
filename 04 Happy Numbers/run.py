def is_happy(n: int) -> bool:
     
    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1

print(is_happy(2))

if __name__ == "__main__":
    assert is_happy(19), 'Test Case 1 Failed'
    assert not is_happy(2), 'Test Case 2 Failed'
    assert is_happy(44), 'Test Case 3 Failed'
    assert is_happy(86), 'Test Case 4 Failed'
    assert is_happy(139), 'Test Case 5 Failed'

    print('All test cases pass')
