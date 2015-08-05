

class Segment(object):

    separator = '|'
    endSegment = '\r\n'

    def is_filled(self):
        return False

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return self.__str__()

