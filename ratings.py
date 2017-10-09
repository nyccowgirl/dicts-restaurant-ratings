"""Restaurant rating lister."""


# put your code here
def get_rest_ratings(filename):
    """ Creates dictionary of restaurants and their related ratings. """

    with open(filename) as rest_file:

        rest_ratings = {}

        for line in rest_file:
            line = line.rstrip()
            restaurant, rating = line.split(":")

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
    user_rating = raw_input("Please give that restaurant a rating: ")
    dictionary[user_restaurant] = user_rating



restaurant_ratings = get_rest_ratings("scores.txt")
get_user_rating(restaurant_ratings)
# sort_restaurants = sort_rest_ratings(complete_ratings)
print_rest_ratings(restaurant_ratings)
