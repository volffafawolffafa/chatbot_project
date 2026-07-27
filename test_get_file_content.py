from functions.get_file_content import get_file_content

from functions.get_file_content import get_file_content

def test_suite():
    # Test 1: Truncation Check on lorem.txt
    print("--- Test 1: Truncation Check ---")
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}\n")

    # Test 2: Read main.py
    print("--- Test 2: get_file_content('calculator', 'main.py') ---")
    print(get_file_content("calculator", "main.py"))
    print()

    # Test 3: Read pkg/calculator.py
    print("--- Test 3: get_file_content('calculator', 'pkg/calculator.py') ---")
    print(get_file_content("calculator", "pkg/calculator.py"))
    print()

    # Test 4: Traversal / Environment Escape
    print("--- Test 4: get_file_content('calculator', '/bin/cat') ---")
    print(get_file_content("calculator", "/bin/cat"))
    print()

    # Test 5: Missing File Target
    print("--- Test 5: get_file_content('calculator', 'pkg/does_not_exist.py') ---")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))
    print()

if __name__ == "__main__":
    test_suite()