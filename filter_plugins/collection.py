def in_list(collection, key, list):
    '''
    extract x for every item x in the collection if x[key] is in the list
    '''

    return [x for x in collection if x[key] in list]


def not_in_list(collection, key, list):
    '''
    extract x for every item x in the collection if x[key] is not in the list
    '''

    return [x for x in collection if x[key] not in list]

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'in_list': in_list,
            'not_in_list': not_in_list,
        }