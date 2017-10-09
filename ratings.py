"""Restaurant rating lister."""

import random

# put your code here
def get_rest_ratings(filename):
    """ Creates dictionary of restaurants and their related ratings. """

    with open(filename) as rest_file:

        rest_ratings = {}

        for line in rest_file:
            line = line.rstrip()
            restaurant, rating = line.split(":")
            # restaurants = line.split(":")

            # restaurant = restaurants[0]
            # rating = restaurants[1]

            rest_ratings[restaurant] = rating

    return rest_ratings


# def sort_rest_ratings(dictionary):
#     """ Sort restaurants and respective ratings in alphabetical order. """

#     alpha_rest = sorted(dictionary.items())

#     return alpha_rest


def print_rest_ratings(dictionary):
    """ Print out restaurants and related ratings in alphabetical order. """

    for restaurant, rating in sorted(dictionary.items()):
        # restaurant = i[0]
        # rating = i[1]

        print "{restaurant} is rated at {rating}.".format(restaurant=restaurant,
                                                          rating=rating)


def get_user_rating(dictionary):
    """ Takes a restaurant and rating as user input and adds it to dictionary. """

    user_restaurant = raw_input("Please enter a restaurant name: ")

    while True:
        user_rating = (raw_input("Please give that restaurant a rating: "))

        if user_rating.isdigit():
            user_rating = int(user_rating)

        if (user_rating >= 1) and (user_rating <= 5):
            dictionary[user_restaurant] = user_rating
            break
        else:
            print "Scores must be between 1 and 5. Please try again."


def update_rating(dictionary):
    """ Updates a restaurant's rating based on user input. """

    random.choice(dictionary.key())


def get_menu():
    """ Displays menu of options for user to pick from. """

    print "\n1 - See the ratings of each restaurant in alphabetical order."
    print "2 - Add a new restaurant and related rating."
    print "3 - Update a restaurant's rating."
    print "4 - Quit\n"


def repl():
    """ Gives user a choice to see all the ratings in alphabetical order, adding a new restaurant with rating, or quitting. """

    restaurant_ratings = get_rest_ratings("scores.txt")

    while True:
        get_menu()

        choice = int(raw_input("What would you like to do? "))

        print "\n"

        if choice == 1:
            print_rest_ratings(restaurant_ratings)
        elif choice == 2:
            get_user_rating(restaurant_ratings)
        elif choice == 3:
            continue
        elif choice == 4:
            break
        else:
            print "That is not one of the options. Please try again."

repl()
