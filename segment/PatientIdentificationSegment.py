from segment.Segment import Segment
from segment.Field import Field


class PatientIdentificationSegment(Segment):

    required = ['id', 'patientId', 'patientName', 'patientDateOfBirth', 'patientSex']

    fieldOrder = ['id', 'setId', 'oldPatientId', 'patientId', 'alternatePatientId',
                  'patientName', 'patientMommaName', 'patientDateOfBirth',
                  'patientSex', 'patientAlias', 'race', 'streetAddress',
                  'countryCode', 'homePhoneNumber', 'businessPhoneNumber',
                  'primaryLanguage', 'maritalStatus', 'religion', 'patientSSN',
                  'driversLicenseNumber', 'mothersIdentifier', 'ethnicGroup',
                  'birthPlace', 'multipleBirthIndicator', 'birthOrder',
                  'citizenship', 'veteranMilitaryStatus', 'nationality',
                  'patientDeathDate', 'patientDeathIndicator',
                  'identityUnknownIndicator', 'identityReliabilityCode',
                  'lastUpdateDate', 'lastUpdateFacility', 'speciesCode',
                  'breedCode', 'strain', 'productionClassCode', 'tribalCitizenship']

    def __init__(self):
        self.id = Field('PID')
        self.setId = Field()
        self.oldPatientId = Field()
        self.patientId = Field()
        self.alternatePatientId = Field()
        self.patientName = Field()
        self.patientMommaName = Field()
        self.patientDateOfBirth = Field()
        self.patientSex = Field()
        self.patientAlias = Field()
        self.race = Field()
        self.streetAddress = Field()
        self.countryCode = Field()
        self.homePhoneNumber = Field()
        self.businessPhoneNumber = Field()
        self.primaryLanguage = Field()
        self.maritalStatus = Field()
        self.religion = Field()
        self.patientSSN = Field()
        self.driversLicenseNumber = Field()
        self.mothersIdentifier = Field()
        self.ethnicGroup = Field()
        self.birthPlace = Field()
        self.multipleBirthIndicator = Field()
        self.birthOrder = Field()
        self.citizenship = Field()
        self.veteranMilitaryStatus = Field()
        self.nationality = Field()
        self.patientDeathDate = Field()
        self.patientDeathIndicator = Field()
        self.identityUnknownIndicator = Field()
        self.identityReliabilityCode = Field()
        self.lastUpdateDate = Field()
        self.lastUpdateFacility = Field()
        self.speciesCode = Field()
        self.breedCode = Field()
        self.strain = Field()
        self.productionClassCode = Field()
        self.tribalCitizenship = Field()

    def is_filled(self):
        if self.id.is_empty() or \
                self.patientId.is_empty() or \
                self.patientName.is_empty() or \
                self.patientSex.is_empty() or \
                self.patientDateOfBirth.is_empty():
            return False
        return True
