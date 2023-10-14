"""
Chooses meals for the week from a list
"""


import argparse
import pandas as pd


def parse_args() -> argparse.Namespace:
    """
    Parse the command line arguments inputs given

    Returns
    -------
    args : Namespace
        Namespace of passed command line argument inputs
    """

    parser = argparse.ArgumentParser(
        description='Feed me a file of meals and I\'ll spit out some choices'
    )

    # Add CLI arg of the input annotated VCF to have filtering flags added
    parser.add_argument(
        '-m',
        '--meals_file',
        type=str,
        required=True,
        help='File containing meal ideas. CSV format with columns MEAL, VEGGIE, SOURCE, TIME'
    )

    args = parser.parse_args()

    return args


def validate_input(meal_file):
    # check input is CSV and contains correct columns (in correct formats)
    # raise exception if not good
    pass


def parse_input(meal_file):
    # validate the file
    validate_input(meal_file)
    # turn it into a dataframe
    meal_df = pd.read_csv(meal_file)
    # return that dataframe
    return meal_df


def choose_meals(meal_df):
    # take df, randomly choose 7 meals (2 veggie)
    veg = meal_df[meal_df['VEGGIE'] == "yes"].sample(n=2)
    meaty = meal_df[meal_df['VEGGIE'] == "no"].sample(n=5)
    # return meal name, difficulty, time
    return pd.concat([veg, meaty])


def main():
    args = parse_args()
    meal_df = parse_input(args.meals_file)
    choices = choose_meals(meal_df)
    print(choices)


if __name__ == "__main__":
    main()