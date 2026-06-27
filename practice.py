assignments = [{"name": "sajan", "points": 15},
               {"name": "sajannn", "points": 16},
               {"name": "ram", "points": 20},
               {"name": "hari", "points": 9}]

def get_assignment_names(assignments):
    names = []
    for assignment in assignments:
        names.append(assignment['name'])
    
    return names

print(get_assignment_names(assignments))
        