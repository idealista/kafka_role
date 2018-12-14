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

def filter_list(list, cond=None):
    '''
    Filter the input list by condition
    '''

    return filter(cond, list)


def filter_evaluated_list(list, cond):
    '''
    Filter the input list by evaluating the input condition from string
    '''

    return filter(eval(cond), list)


class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'zip_dict': zip_dict,
            'flatten_list': flatten,
            'filter': filter_list,
            'filter_evaluated': filter_evaluated_list
        }