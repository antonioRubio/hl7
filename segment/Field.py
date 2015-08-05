

class Field(object):

    def __init__(self, value=None):
        self.value = value

    def is_emtpy(self):
        return not self.value

    def __str__(self):
        return str(self.value) if self.value else ''
