def add_numbers(a, b):
    return a + b


def test_add_numbers():
    test_cases = [
        (2, 3, 5),
        (-2, 3, 1),
        (0, 0, 0),
        (5, -5, 0),
    ]

    i = 0
    while i < 4:
        test_case = test_cases[i]
        a = test_case[0]
        b = test_case[1]
        expected_result = test_case[2]
        result = add_numbers(a, b)

        if result != expected_result:
            print("Test case", i + 1, "failed:", a, "+", b, "=", result, "expected", expected_result)

        i += 1