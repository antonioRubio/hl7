from unittest import TestCase
from segment.PatientIdentificationSegment import PatientIdentificationSegment

__author__ = 'luis'


class TestPatientIdentificationSegment(TestCase):
    def setUp(self):
        self.patientIdentificationSegment = PatientIdentificationSegment()

    def test_not_filled_patient_identification_segment(self):
        self.assertFalse(self.patientIdentificationSegment.is_filled())

    def test_filled_patient_identification_segment(self):
        self.patientIdentificationSegment.patientId.value = 'patientID'
        self.patientIdentificationSegment.patientName.value = 'patientName'
        self.patientIdentificationSegment.patientDateOfBirth.value = 'birthDate'
        self.patientIdentificationSegment.patientSex.value = 'sex'
        self.assertTrue(self.patientIdentificationSegment.is_filled())

    def test_filled_hl7_patient_identification_segment(self):
        self.patientIdentificationSegment.patientId.value = 'patientID'
        self.patientIdentificationSegment.patientName.value = 'patientName'
        self.patientIdentificationSegment.patientDateOfBirth.value = 'birthDate'
        self.patientIdentificationSegment.patientSex.value = 'sex'
        self.assertTrue(self.patientIdentificationSegment.is_filled())
        print self.patientIdentificationSegment.to_hl7()