"""Restaurant rating lister."""


# put your code here
def rest_ratings_dict(filename):
    """ Creates dictionary of restaurants and their related ratings. """

    with open(filename) as rest_file:

        rest_rate = {}

        for line in rest_file:
            line = line.rstrip()
            restaurant, rating = line.split(":")

            # restaurant = restaurants[0]
            # rating = restaurants[1]

            rest_rate[restaurant] = rating

    return rest_rate


def sort_rest_ratings(dictionary):
    """ Sort restaurants and respective ratings in alphabetical order. """

    alpha_rest = sorted(dictionary.items())

    return alpha_rest


def print_rest_ratings(lst):
    """ Print out restaurants and related ratings in alphabetical order. """

    for restaurant, rating in lst:
        # restaurant = i[0]
        # rating = i[1]

        print "{restaurant} is rated at {rating}.".format(restaurant=restaurant,
                                                          rating=rating)


restaurants = rest_ratings_dict("scores.txt")
sort_restaurants = sort_rest_ratings(restaurants)
print_rest_ratings(sort_restaurants)
