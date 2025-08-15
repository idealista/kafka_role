def uuid_to_base64(self: str, short: bool = False):
    import uuid,base64

    if short:
        return base64.b64encode(uuid.UUID(self).bytes[:12]).decode()
    else:
        return base64.b64encode(uuid.UUID(self).bytes).decode()

def base64_to_uuid(self: str, short: bool = False):
    import uuid,base64

    if short:
        return str(uuid.UUID(bytes=base64.b64decode(self + '==')))
    else:
        return str(uuid.UUID(bytes=base64.b64decode(self)))

class FilterModule(object):
    '''
    custom jinja2 filters for working with collections
    '''

    def filters(self):
        return {
            'uuid_to_base64': uuid_to_base64,
            'base64_to_uuid': base64_to_uuid
        }
