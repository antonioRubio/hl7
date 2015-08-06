from unittest import TestCase
from segment.HeaderSegment import HeaderSegment

__author__ = 'antonio'


class TestHeaderSegment(TestCase):
    def setUp(self):
        self.headerSegment = HeaderSegment()

    def test_not_filled_header_segment(self):
        self.assertFalse(self.headerSegment.is_filled())

    def test_filled_header_segment(self):
        self.headerSegment.sendingApplication.value = 'sendingApplication'
        self.headerSegment.sendingFacility.value = 'sendingFacility'
        self.headerSegment.receivingApplication.value = 'receivingApplication'
        self.headerSegment.receivingFacility.value = 'receivingFacility'
        self.headerSegment.messageType.value = 'messageType'
        self.headerSegment.messageControlId.value = 'messageControlId'
        self.assertTrue(self.headerSegment.is_filled())

    def test_filled_hl7_header_segment(self):
        self.headerSegment.sendingApplication.value = 'sendingApplication'
        self.headerSegment.sendingFacility.value = 'sendingFacility'
        self.headerSegment.receivingApplication.value = 'receivingApplication'
        self.headerSegment.receivingFacility.value = 'receivingFacility'
        self.headerSegment.messageType.value = 'messageType'
        self.headerSegment.messageControlId.value = 'messageControlId'
        self.assertTrue(self.headerSegment.is_filled())
        print self.headerSegment
