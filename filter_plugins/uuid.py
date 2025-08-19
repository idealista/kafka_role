import uuid
import base64

def uuid_to_base64(self: str):
    """
    Convierte un UUID string estándar a base64-url-safe sin padding, como Kafka.
    """
    u = uuid.UUID(self)
    b64 = base64.urlsafe_b64encode(u.bytes).decode('ascii').rstrip("=")
    return b64

def base64_to_uuid(self: str):
    """
    Convierte un base64-url-safe sin padding a UUID string estándar, como Kafka.
    """
    # Añadir padding si falta
    padded = self + '=' * (-len(self) % 4)
    u = uuid.UUID(bytes=base64.urlsafe_b64decode(padded))
    return str(u)
class FilterModule(object):
    '''
    custom jinja2 filters for working with Kafka-style UUIDs
    '''
    def filters(self):
        return {
            'uuid_to_base64': uuid_to_base64,
            'base64_to_uuid': base64_to_uuid
        }
