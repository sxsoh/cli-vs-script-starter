"""a variety of numerical operations based on the value of an option to the CLI"""



import typer

# create a Typer object to support the command-line interface
cli_object = typer.Typer()

def compute_one_by_addition() -> float:
    """Perform addition in a loop that is expected to add to 1.0"""
    number = 0.0
    for _ in range(10):
        number = number + 0.1
    return number

def compute_one_by_multiplication() -> float:
    """Perform a multiplication that is expected to be 1.0"""
    multiply_number = 10.0 * 0.1
    return multiply_number

def determine_even_odd(value: int) -> str:
    """Determine if a number is even or odd."""
    if value % 2 == 0:
        return "even"
    else:
        return "odd"

@cli_object.command()
def cli(
    option: str = typer.Option(0),
) -> None:
    """Perform one of a variety of numerical operations based on the value of the option."""

    print("~ ~ ~ ~ ~ ~ ~ ~ ~")
    print(f"✨ The value of the cli option is {option}")
    print()
    print(f"✨ I will now being running {option}")

    if option == "floating_point_operations":

        # call compute_one_by_addition and one_by_multiplication and assign the return value into variables
        one_by_addition = compute_one_by_addition()
        one_by_multiplication = compute_one_by_multiplication()

        print(f"Calculating 'one' by addition is {one_by_addition}")
        print(f"Calculating 'one' by multiplication is {one_by_multiplication}")
        print()
        print(f"✨ That doesn't seem right, but it is!")

    elif option == "even_odd_checks":


        number = 0
        response = determine_even_odd(number)
        print(f"The number of {number} is {response}!")


        number = 10
        response = determine_even_odd(number)
        print(f"The number of {number} is {response}!")


        number = 11
        response = determine_even_odd(number)
        print(f"The number of {number} is {response}!")


        number = -10
        response = determine_even_odd(number)
        print(f"The number of {number} is {response}!")


        number = -11
        response = determine_even_odd(number)
        print(f"The number of {number} is {response}!")

    else:
        print(f"I don't know how to run {option}, sorry!")

    print("~ ~ ~ ~ ~ ~ ~ ~ ~")



