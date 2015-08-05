from segment.Segment import Segment
from segment.Field import Field
import datetime


class HeaderSegment(Segment):

    required = ['id', 'specialChars', 'sendingApplication', 'sendingFacility',
                'receivingFacility', 'messageDate', 'messageType',
                'messageControlId', 'processingId', 'version']

    fieldOrder = ['id', 'specialChars', 'sendingApplication', 'sendingFacility',
                'receivingFacility', 'messageDate', 'security', 'messageType',
                'messageControlId', 'processingId', 'version']

    def is_filled(self):
        if self.id.is_emtpy() or \
                self.specialChars.is_emtpy() or \
                self.sendingApplication.is_emtpy() or \
                self.sendingFacility.is_emtpy() or \
                self.receivingFacility.is_emtpy() or \
                self.messageDate.is_emtpy() or \
                self.messageType.is_emtpy() or \
                self.messageControlId.is_emtpy() or \
                self.processingId.is_emtpy() or \
                self.version.is_emtpy():
            return False
        return True

    def __init__(self):
        self.id = Field('MSH')
        self.specialChars = Field('^~&')
        self.sendingApplication = Field()
        self.sendingFacility = Field()
        self.receivingApplication = Field()
        self.receivingFacility = Field()
        self.messageDate = Field(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
        self.security = Field()
        self.messageType = Field()
        self.messageControlId = Field()
        self.processingId = Field('P')
        self.version = Field('2.2')

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
