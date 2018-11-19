destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
test_traveller = ["Erin Wilkes", "Shanghai, China", ['historical site', 'art']]
attractions = []

def get_destination_index(destination):
    destination_index = destinations.index(destination)
    return destination_index


def get_traveller_location(traveller):
    traveller_destination = traveller[1]
    traveller_destination_index = get_destination_index(traveller_destination)
    return traveller_destination_index

test_destination_index = get_traveller_location(test_traveller)

print(test_destination_index)

for destination in destinations:
    attractions.append([])
    print(attractions)

def add_attraction(destination, attraction):
