from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _








lickertfive = (
	('one', 'ONE'),
	('two', 'TWO'),
	('three', 'THREE'),
	('four', 'FOUR'),
	('five', 'FIVE')
)

class QTest(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	ready = models.BooleanField(default=False)
	question_one = models.CharField(max_length=100, choices=lickertfive, blank=True)
	question_two = models.CharField(max_length=100, choices=lickertfive, blank=True)




#############################
### BACKGROUND QUESTIONS ####
#############################

class Questionnaire_Background(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	ready = models.BooleanField(null=True, blank=True)
	birth_place = models.CharField(null=True, max_length=200, blank=True) #txt
	current_residence = models.CharField(null=True, max_length=200, blank=True) #txt
	education_level = models.CharField(null=True, max_length=200, blank=True) #choice EDUCATION_OPTIONS
	raised_in_targetplace = models.CharField(null=True, max_length=200, blank=True)
	raised_place = models.CharField(null=True, max_length=200, blank=True) #txt
	generations_in_targetplace = models.CharField(null=True, max_length=200, blank=True)#choice ISO_GENERATION_OPTIONS
	time_away_from_targetplace = models.BooleanField(null=True, blank=True)#bool
	time_away_from_targetplace_elaboration = models.TextField(null=True, blank=True)#BIGtxt
	plan_to_live_in_targetplace = models.CharField(null=True, max_length=200, blank=True)#bool




###################################
### LANGUAGE ABILITY QUESTIONS ####
###################################

class Questionnaire_LanguageAbility(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	mother_tongue  = models.CharField(max_length=200, blank=True)#choice
	mother_tongue_other = models.CharField(max_length=200, blank=True) #txt
	mother_tongue_itsComplicated = models.TextField(blank=True) #BIGtxt
	how_long_target = models.CharField(max_length=200, blank=True) #choice
	rate_target_speaking = models.CharField(max_length=200, blank=True) #choice - likert9
	rate_target_listening = models.CharField(max_length=200, blank=True) #choice - likert9
	formal_education_in_target = models.CharField(max_length=200, blank=True)
	formal_education_elaboration = models.TextField(blank=True)
	rate_polish_speaking = models.CharField(max_length=200, blank=True) #choice - likert9
	rate_polish_listening = models.CharField(max_length=200, blank=True) #choice - likert9
	know_other_languages = models.CharField(max_length=200, blank=True)#bool
	addLang_1 = models.CharField(max_length=200, blank=True) #txt
	addLang_1_rate_speaking = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_1_rate_listening = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_2 = models.CharField(max_length=200, blank=True) #txt
	addLang_2_rate_speaking = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_2_rate_listening = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_3 = models.CharField(max_length=200, blank=True) #txt
	addLang_3_rate_speaking = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_3_rate_listening = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_4 = models.CharField(max_length=200, blank=True) #txt
	addLang_4_rate_speaking = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_4_rate_listening = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_5 = models.CharField(max_length=200, blank=True) #txt
	addLang_5_rate_speaking = models.CharField(max_length=200, blank=True) #choice - likert9
	addLang_5_rate_listening = models.CharField(max_length=200, blank=True) #choice - likert9


	

#####################################
### LANGUAGE PRACTICES QUESTIONS ####
#####################################

class Questionnaire_LanguagePractices(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	target_used_in_home  = models.CharField(max_length=200, blank=True)#choice - likert 5
	number_target_interlocuters = models.CharField(max_length=200, blank=True) #txt
	frequency_speaking_target = models.CharField(max_length=200, blank=True) #choice - likert 5
	target_study_time = models.CharField(max_length=200, blank=True) #choice - likert 9
	use_target_with_grandparents  = models.CharField(max_length=200, blank=True)#choice - likert 7
	use_target_with_parents = models.CharField(max_length=200, blank=True)#choice - likert 7
	use_target_with_siblings = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_children = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_familyGathering = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_friends = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_neighbors = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_coworkers = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_businessActivities = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_romanticPartner = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_church = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_healthCare = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_shopping = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_socialMedia = models.CharField(max_length=200, blank=True) #choice - likert 7
	use_target_with_elaboration = models.TextField(blank=True) #BIGtxt
	target_internal_dialogue = models.CharField(max_length=200, blank=True) #choice - likert 5
	target_dreams = models.CharField(max_length=200, blank=True) #choice - lickert 5
	foreign_target_users = models.CharField(max_length=200, blank=True) #choice - lickert 5


	

###########################
### ACTIVISM QUESTIONS ####
###########################
 
class Questionnaire_Activism(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	target_language_how_long = models.CharField(max_length=200, blank=True)
	target_language_motivation = models.TextField(blank=True) #BIGtxt
	target_langauge_engagement = models.CharField(max_length=200, blank=True) #choice -likert 9
	target_culture_engagement = models.CharField(max_length=200, blank=True) #choice -likert 9
	parents_support_language_engagement = models.CharField(max_length=200, blank=True) #choice - likert 0
	parents_support_culture_engagement = models.CharField(max_length=200, blank=True) #choice - likert 9
	family_against_language_engagement = models.CharField(max_length=200, blank=True) #choice - 5
	peers_against_langauge_engagement = models.CharField(max_length=200, blank=True) #choice - 5
	people_against_elaboration = models.TextField(blank=True) #BIGtxt




########################
### SHAME QUESTIONS #### controll group skips
########################	

class Questionnaire_Shame(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	pride_speaking_target = models.CharField(null=True, max_length=200, blank=True) #choice - likert 5
	shame_speaking_target = models.CharField(null=True, max_length=200, blank=True) #choice - likert 5
	avoids_target = models.BooleanField(null=True, blank=True)#bool
	avoids_target_elaboration = models.TextField(null=True, blank=True) #BIGtxt
	target_speaker_criticism = models.CharField(null=True, max_length=200, blank=True) #choice




#############################
### THE FUTURE QUESTIONS ####
#############################	

class Questionnaire_Future(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	locals_should_target = models.CharField(max_length=200, blank=True) #choice
	target_taught_to_schoolChildren = models.CharField(max_length=200, blank=True)  #choice
	target_transmission_important = models.CharField(max_length=200, blank=True) #choice




#################################
### ANYTHING TO ADD QUESTIONS ###
#################################

class Questionnaire_AnythingElse(models.Model):
	user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)
	anything_to_add = models.TextField(blank=True)