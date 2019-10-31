"""use this code to make a UML Diagram"""

class Hospital:# pylint: disable=too-few-public-methods
    """This function contains a hospital id and hospital name but do nothing"""
    def __init__(self, hospital_id: int, hospital_name: str):
        self.id = hospital_id#pylint: disable=invalid-name
        self.name = hospital_name

    def __str__(self):
        return self.__class__.__name__

class Patient:
    """This function represent patient information and also symptom"""
    def __init__(self, patient_id: int, patient_name: str, patient_blood_group: str):
        self.id = patient_id#pylint: disable=invalid-name
        self.name = patient_name
        self.blood = patient_blood_group

    @property
    def symptom(self) -> str:
        """symptom"""
		# code omitted
        return ""
    def __str__(self):
        return self.__class__.__name__

class Medicine:# pylint: disable=too-few-public-methods
    """This function will represent a medicine information"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pass

    def __str__(self):
        return self.__class__.__name__

class Doctor(Hospital):
    """This function represent doctor skill and responsibility"""
    def __init__(self, doctor_id: int, doctor_name: str, specialize: str):
        self.id = doctor_id
        self.name = doctor_name
        self.skill = specialize

    @property
    def responsibility(self, use: Medicine) -> str:
        """omit"""
	    # code omitted
        return use

    def __str__(self):
        return self.__class__.__name__
