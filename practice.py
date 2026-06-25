assignments = [{"name": "sajan", "points": 15},
               {"name": "sajannn", "points": 16},
               {"name": "ram", "points": 20},
               {"name": "hari", "points": 9}]

def filter_with_points(assignments, points):
    more_than_15 = []
    for assignment in assignments:
        if assignment['points'] > points:
            more_than_15.append(assignment)
    return more_than_15

print(filter_with_points(assignments, 10))
        