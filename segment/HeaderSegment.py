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
