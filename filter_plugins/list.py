def zip_dict(list, keys):
    '''
    return a dictionary of zipped lists
    '''

    return dict(zip(keys, list))

def flatten(list):
    '''
    flat a list of lists
    '''

    return [item for sublist in list for item in sublist]


class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'zip_dict': zip_dict,
            'flatten': flatten
        }