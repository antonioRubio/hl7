

class Segment(object):

    separator = '|'
    endSegment = '\r\n'
    required = []
    fieldOrder = []

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.to_hl7()

    def is_filled(self):
        for i in self.required:
            if self.__dict__[i].is_empty():
                return False
        return True

    def to_hl7(self):
        if not self.is_filled():
            raise Exception()
        begin_format_field = "%("
        end_format_field = ")s"
        hl7 = begin_format_field
        join_separator = end_format_field + self.separator + begin_format_field
        hl7 += join_separator.join(self.fieldOrder)
        hl7 += end_format_field
        return hl7 % self.__dict__

