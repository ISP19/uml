class Hospital:
	def __init__(self, hospital_id:int, hospital_name:str):
		self.id = hospital_id
		self.name = hospital_name

class Patient:
	def __init__(self, patient_id:int, patient_name:str, patient_blood_group:str): # verticies is a list of Points
		self.id = patient_id
		self.name =patient_name
		self.blood = patient_blood_group 

	def symptom(self) -> str:
		# code omitted
		return ""

class Doctor(Hospital):
	def __init__(self, doctor_id:int, doctor_name:str, specialize:str): # verticies is a list of Points
		self.id = doctor_id
		self.name = doctor_name
		self.skill = specialize

	def responsibility(self, use:Medicine) -> str:
		# code omitted
		return ""

class Medicine:
	def __init__(self, *args, **kwargs):
	 super().__init__(*args, **kwargs)