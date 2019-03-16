def unpacking_experiment(*args):
    first_argument = args[0]
    second_argument = args[1]
    other_arguments = args[2:]
    print(first_argument)
    print(second_argument)
    print(other_arguments)

unpacking_experiment(1, 2, 3, 4, 5, 6)
# 1 2 (3, 4, 5, 6)

def unpacking_experiment(**kwargs):
    print(kwargs)

unpacking_experiment(named = "Test", other = "Other")
# {'named': 'Test', 'other': 'Other'}
