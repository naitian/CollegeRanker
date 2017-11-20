import csv
import math
import random

K = 10

colleges = [
    'UIUC',
    'Cornell',
    'Princeton',
    'Georgia Tech',
    'UT Austin',
    'Caltech',
    'UW Madison',
    'UCLA',
    'Columbia',
    'UCSD',
    'Harvard',
    'UPenn',
    'Brown',
    'Rice',
    'Yale',
    'Duke',
    'UMass Amherst',
    'UNC Chapel Hill',
    'Northwestern',
    'U Chicago',
    'Boston University',
    'Harvey Mudd',
    'Northeastern'
]

features = [
    'Culture',
    'Location',
    'Prestige',
    'Major',
    'Affordability',
    'Gut'
]


class Feature(object):

    """Docstring for Feature. """

    def __init__(self, name):
        """TODO: to be defined1.

        :name: TODO

        """
        self._name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.rating = 1500

    @staticmethod
    def update_ratings(winner, loser, draw=False):
        """Update ratings after a match

        :winner: TODO
        :loser: TODO
        :draw: TODO
        :returns: TODO

        """
        r1 = math.pow(10, winner.rating / 400)
        r2 = math.pow(10, loser.rating / 400)

        e1 = r1 / (r1 + r2)
        e2 = r2 / (r1 + r2)

        winner.rating = r1 + K - e1 if not draw else r1 + 0.5 * K - e1
        loser.rating = r2 - e2 if not draw else r2 + 0.5 * K - e2

    def __str__(self):
        """TODO: Docstring for __str__.

        :returns: TODO

        """
        return self._name


class University(object):

    """Docstring for University. """

    def __init__(self, name, feature_set):
        self.name = name
        self.feature_set = []
        for feature in feature_set:
            self.feature_set.append(feature.lower())
            setattr(self, feature.lower(), Feature(feature))

    @property
    def rating(self):
        """TODO: Docstring for rating.
        :returns: TODO

        """
        return sum([getattr(self, feature).rating for feature in self.feature_set]) / len(self.feature_set)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.rating > other.rating

    def __eq__(self, other):
        return self.rating == other.rating

    def __hash__(self):
        return self.name.__hash__()


def list_scores():
    i = 1
    for uni in sorted(unis, reverse=True):
        print("{}. {}({})".format(i, uni, uni.rating))
        i += 1


def save_stats(universities):
    """Save a CSV of ratings

    :returns: TODO

    """
    with open('colleges.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['University'] + features)
        for uni in universities:
            writer.writerow([uni] + [getattr(uni, feature.lower())
                                     .rating for feature in features])


unis = []
feature_empty_set = dict()
for college in colleges:
    uni = University(college, features)
    unis.append(uni)
    for feature in features:
        if feature not in feature_empty_set:
            feature_empty_set[feature] = set()
        feature_empty_set[feature].add(uni)

while True:

    # Choose opponent and features

    # Choose feature from list
    feature = random.choice(features)

    # If feature has colleges that haven't been compared for that
    # feature yet, choose those.
    if len(feature_empty_set[feature]) > 1:
        c1 = random.choice(list(feature_empty_set[feature]))
        c2 = random.choice(list(feature_empty_set[feature]))
        while c1.name == c2.name:
            c2 = random.choice(list(feature_empty_set[feature]))
        feature_empty_set[feature].remove(c1)
        feature_empty_set[feature].remove(c2)
    elif len(feature_empty_set[feature]) == 1:
        c1 = random.choice(list(feature_empty_set[feature]))
        feature_empty_set[feature].remove(c1)
        c2 = random.choice(unis)
    else:
        c1 = random.choice(unis)
        c2 = random.choice(unis)
    while c1.name == c2.name:
        c2 = random.choice(unis)

    # Get feature objects
    f1 = getattr(c1, feature.lower())
    f2 = getattr(c2, feature.lower())

    # "UI"
    print("Choose a University based on {}".format(feature))
    print("1: {}".format(c1))
    print("\tScore: {}".format(f1.rating))
    print("2: {}".format(c2))
    print("\tScore: {}".format(f1.rating))

    result = input("Choose {} (1) or {} (2):\n".format(c1, c2))

    if result == 'Q':
        break

    elif result == 'L':
        list_scores()
        continue

    elif result == "1":
        Feature.update_ratings(f1, f2)
        continue

    elif result == '2':
        Feature.update_ratings(f2, f1)
        continue

    elif result == 'D':
        Feature.update_ratings(f1, f2, draw=True)
        continue

# Post-quit operations
list_scores()
save_stats(sorted(unis, reverse=True))
