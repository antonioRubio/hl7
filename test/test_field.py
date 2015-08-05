from unittest import TestCase
from segment.Field import Field

__author__ = 'antonio'


class TestField(TestCase):
    def setUp(self):
        self.field = Field()

    def test_init(self):
        self.assertEquals(1, 1)

    def test_empty(self):
        self.assertTrue(self.field.is_emtpy())

    def test_not_empty(self):
        self.field.value = 'a'
        self.assertFalse(self.field.is_emtpy())
