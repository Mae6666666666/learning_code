import json

def retrieve_all():
    my_tuple = ()
    with open("courses_offered_at_uni.json") as courses_offered:
        for component in courses_offered:
            component_dictionary = json.loads(component)
            json.dumps(my_tuple)
            # dict.items(component_dictionary)
            print(component_dictionary)
            adding_tuples = component_dictionary + my_tuple
            print(adding_tuples)
retrieve_all()