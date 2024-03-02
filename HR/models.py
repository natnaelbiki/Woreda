from django.db import models


class Staff(models.Model):
	class Hire_Type(models.TextChoices):
		Permanent = 'ቋሚ', ('ቋሚ')
		Contractual = 'ጊዜያዊ', ('ጊዜያዊ')

	class Gender(models.TextChoices):
		FEMALE = 'ሴት', ('ሴት')
		MALE = 'ወ', ('ወ')

	class Ethnicity(models.TextChoices):
		AMHARA = 'አማራ', ('አማራ')
		OROMO = 'ኦሮሞ', ('ኦሮሞ')
		GURAGE = 'ጉራጌ', ('ጉራጌ')
		SOMALI = 'ሱማሌ', ('ሱማሌ')
		HADIYA = 'ሀዲያ', ('ሀዲያ')
		DEBUB = 'ደቡብ', ('ደቡብ')

	class Marital_Status(models.TextChoices):
		Married_Women = 'ያገባች', ('ያገባች')
		Married_Men = 'ያገባ', ('ያገባ')
		Unmarried_Women = 'ያላገባች', ('ያላገባች')
		Unmarried_Men = 'ያላገባ', ('ያላገባ')
		Divorced = 'የፈታ/ች', ('የፈታ/ች')

	full_name_amh = models.CharField(max_length=40)
	full_name_eng = models.CharField(max_length=30)
	gender = models.CharField(max_length=4, choices=Gender.choices, default=Gender.MALE)
	place_of_work = models.CharField(max_length=15)
	pension_id_no = models.CharField(max_length=25, blank=True)
	date_of_birth = models.DateField()
	ethnicity = models.CharField(max_length=8, choices=Ethnicity.choices)
	edu_type = models.CharField(max_length=25, blank=True)
	edu_level = models.CharField(max_length=25, blank=True)
	hired_year = models.DateField()
	years_of_service = models.CharField(max_length=25)
	marital_status = models.CharField(max_length=25, choices=Marital_Status, default=Marital_Status.Unmarried_Men)
	position = models.CharField(max_length=55)
	position_grade = models.CharField(max_length=6)
	salary = models.DecimalField(max_digits=10, decimal_places=2)
	hire_type = models.CharField(max_length=6, choices=Hire_Type, default=Hire_Type.Contractual)
    

	def __str__(self):
		return f"{self.full_name_eng}"
