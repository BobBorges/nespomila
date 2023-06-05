from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from users.models import UserDetails
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from .models import * #QTest, lickertfive


####################################
####################################
# # # # # # #~ TEST ~# # # # # # # #
####################################
####################################
csbQ1label = "How many eyes do you have?"
csbQ2label = "How many fingers are usually on one hand?"


class InitForm(forms.ModelForm):
	user = forms.CharField(widget=forms.HiddenInput(), required=True)
	ready = forms.BooleanField(required=True)
	next_url = 'one'

	class Meta:
		model = QTest
		fields = ['user', 'ready']


class csb_Q_one(forms.ModelForm):
#	user = forms.CharField(widget=forms.HiddenInput(), required=True)
	question_one = forms.ChoiceField(choices=lickertfive, label=csbQ1label, widget=forms.RadioSelect, required=True)
	next_url = 'two'

	class Meta:
		model = QTest
		fields = ['question_one']


class csb_Q_two(forms.ModelForm):
#	user = forms.CharField(widget=forms.HiddenInput(), required=True)
	question_two = forms.ChoiceField(choices=lickertfive, label=csbQ2label, widget=forms.RadioSelect, required=True)
	next_url = 'finish'

	class Meta:
		model = QTest
		fields = ['question_two']


class finish_form(forms.ModelForm):
	questionnaire_complete = forms.BooleanField(widget=forms.HiddenInput(), required=True, initial=True)

	class Meta:
		model = UserDetails
		fields = ['questionnaire_complete']






####################################
####################################
# # # # #~ QUESTIONNAIRE ~ # # # # #
####################################
####################################







	#############################
	### BACKGROUND QUESTIONS ####
	#############################



#
# URL 'welcome/'
#
WELCOME_LABEL = _('Ready')

class Welcome(forms.ModelForm):
	ready = forms.BooleanField(required=True, label=WELCOME_LABEL)

	class Meta:
		model = Questionnaire_Background
		fields = ['ready']




#
# URL birthplaceresidence/
#
birth_place_label = _('In what city / town were you born? ')
current_residence_label = _('Where do you currently live? ')

class BirthPlaceResidence(forms.ModelForm):
	birth_place = forms.CharField(max_length=200, label=birth_place_label, required=True)
	current_residence = forms.CharField(max_length=200, label=current_residence_label, required=True)

	class Meta:
		model = Questionnaire_Background
		fields = ['birth_place', 'current_residence']




#
# URL educationlevel/
#
education_level_label = _('What is your highest level of education? ')
EDUCATION_OPTIONS = (
	('not finished middleschool', _('I have not (yet) finished middleschool.')), #'jestem w szkole podstawowej lub w gimnazjum',
	('finished middleschool', _('I have finished middleschool.')), #'ukończyłem/am gimnazjum',
	('not finished secondary school', _('I have not (yet) finished secondary school.')), # 'jestem w liceum/technikum/szkole zawodowej',
	('finished secondary school', _('I have finished secondary school.')), # 'ukończyłem/am liceum/technikum/szkołę zawodową',
	('not finished Bachelor', _('I have not (yet) finished undergraduate education.')), # 'jestem na studiach licencjackich',
	('finished Bachelor', _('I have finished undergraduate education.')), # 'ukończyłem/am licencjat',
	('not finished Master', _('I have not (yet) finished Master sudies.')), # 'jestem na studiach magisterskich', 
	('finished Master', _('I have finished Master studies.')), #		'ukończone studia magisterskie (tytuł magistra)',
	('post Master education',_('I have continued in higher education after finishing Master studies.')) # 'jestem lub ukończyłem/am studia doktoranckie'
)

class EducationLevel(forms.ModelForm):
	education_level = forms.ChoiceField(label=education_level_label, choices=EDUCATION_OPTIONS, required=True, help_text=_('Select Option'))

	class Meta:
		model = Questionnaire_Background
		fields = ['education_level']




#
# URL raised   ### control group skips
#
YESorNO = (
	(True, _('Yes')),
	(False, _('No'))
)

raised_place_label = _('Where were you raised? ')
elaborate = _('Please elaborate. ')

raised_in_places_CSB_label = _('Were you raised in Kaszuby?')
time_away_from_targetplace_CSB_label = _('Have you spent any long periods away from Kaszuby?')

class csb_Raised(forms.ModelForm):
	raised_in_targetplace = forms.ChoiceField(label=raised_in_places_CSB_label, 
										choices=YESorNO, 
										widget=forms.RadioSelect, 
										required=True)
	raised_place = forms.CharField(max_length=200, label=raised_place_label)
	time_away_from_targetplace = forms.ChoiceField(label=time_away_from_targetplace_CSB_label, 
										choices=YESorNO, 
										widget=forms.RadioSelect(attrs={'onchange': 'Raised();'}), 
										required=True)
	time_away_from_targetplace_elaboration = forms.CharField(label=elaborate, 
										widget=forms.Textarea(attrs={'style':'display:none'}), 
										required=False)
	class Meta:
		model = Questionnaire_Background
		fields = ['raised_in_targetplace', 'raised_place', 'time_away_from_targetplace', 'time_away_from_targetplace_elaboration']




raised_in_places_WYM_label = _('Were you raised in Wilamowice? ')
time_away_from_targetplace_WYM_label = _('Have you spent any long periods away from Wilamowice? ')

class wym_Raised(forms.ModelForm):
	raised_in_targetplace = forms.ChoiceField(label=raised_in_places_WYM_label, 
										choices=YESorNO, 
										widget=forms.RadioSelect(attrs={'onchange': 'RaisedOne();'}), 
										required=True)
	raised_place = forms.CharField(max_length=200, label=raised_place_label)
	time_away_from_targetplace = forms.ChoiceField(label=time_away_from_targetplace_WYM_label, 
										choices=YESorNO, 
										widget=forms.RadioSelect(attrs={'onchange': 'Raised();'}), 
										required=True)
	time_away_from_targetplace_elaboration = forms.CharField(label=elaborate, 
										widget=forms.Textarea(attrs={'style':'display:none'}), 
										required=False)
	class Meta:
		model = Questionnaire_Background
		fields = ['raised_in_targetplace', 'raised_place', 'time_away_from_targetplace', 'time_away_from_targetplace_elaboration']




#
# URL generations/   :   control group skips
#
generations_in_targetplace_CSB_label = _('How many generations has your family been in Kaszuby? ')
csb_GENERATION_OPTIONS = (
	('NA', _('I do not know / not applicable.')),
	('0', _('I moved to Kaszuby and am the first in my family.')),
	('1', _('My parents moved to Kaszuby.')),
	('2', _('My grandparents moved to Kaszuby.')),
	('3+', _('My family has been in Kaszuby since before my grandparents.')),
)

class csb_Generations(forms.ModelForm):
	generations_in_targetplace = forms.ChoiceField(label=generations_in_targetplace_CSB_label,
										choices=csb_GENERATION_OPTIONS,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_Background
		fields = ['generations_in_targetplace']




generations_in_targetplace_WYM_label = _('How many generations has your family been in Wilamowice? ')
wym_GENERATION_OPTIONS = (
	('NA', _('I do not know / not applicable.')),
	('0', _('I moved to Wilamowice and am the first in my family.')),
	('1', _('My parents moved to Wilamowice.')),
	('2', _('My grandparents moved to Wilamowice.')),
	('3+', _('My family has been in Wilamowice since before my grandparents.')),
)

class wym_Generations(forms.ModelForm):
	generations_in_targetplace = forms.ChoiceField(label=generations_in_targetplace_WYM_label,
										choices=wym_GENERATION_OPTIONS,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_Background
		fields = ['generations_in_targetplace']




#
# URL residenceplans
#
YESorNO_likert5 = (
	('definitely no',_('Definitely No')), #	'Zdecydowanie nie',
	('probably no',_('Probably No')), #	'Prawdopodobnie nie',
	('I don\'t know',_('I don\'t know')), #	'Nie wiem',
	('probably yes',_('Probably Yes')), # 'Prawdopodobnie tak',
	('definitely yes',_('Definitely Yes')), # 'Zdecydowanie tak']
)

plan_to_live_in_targetplace_CSB_label = _('Do you plan to stay / return / move to Kaszuby? ')

class csb_ResidencePlans(forms.ModelForm):
	plan_to_live_in_targetplace = forms.ChoiceField(label=plan_to_live_in_targetplace_CSB_label,
										choices=YESorNO_likert5,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_Background
		fields = ['plan_to_live_in_targetplace']




plan_to_live_in_targetplace_WYM_label = _('Do you plan to stay / return / move to Wilamowice? ')

class wym_ResidencePlans(forms.ModelForm):
	plan_to_live_in_targetplace = forms.ChoiceField(label=plan_to_live_in_targetplace_WYM_label,
										choices=YESorNO_likert5,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_Background
		fields = ['plan_to_live_in_targetplace']




plan_to_live_in_targetplace_DE_label = _('Do you plan to live in a German-speaking place? ')

class de_ResidencePlans(forms.ModelForm):
	plan_to_live_in_targetplace = forms.ChoiceField(label=plan_to_live_in_targetplace_DE_label,
										choices=YESorNO_likert5,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_Background
		fields = ['plan_to_live_in_targetplace']




plan_to_live_in_targetplace_RU_label = _('Do you plan to live in a Russian-speaking place? ')

class ru_ResidencePlans(forms.ModelForm):
	plan_to_live_in_targetplace = forms.ChoiceField(label=plan_to_live_in_targetplace_RU_label,
										choices=YESorNO_likert5,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_Background
		fields = ['plan_to_live_in_targetplace']








	###################################
	### LANGUAGE ABILITY QUESTIONS ####
	###################################



#
# URL mothertongue
#
mother_tongue_label = _('What is your mother tongue? ')

mother_tongue_itsComplicated_label = _('Please explain: ')

mother_tongue_other_label = _('Write your mother tongue here: ')

MOTHER_TONGUE_CHOICES_CSB = (
	('polish', _('Polish')),
	('kashubian', _('Kashubian')),
	('other', _('Other')),
	('complicated', _('It\'s complicated.'))
)

class csb_MotherTongue(forms.ModelForm):
	mother_tongue = forms.ChoiceField(label=mother_tongue_label,
									choices=MOTHER_TONGUE_CHOICES_CSB,
									widget=forms.RadioSelect(attrs={'onchange': 'MotherTongue();'}),
									required=True)
	mother_tongue_other = forms.CharField(label=mother_tongue_other_label, 
									max_length=200, 
									widget=forms.TextInput(attrs={'style': 'display:none'}),
									required=False)
	mother_tongue_itsComplicated = forms.CharField(label=mother_tongue_itsComplicated_label, 
									widget=forms.Textarea(attrs={'style': 'display:none'}),
									required=False)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['mother_tongue', 'mother_tongue_other', 'mother_tongue_itsComplicated']




MOTHER_TONGUE_CHOICES_WYM = (
	('polish', _('Polish')),
	('wymysorys', _('Wymysorys')),
	('other', _('Other')),
	('complicated', _('It\'s complicated.'))
)

class wym_MotherTongue(forms.ModelForm):
	mother_tongue = forms.ChoiceField(label=mother_tongue_label,
									choices=MOTHER_TONGUE_CHOICES_WYM,
									widget=forms.RadioSelect(attrs={'onchange': 'MotherTongue();'}),
									required=True)
	mother_tongue_other = forms.CharField(label=mother_tongue_other_label, 
									max_length=200, 
									widget=forms.TextInput(attrs={'style': 'display:none'}),
									required=False)
	mother_tongue_itsComplicated = forms.CharField(label=mother_tongue_itsComplicated_label, 
									widget=forms.Textarea(attrs={'style': 'display:none'}),
									required=False)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['mother_tongue', 'mother_tongue_other', 'mother_tongue_itsComplicated']




MOTHER_TONGUE_CHOICES_control = (
	('polish', _('Polish')),
	('other', _('Other')),
	('complicated', _('It\'s complicated.'))
)

class control_MotherTongue(forms.ModelForm):
	mother_tongue = forms.ChoiceField(label=mother_tongue_label,
									choices=MOTHER_TONGUE_CHOICES_control,
									widget=forms.RadioSelect(attrs={'onchange':'MotherTongueOne();'}),
									required=True)
	mother_tongue_other = forms.CharField(label=mother_tongue_other_label, 
									max_length=200, 
									widget=forms.TextInput(attrs={'style': 'display:none'}),
									required=False)
	mother_tongue_itsComplicated = forms.CharField(label=mother_tongue_itsComplicated_label, 
									widget=forms.Textarea(attrs={'style': 'display:none'}),
									required=False)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['mother_tongue', 'mother_tongue_other', 'mother_tongue_itsComplicated']




#
# URL selfrate/'
#
SELF_RATE_OPTIONS = (
	('1', _('1 None')),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', _('9 Fluent'))
)

rate_target_speaking_CSB_label = _('Rate your ability to speak Kashubian. ')
rate_target_listening_CSB_label = _('Rate your abiility to understand spoken Kashubian. ')

class csb_SelfRate(forms.ModelForm):
	rate_target_speaking = forms.ChoiceField(label=rate_target_speaking_CSB_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	rate_target_listening = forms.ChoiceField(label=rate_target_listening_CSB_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['rate_target_speaking', 'rate_target_listening']




rate_target_speaking_WYM_label = _('Rate your ability to speak Wymysorys. ')
rate_target_listening_WYM_label = _('Rate your abiility to understand spoken Wymysorys. ')

class wym_SelfRate(forms.ModelForm):
	rate_target_speaking = forms.ChoiceField(label=rate_target_speaking_WYM_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	rate_target_listening = forms.ChoiceField(label=rate_target_listening_WYM_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['rate_target_speaking', 'rate_target_listening']




rate_target_speaking_DE_label = _('Rate your ability to speak German. ')
rate_target_listening_DE_label = _('Rate your abiility to understand spoken German. ')

class de_SelfRate(forms.ModelForm):
	rate_target_speaking = forms.ChoiceField(label=rate_target_speaking_DE_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	rate_target_listening = forms.ChoiceField(label=rate_target_listening_DE_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['rate_target_speaking', 'rate_target_listening']




rate_target_speaking_RU_label = _('Rate your ability to speak Russian. ')
rate_target_listening_RU_label = _('Rate your abiility to understand spoken Russian. ')

class ru_SelfRate(forms.ModelForm):
	rate_target_speaking = forms.ChoiceField(label=rate_target_speaking_RU_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	rate_target_listening = forms.ChoiceField(label=rate_target_listening_RU_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['rate_target_speaking', 'rate_target_listening']




#
# URL formaleducation/
#
FORMAL_EDUCATION_OPTIONS = (
	('none', _('No formal education')),
	('a1', 'A1'),
	('a2', 'A2'),
	('b1', 'B1'),
	('b2', 'B2'),
	('c1', 'C1'),
	('c2', 'C2')
)

formal_education_elaboration_label = _('Do you feel that your level of formal education adequately reflects your actual abilities? Please explain: ')

formal_education_in_target_CSB_label = _('Please indicate the highest level of formal language education you have completed in Kashubian. ' )

class csb_FormalEducation(forms.ModelForm):
	formal_education_in_target = forms.ChoiceField(label=formal_education_in_target_CSB_label,
													choices=FORMAL_EDUCATION_OPTIONS,
													widget=forms.RadioSelect,
													required=True)
	formal_education_elaboration = forms.CharField(label=formal_education_elaboration_label, widget=forms.Textarea)

	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['formal_education_in_target', 'formal_education_elaboration']




formal_education_in_target_WYM_label = _('Please indicate the highest level of formal language education you have completed in Wymysorys. ')

class wym_FormalEducation(forms.ModelForm):
	formal_education_in_target = forms.ChoiceField(label=formal_education_in_target_WYM_label,
													choices=FORMAL_EDUCATION_OPTIONS,
													widget=forms.RadioSelect,
													required=True)
	formal_education_elaboration = forms.CharField(label=formal_education_elaboration_label, widget=forms.Textarea)

	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['formal_education_in_target', 'formal_education_elaboration']




formal_education_in_target_DE_label = _('Please indicate the highest level of formal language education you have completed in German. ')

class de_FormalEducation(forms.ModelForm):
	formal_education_in_target = forms.ChoiceField(label=formal_education_in_target_DE_label,
													choices=FORMAL_EDUCATION_OPTIONS,
													widget=forms.RadioSelect,
													required=True)
	formal_education_elaboration = forms.CharField(label=formal_education_elaboration_label, widget=forms.Textarea)

	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['formal_education_in_target', 'formal_education_elaboration']




formal_education_in_target_RU_label = _('Please indicate the highest level of formal language education you have completed in Russian. ')

class ru_FormalEducation(forms.ModelForm):
	formal_education_in_target = forms.ChoiceField(label=formal_education_in_target_RU_label,
													choices=FORMAL_EDUCATION_OPTIONS,
													widget=forms.RadioSelect,
													required=True)
	formal_education_elaboration = forms.CharField(label=formal_education_elaboration_label, widget=forms.Textarea)

	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['formal_education_in_target', 'formal_education_elaboration']




#
# URL plselfrate/
#
rate_polish_speaking_label = _('Rate your ability to speak Polish. ')
rate_polish_listening_label = _('Rate your abiility to understand spoken Polish. ')

class pl_SelfRate(forms.ModelForm):
	rate_polish_speaking = forms.ChoiceField(label=rate_polish_speaking_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	rate_polish_listening = forms.ChoiceField(label=rate_polish_listening_label,
									choices=SELF_RATE_OPTIONS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = ['rate_polish_speaking', 'rate_polish_listening']




#
# URL otherlanguages/
#
know_other_languages_label = _('Do you know other languages? ')

addLang_1_label = _('Indicate as many as five other languages you speak. If you know more than five additional languages, choose the five that you speak best.<br><br>Additional Language 1: <span class="langOneVal"></span>')#txt
addLang_1_rate_speaking_label = _('Rate your ability to speak the language: <span class="langOneVal"></span>') #choice - likert9
addLang_1_rate_listening_label = _('Rate your ability to understand the spoken language: <span class="langOneVal"></span>') #choice - likert9	

addLang_2_label = _('Additional Language 2: <span class="langTwoVal"></span>')#txt
addLang_2_rate_speaking_label = _('Rate your ability to speak the language: <span class="langTwoVal"></span>') #choice - likert9
addLang_2_rate_listening_label = _('Rate your ability to understand the spoken language: <span class="langTwoVal"></span>') #choice - likert9	

addLang_3_label = _('Additional Language 3: <span class="langThreeVal"></span>')#txt
addLang_3_rate_speaking_label = _('Rate your ability to speak the language: <span class="langThreeVal"></span>') #choice - likert9
addLang_3_rate_listening_label = _('Rate your ability to understand the spoken language: <span class="langThreeVal"></span>') #choice - likert9	

addLang_4_label = _('Additional Language 4: <span class="langFourVal"></span>')#txt
addLang_4_rate_speaking_label = _('Rate your ability to speak the language: <span class="langFourVal"></span>') #choice - likert9
addLang_4_rate_listening_label = _('Rate your ability to understand the spoken language: <span class="langFourVal"></span>') #choice - likert9	

addLang_5_label = _('Additional Language 5: <span class="langFiveVal"></span>')#txt
addLang_5_rate_speaking_label = _('Rate your ability to speak the language: <span class="langFiveVal"></span>') #choice - likert9
addLang_5_rate_listening_label = _('Rate your ability to understand the spoken language: <span class="langFiveVal"></span>') #choice - likert9	

class OtherLanguages(forms.ModelForm):
	know_other_languages = forms.ChoiceField(label=know_other_languages_label,
											choices=YESorNO,
											widget=forms.RadioSelect(attrs={'onchange':'AddLang();'}),
											required=True)
	addLang_1 = forms.CharField(max_length=200, label=mark_safe(addLang_1_label), widget=forms.TextInput(attrs={'style': 'display:none'}), required=False) #txt
	addLang_1_rate_speaking = forms.ChoiceField(label=mark_safe(addLang_1_rate_speaking_label),
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)
	addLang_1_rate_listening = forms.ChoiceField(label=mark_safe(addLang_1_rate_listening_label),
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)	
	addLang_2 = forms.CharField(max_length=200, label=addLang_2_label, widget=forms.TextInput(attrs={'style': 'display:none'}), required=False) #txt
	addLang_2_rate_speaking = forms.ChoiceField(label=addLang_2_rate_speaking_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)
	addLang_2_rate_listening = forms.ChoiceField(label=addLang_2_rate_listening_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)	
	addLang_3 = forms.CharField(max_length=200, label=addLang_3_label, widget=forms.TextInput(attrs={'style': 'display:none'}), required=False) #txt
	addLang_3_rate_speaking = forms.ChoiceField(label=addLang_3_rate_speaking_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)
	addLang_3_rate_listening = forms.ChoiceField(label=addLang_3_rate_listening_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)	
	addLang_4 = forms.CharField(max_length=200, label=addLang_4_label, widget=forms.TextInput(attrs={'style': 'display:none'}), required=False) #txt
	addLang_4_rate_speaking = forms.ChoiceField(label=addLang_4_rate_speaking_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)
	addLang_4_rate_listening = forms.ChoiceField(label=addLang_4_rate_listening_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)	
	addLang_5 = forms.CharField(max_length=200, label=addLang_5_label, widget=forms.TextInput(attrs={'style': 'display:none'}), required=False) #txt
	addLang_5_rate_speaking = forms.ChoiceField(label=addLang_5_rate_speaking_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)
	addLang_5_rate_listening = forms.ChoiceField(label=addLang_5_rate_listening_label,
											choices=SELF_RATE_OPTIONS,
											widget=forms.RadioSelect(attrs={'style': 'display:none'}), required=False)	
	class Meta:
		model = Questionnaire_LanguageAbility
		fields = [
			'know_other_languages', 
			'addLang_1', 
			'addLang_1_rate_speaking', 
			'addLang_1_rate_listening', 
			'addLang_2',
			'addLang_2_rate_speaking', 
			'addLang_2_rate_listening', 
			'addLang_3', 
			'addLang_3_rate_speaking', 
			'addLang_3_rate_listening', 
			'addLang_4', 
			'addLang_4_rate_speaking', 
			'addLang_4_rate_listening', 
			'addLang_5', 
			'addLang_5_rate_speaking', 
			'addLang_5_rate_listening'
		]








	#####################################
	### LANGUAGE PRACTICES QUESTIONS ####
	#####################################




#
# URL homelanguage/
#
NEVER_to_ALWAYS = (
	('never', _('Never')),
	('sometimes', _('Sometimes')),
	('often', _('Often')),
	('very often', _('Very Often')),
	('always', _('Always'))
)

target_used_in_home_CSB_label = _('Is Kashubian used in your home? ')

class csb_HomeLanguage(forms.ModelForm):
	target_used_in_home = forms.ChoiceField(label=target_used_in_home_CSB_label,
											choices=NEVER_to_ALWAYS, 
											widget=forms.RadioSelect, 
											required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_used_in_home']




target_used_in_home_WYM_label = _('Is Wymysorys used in your home? ')
class wym_HomeLanguage(forms.ModelForm):
	target_used_in_home = forms.ChoiceField(label=target_used_in_home_WYM_label,
											choices=NEVER_to_ALWAYS, 
											widget=forms.RadioSelect, 
											required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_used_in_home']




target_used_in_home_RU_label = _('Is Russian used in your home? ')

class ru_HomeLanguage(forms.ModelForm):
	target_used_in_home = forms.ChoiceField(label=target_used_in_home_RU_label,
											choices=NEVER_to_ALWAYS, 
											widget=forms.RadioSelect, 
											required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_used_in_home']



target_used_in_home_DE_label = _('Is German used in your home? ')

class de_HomeLanguage(forms.ModelForm):
	target_used_in_home = forms.ChoiceField(label=target_used_in_home_DE_label,
											choices=NEVER_to_ALWAYS, 
											widget=forms.RadioSelect, 
											required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_used_in_home']




#
# URL interlocutors/
#
RARELY_to_MOSToftheTIME = (
	('rarely', _('Rarely')),
	('once per week', _('Once per week')),
	('a few times per week', _('A few times per week')),
	('everyday', _('Everyday')),
	('most of the time', _('Most of the time'))
)

number_target_interlocuters_helptext = _('Write number.')
number_target_interlocuters_CSB_label = _('Estimate, with how many people do you speak Kashubian? ')
frequency_speaking_targt_CSB_label = _('How often do you speak Kashubian?')

class csb_InterlocutorsFrequency(forms.ModelForm):
	number_target_interlocuters = forms.CharField(label=number_target_interlocuters_CSB_label, 
												help_text=number_target_interlocuters_helptext,
												required=True)
	frequency_speaking_target = forms.ChoiceField(label=frequency_speaking_targt_CSB_label,
												choices=RARELY_to_MOSToftheTIME,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['number_target_interlocuters', 'frequency_speaking_target']




number_target_interlocuters_WYM_label = _('Estimate, with how many people do you speak Wymysorys? ')
frequency_speaking_targt_WYM_label = _('How often do you speak Wymysorys?')

class wym_InterlocutorsFrequency(forms.ModelForm):
	number_target_interlocuters = forms.CharField(label=number_target_interlocuters_WYM_label, 
												help_text=number_target_interlocuters_helptext,
												required=True)
	frequency_speaking_target = forms.ChoiceField(label=frequency_speaking_targt_WYM_label,
												choices=RARELY_to_MOSToftheTIME,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['number_target_interlocuters', 'frequency_speaking_target']




number_target_interlocuters_DE_label = _('Estimate, with how many people do you speak German? ')
frequency_speaking_targt_DE_label = _('How often do you speak German?')

class de_InterlocutorsFrequency(forms.ModelForm):
	number_target_interlocuters = forms.CharField(label=number_target_interlocuters_DE_label, 
												help_text=number_target_interlocuters_helptext,
												required=True)
	frequency_speaking_target = forms.ChoiceField(label=frequency_speaking_targt_DE_label,
												choices=RARELY_to_MOSToftheTIME,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['number_target_interlocuters', 'frequency_speaking_target']




number_target_interlocuters_RU_label = _('Estimate, with how many people do you speak Russian? ')
frequency_speaking_targt_RU_label = _('How often do you speak Russian?')

class ru_InterlocutorsFrequency(forms.ModelForm):
	number_target_interlocuters = forms.CharField(label=number_target_interlocuters_RU_label, 
												help_text=number_target_interlocuters_helptext,
												required=True)
	frequency_speaking_target = forms.ChoiceField(label=frequency_speaking_targt_RU_label,
												choices=RARELY_to_MOSToftheTIME,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['number_target_interlocuters', 'frequency_speaking_target']




#
# URL studytime/'
#
HOW_OFTEN = (
	('>1 hour/week', _('Less than one hour per week')),
	('1-2 hours/week', _('One to two hours per week')),
	('2-3 hours/week', _('Two to three hours per week')),
	('3-4 hours/week', _('Three to four hours per week')),
	('4-5 hours/week', _('Four to five hours per week')),
	('5-6 hours/week', _('Five to six hours per week')),
	('6-7 hours/week', _('Six to seven hours per week')),
	('7-8 hours/week', _('Seven to eight hours per week')),
	('8-9 hours/week', _('Eight to Nine hours per week')),
	('<9 hours/week', _('Nine or more hours per week'))
)

target_study_time_CSB_label = _('How much time do you spend studying, reading and/or writing Kashubian? ')

class csb_StudyTime(forms.ModelForm):
	target_study_time = forms.ChoiceField(label=target_study_time_CSB_label,
										choices=HOW_OFTEN,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_study_time']




target_study_time_WYM_label = _('How much time do you spend studying, reading and/or writing Wymysorys? ')

class wym_StudyTime(forms.ModelForm):
	target_study_time = forms.ChoiceField(label=target_study_time_WYM_label,
										choices=HOW_OFTEN,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_study_time']




target_study_time_DE_label = _('How much time do you spend studying, reading and/or writing German? ')

class de_StudyTime(forms.ModelForm):
	target_study_time = forms.ChoiceField(label=target_study_time_DE_label,
										choices=HOW_OFTEN,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_study_time']




target_study_time_RU_label = _('How much time do you spend studying, reading and/or writing Russian? ')

class ru_StudyTime(forms.ModelForm):
	target_study_time = forms.ChoiceField(label=target_study_time_RU_label,
										choices=HOW_OFTEN,
										widget=forms.RadioSelect,
										required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_study_time']




#
# URL speakswith/    control group skips
#
HOW_LIKELY = (
	('never', _('Never')),
	('very unlikely', _('Very unlikely')),
	('unlikely', _('Unlikely')),
	('maybe', _('Maybe')),
	('likely', _('Likely')),
	('very likely', _('Very likely')),
	('always', _('Always'))
)

use_target_with_parents_label = _('...with your parents? ') #choice - likert 7
use_target_with_siblings_label = _('...with siblings? ') #choice - likert 7
use_target_with_children_label = _('...with children? (any) ') #choice - likert 7
use_target_with_familyGathering_label = _('...at family gatherings? ') #choice - likert 7
use_target_with_friends_label = _('...with friends? ') #choice - likert 7
use_target_with_neighbors_label = _('...with neighbors? ') #choice - likert 7
use_target_with_coworkers_label = _('...with coworkers? ') #choice - likert 7
use_target_with_businessActivities_label = _('...in business activities? ') #choice - likert 7
use_target_with_romanticPartner_label = _('...with a (potential) romantic partner? ')
use_target_with_church_label = _('...at church? ') #choice - likert 7
use_target_with_healthCare_label = _('...with healthcare providers? ') #choice - likert 7
use_target_with_shopping_label = _('...while shopping? ') #choice - likert 7
use_target_with_socialMedia_label = _('...on social media? ') #choice - likert 7
use_target_with_elaboration_label = _('Would you like to provide any additional details about this question? ')

use_target_with_grandparents_CSB_label = _('How likely are you to speak Kashubian:<br><br>...with your grandparents? ')

class csb_SpeaksWith(forms.ModelForm):
	use_target_with_grandparents = forms.ChoiceField(
		label=mark_safe(use_target_with_grandparents_CSB_label),
		choices=HOW_LIKELY,
		widget=forms.RadioSelect,
		required=True)
	use_target_with_parents = forms.ChoiceField(label=use_target_with_parents_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_siblings = forms.ChoiceField(label=use_target_with_siblings_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_children = forms.ChoiceField(label=use_target_with_children_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_familyGathering = forms.ChoiceField(label=use_target_with_familyGathering_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_friends = forms.ChoiceField(label=use_target_with_friends_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_neighbors = forms.ChoiceField(label=use_target_with_neighbors_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_coworkers = forms.ChoiceField(label=use_target_with_coworkers_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_businessActivities = forms.ChoiceField(
		label=use_target_with_businessActivities_label,
		choices=HOW_LIKELY,
		widget=forms.RadioSelect,
		required=True)
	use_target_with_romanticPartner = forms.ChoiceField(label=use_target_with_romanticPartner_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_church = forms.ChoiceField(label=use_target_with_church_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_healthCare = forms.ChoiceField(label=use_target_with_healthCare_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_shopping = forms.ChoiceField(label=use_target_with_shopping_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_socialMedia = forms.ChoiceField(label=use_target_with_socialMedia_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_elaboration = forms.CharField(label=use_target_with_elaboration_label, widget=forms.Textarea, required=False)

	class Meta:
		model = Questionnaire_LanguagePractices
		fields = [
			'use_target_with_grandparents', 
			'use_target_with_parents', 
			'use_target_with_siblings',
			'use_target_with_children', 
			'use_target_with_familyGathering', 
			'use_target_with_friends',
			'use_target_with_neighbors', 
			'use_target_with_coworkers', 
			'use_target_with_businessActivities',
			'use_target_with_romanticPartner', 
			'use_target_with_church', 
			'use_target_with_healthCare',
			'use_target_with_shopping', 
			'use_target_with_socialMedia', 
			'use_target_with_elaboration'
		]




use_target_with_grandparents_WYM_label = _('How likely are you to speak Wymysorys:<br><br>...with your grandparents? ')

class wym_SpeaksWith(forms.ModelForm):
	use_target_with_grandparents = forms.ChoiceField(
		label=mark_safe(use_target_with_grandparents_WYM_label),
		choices=HOW_LIKELY,
		widget=forms.RadioSelect,
		required=True)
	use_target_with_parents = forms.ChoiceField(label=use_target_with_parents_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_siblings = forms.ChoiceField(label=use_target_with_siblings_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_children = forms.ChoiceField(label=use_target_with_children_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_familyGathering = forms.ChoiceField(label=use_target_with_familyGathering_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_friends = forms.ChoiceField(label=use_target_with_friends_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_neighbors = forms.ChoiceField(label=use_target_with_neighbors_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_coworkers = forms.ChoiceField(label=use_target_with_coworkers_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_businessActivities = forms.ChoiceField(
		label=use_target_with_businessActivities_label,
		choices=HOW_LIKELY,
		widget=forms.RadioSelect,
		required=True)
	use_target_with_romanticPartner = forms.ChoiceField(label=use_target_with_romanticPartner_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_church = forms.ChoiceField(label=use_target_with_church_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_healthCare = forms.ChoiceField(label=use_target_with_healthCare_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_shopping = forms.ChoiceField(label=use_target_with_shopping_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_socialMedia = forms.ChoiceField(label=use_target_with_socialMedia_label,
												choices=HOW_LIKELY,
												widget=forms.RadioSelect,
												required=True)
	use_target_with_elaboration = forms.CharField(label=use_target_with_elaboration_label, widget=forms.Textarea, required=False)

	class Meta:
		model = Questionnaire_LanguagePractices
		fields = [
			'use_target_with_grandparents', 
			'use_target_with_parents', 
			'use_target_with_siblings',
			'use_target_with_children', 
			'use_target_with_familyGathering', 
			'use_target_with_friends',
			'use_target_with_neighbors', 
			'use_target_with_coworkers', 
			'use_target_with_businessActivities',
			'use_target_with_romanticPartner', 
			'use_target_with_church', 
			'use_target_with_healthCare',
			'use_target_with_shopping', 
			'use_target_with_socialMedia', 
			'use_target_with_elaboration'
		]




#
# URL internaldreams/
#
target_internal_dialogue_CSB_label = _('Do you ever think or have internal dialogues in Kashubian? ')
target_dreams_CSB_label = _('Do you ever have dreams in Kashubian? ')

class csb_InternalDreams(forms.ModelForm):
	target_internal_dialogue = forms.ChoiceField(label=target_internal_dialogue_CSB_label,
												choices=NEVER_to_ALWAYS,
												widget=forms.RadioSelect,
												required=True)
	target_dreams = forms.ChoiceField(label=target_dreams_CSB_label,
									choices=NEVER_to_ALWAYS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_internal_dialogue', 'target_dreams']




target_internal_dialogue_WYM_label = _('Do you ever think or have internal dialogues in Wymysorys? ')
target_dreams_WYM_label = _('Do you ever have dreams in Wymysorys? ')

class wym_InternalDreams(forms.ModelForm):
	target_internal_dialogue = forms.ChoiceField(label=target_internal_dialogue_WYM_label,
												choices=NEVER_to_ALWAYS,
												widget=forms.RadioSelect,
												required=True)
	target_dreams = forms.ChoiceField(label=target_dreams_WYM_label,
									choices=NEVER_to_ALWAYS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_internal_dialogue', 'target_dreams']




target_internal_dialogue_DE_label = _('Do you ever think or have internal dialogues in German? ')
target_dreams_DE_label = _('Do you ever have dreams in German? ')

class de_InternalDreams(forms.ModelForm):
	target_internal_dialogue = forms.ChoiceField(label=target_internal_dialogue_DE_label,
												choices=NEVER_to_ALWAYS,
												widget=forms.RadioSelect,
												required=True)
	target_dreams = forms.ChoiceField(label=target_dreams_DE_label,
									choices=NEVER_to_ALWAYS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_internal_dialogue', 'target_dreams']




target_internal_dialogue_RU_label = _('Do you ever think or have internal dialogues in Russian? ')
target_dreams_RU_label = _('Do you ever have dreams in Russian? ')

class ru_InternalDreams(forms.ModelForm):
	target_internal_dialogue = forms.ChoiceField(label=target_internal_dialogue_RU_label,
												choices=NEVER_to_ALWAYS,
												widget=forms.RadioSelect,
												required=True)
	target_dreams = forms.ChoiceField(label=target_dreams_RU_label,
									choices=NEVER_to_ALWAYS,
									widget=forms.RadioSelect,
									required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['target_internal_dialogue', 'target_dreams']




#
# URL foreigntl/    control group skips
#
AGREE_or_NOT = (
	('strongly disagree', _('Strongly disagree')),
	('disagree', _('Disagree')),
	('neutral', _('Neither agree nor disagree')),
	('agree', _('Agree')),
	('strongly agree', _('Strongly Agree'))
)

foreign_target_learners_CSB_label = _('People who are not from Kashubia may learn and use Kashubian. ')

class csb_ForeignTargetLearners(forms.ModelForm):
	foreign_target_users = forms.ChoiceField(label=foreign_target_learners_CSB_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['foreign_target_users']




foreign_target_learners_WYM_label = _('People who are not from Wilamowice may learn and use Wymysorys. ')

class wym_ForeignTargetLearners(forms.ModelForm):
	foreign_target_users = forms.ChoiceField(label=foreign_target_learners_WYM_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_LanguagePractices
		fields = ['foreign_target_users']








	###########################
	### ACTIVISM QUESTIONS ####
	###########################




#
# URL motivationdurration/
#
target_language_how_long_CSB_label = _('How long have you been actively engaged with learning and using Kashubian? ')
target_language_motivation_CSB_label = _('Please describe your motivation for begining to, and continuing to be engaged with the Kashubian language. ')

class csb_MotivationDurration(forms.ModelForm):
	target_language_how_long = forms.CharField(
		label=target_language_how_long_CSB_label, 
		required=True
	)
	target_language_motivation = forms.CharField(
		label=target_language_motivation_CSB_label, 
		widget=forms.Textarea, 
		required=True
	)

	class Meta:
		model = Questionnaire_Activism
		fields = ['target_language_how_long', 'target_language_motivation']




target_language_how_long_WYM_label = _('How long have you been actively engaged with learning and using Wymysorys? ')
target_language_motivation_WYM_label = _('Please describe your motivation for begining to, and continuing to be engaged with Wymysorys. ')

class wym_MotivationDurration(forms.ModelForm):
	target_language_how_long = forms.CharField(
		label=target_language_how_long_WYM_label, 
		required=True
	)
	target_language_motivation = forms.CharField(
		label=target_language_motivation_WYM_label, 
		widget=forms.Textarea, 
		required=True
	)

	class Meta:
		model = Questionnaire_Activism
		fields = ['target_language_how_long', 'target_language_motivation']




target_language_how_long_DE_label = _('How long have you been actively engaged with learning and using German? ')
target_language_motivation_DE_label = _('Please describe your motivation for begining to, and continuing to be engaged with German. ')

class de_MotivationDurration(forms.ModelForm):
	target_language_how_long = forms.CharField(
		label=target_language_how_long_DE_label, 
		required=True
	)
	target_language_motivation = forms.CharField(
		label=target_language_motivation_DE_label, 
		widget=forms.Textarea, required=True
	)

	class Meta:
		model = Questionnaire_Activism
		fields = ['target_language_how_long', 'target_language_motivation']
 


target_language_how_long_RU_label = _('How long have you been actively engaged with learning and using Russian? ')
target_language_motivation_RU_label = _('Please describe your motivation for begining to, and continuing to be engaged with Russian. ')

class ru_MotivationDurration(forms.ModelForm):
	target_language_how_long = forms.CharField(
		label=target_language_how_long_RU_label, 
		required=True
	)
	target_language_motivation = forms.CharField(
		label=target_language_motivation_RU_label, 
		widget=forms.Textarea, 
		required=True
	)

	class Meta:
		model = Questionnaire_Activism
		fields = ['target_language_how_long', 'target_language_motivation']



#
# URL engagement/     Control group skips
#
SELF_RATE_ENGAGEMENT = (
	('1', _('1 No engagement')),
	('2', '2'),
	('3', '3'),
	('4', '4'),
	('5', '5'),
	('6', '6'),
	('7', '7'),
	('8', '8'),
	('9', _('9 Completely dedicated'))
)

target_language_engagement_CSB_label = _('Please rate your level of engagement with the maintenance and revitalization of Kashubian. ')
target_culture_engagement_CSB_label	= _('Please rate your level of engagement with Kashubian culture. ')

class csb_Engagement(forms.ModelForm):
	target_langauge_engagement = forms.ChoiceField(label=target_language_engagement_CSB_label,
												choices=SELF_RATE_ENGAGEMENT,
												widget=forms.RadioSelect,
												required=True)
	target_culture_engagement = forms.ChoiceField(label=target_culture_engagement_CSB_label,
												choices=SELF_RATE_ENGAGEMENT,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_Activism
		fields = ['target_langauge_engagement', 'target_culture_engagement'] # dont fix the typo in langauge




target_language_engagement_WYM_label = _('Please rate your level of engagement with the maintenance and revitalization of Wymysorys. ')
target_culture_engagement_WYM_label	= _('Please rate your level of engagement with Wilamowian culture. ')

class wym_Engagement(forms.ModelForm):
	target_langauge_engagement = forms.ChoiceField(label=target_language_engagement_WYM_label,
												choices=SELF_RATE_ENGAGEMENT,
												widget=forms.RadioSelect,
												required=True)
	target_culture_engagement = forms.ChoiceField(label=target_culture_engagement_WYM_label,
												choices=SELF_RATE_ENGAGEMENT,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_Activism
		fields = ['target_langauge_engagement', 'target_culture_engagement'] # dont fix the typo in langauge




#
# URL parentalsupport/   control group skips
#
PARENTAL_SUPPORT_OPTIONS = (
	('they try to forbid it', _('They try to forbid it.')), # 'Próbują tego zabronić',
	('they are strongly against it', _('They are strongly against it.')), 
	('they are against it', _('They are against it.')), # 'Są przeciwko temu',
	('they don\'t like it', _('They don\'t like it.')), # 'Nie podoba im się to',
	('they are neutral', _('They are neutral.')), #	'Neutralni',
	('they like it', _('They like it.')), #	'Podoba im się to',
	('they support it', _('They support it.')), #	'Wspierają',
	('they strongly support it', _('They strongly support it.')), #	'Bardzo wspierają',
	('they force(d) me into it', _('They force(d) me into it.'))# 'Wymuszają moje zaangażowanie'
)

parents_support_language_engagement_CSB_label = _('How much do your parents / guardians support your involvement with the Kashubian language? ')
parents_support_culture_engagement_CSB_label = _('How much to your parents / guardians support your involvement with Kashubian culture? ')

class csb_ParentalSupport(forms.ModelForm):
	parents_support_language_engagement = forms.ChoiceField(
		label=parents_support_language_engagement_CSB_label,
		choices=PARENTAL_SUPPORT_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	parents_support_culture_engagement = forms.ChoiceField(
		label=parents_support_culture_engagement_CSB_label,
		choices=PARENTAL_SUPPORT_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	class Meta:
		model = Questionnaire_Activism
		fields = ['parents_support_language_engagement', 'parents_support_culture_engagement']



parents_support_language_engagement_WYM_label = _('How much do your parents / guardians support your involvement with Wymysorys? ')
parents_support_culture_engagement_WYM_label = _('How much to your parents / guardians support your involvement with Wilamowian culture? ')

class wym_ParentalSupport(forms.ModelForm):
	parents_support_language_engagement = forms.ChoiceField(
		label=parents_support_language_engagement_WYM_label,
		choices=PARENTAL_SUPPORT_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	parents_support_culture_engagement = forms.ChoiceField(
		label=parents_support_culture_engagement_WYM_label,
		choices=PARENTAL_SUPPORT_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	class Meta:
		model = Questionnaire_Activism
		fields = ['parents_support_language_engagement', 'parents_support_culture_engagement']




#
# URL antagonism/ :  control group skips
#
ANTAGONISM_OPTIONS = (
	('no one', _('No one')),
	('one person', _('One person')),
	('> one person', _('More than one person'))
)

family_against_language_engagement_CSB_label = _('Are there people in your family who are against your engagement with the Kashubian language? ')
peers_against_langauge_engagement_CSB_label = _('Are there people among your peers who are against your engagement with the Kashubian language? ')
people_against_elaboration_CSB_label = _('Would you care to provie more details relating to this question?')

class csb_Antagonism(forms.ModelForm):
	family_against_language_engagement = forms.ChoiceField(
		label=family_against_language_engagement_CSB_label,
		choices=ANTAGONISM_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	peers_against_langauge_engagement = forms.ChoiceField(
		label=peers_against_langauge_engagement_CSB_label,
		choices=ANTAGONISM_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	people_against_elaboration = forms.CharField(
		label=people_against_elaboration_CSB_label, 
		widget=forms.Textarea, 
		required=False)

	class Meta:
		model = Questionnaire_Activism
		fields = [
			'family_against_language_engagement',
			'peers_against_langauge_engagement', 
			'people_against_elaboration'
		]




family_against_language_engagement_WYM_label = _('Are there people in your family who are against your engagement with Wymysorys? ')
peers_against_langauge_engagement_WYM_label = _('Are there people among your peers who are against your engagement with Wymysorys? ')
people_against_elaboration_WYM_label = _('Would you care to provie more details relating to this question?')

class wym_Antagonism(forms.ModelForm):
	family_against_language_engagement = forms.ChoiceField(
		label=family_against_language_engagement_WYM_label,
		choices=ANTAGONISM_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	peers_against_langauge_engagement = forms.ChoiceField(
		label=peers_against_langauge_engagement_WYM_label,
		choices=ANTAGONISM_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	people_against_elaboration = forms.CharField(
		label=people_against_elaboration_WYM_label, 
		widget=forms.Textarea, 
		required=False)

	class Meta:
		model = Questionnaire_Activism
		fields = [
			'family_against_language_engagement',
			'peers_against_langauge_engagement',
			'people_against_elaboration'
		]








	########################
	### SHAME QUESTIONS #### controll group skips
	########################




#
# URL prideshame/  :  control group skips
#
pride_speaking_target_CSB_label = _('Do you ever feel pride from speaking Kashubian? ')
shame_speaking_target_CSB_label = _('Do you ever feel ashamed from speaking Kashubian? ')

class csb_PrideShame(forms.ModelForm):
	pride_speaking_target = forms.ChoiceField(
		label=pride_speaking_target_CSB_label,
		choices=NEVER_to_ALWAYS,
		widget=forms.RadioSelect,
		required=True)
	shame_speaking_target = forms.ChoiceField(
		label=shame_speaking_target_CSB_label,
		choices=NEVER_to_ALWAYS,
		widget=forms.RadioSelect,
		required=True)

	class Meta:
		model = Questionnaire_Shame
		fields = ['pride_speaking_target', 'shame_speaking_target']



pride_speaking_target_WYM_label = _('Do you ever feel pride from speaking Wymysorys? ')
shame_speaking_target_WYM_label = _('Do you ever feel ashamed from speaking Wymysorys? ')

class wym_PrideShame(forms.ModelForm):
	pride_speaking_target = forms.ChoiceField(
		label=pride_speaking_target_WYM_label,
		choices=NEVER_to_ALWAYS,
		widget=forms.RadioSelect,
		required=True)
	shame_speaking_target = forms.ChoiceField(
		label=shame_speaking_target_WYM_label,
		choices=NEVER_to_ALWAYS,
		widget=forms.RadioSelect,
		required=True)

	class Meta:
		model = Questionnaire_Shame
		fields = ['pride_speaking_target', 'shame_speaking_target']




#
# URL criticismavoideance/  :  control group skips
#
CRITICISM_OPTIONS = (
	('never', _('Never')),
	('constructively', _('In a constructive way')),
	('hurtfully', _('In a cruel or hurtful way'))
)

target_speaker_criticism_CSB_label = _('Do other speakers of Kashubian criticize your use of the language? ')
avoids_targt_CSB_label = _('Do you avoid speaking Kashubian in certain situations becuase people may think of you differently or treat you differently if they knew that you speak Kashubian? ')
avoids_target_elaboration_CSB_label = _('Would you like to provide more details relating to this question?')

class csb_CriticismAvoidance(forms.ModelForm):
	target_speaker_criticism = forms.ChoiceField(
		label=target_speaker_criticism_CSB_label,
		choices=CRITICISM_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	avoids_target = forms.ChoiceField(
		label=avoids_targt_CSB_label,
		choices=YESorNO,
		widget=forms.RadioSelect(attrs={'onchange': 'Criticism();'}),
		required=True)
	avoids_target_elaboration = forms.CharField(
		label=avoids_target_elaboration_CSB_label, 
		widget=forms.Textarea, 
		required=False)

	class Meta:
		model = Questionnaire_Shame
		fields = ['target_speaker_criticism', 'avoids_target', 'avoids_target_elaboration']




target_speaker_criticism_WYM_label = _('Do other speakers of Wymysorys criticize your use of the language? ')
avoids_targt_WYM_label = _('Do you avoid speaking Wymysorys in certain situations becuase people may think of you differently or treat you differently if they knew that you speak Wymysorys? ')
avoids_target_elaboration_WYM_label = _('Would you like to provide more details relating to this question?')

class wym_CriticismAvoidance(forms.ModelForm):
	target_speaker_criticism = forms.ChoiceField(
		label=target_speaker_criticism_WYM_label,
		choices=CRITICISM_OPTIONS,
		widget=forms.RadioSelect,
		required=True)
	avoids_target = forms.ChoiceField(
		label=avoids_targt_WYM_label,
		choices=YESorNO,
		widget=forms.RadioSelect(attrs={'onchange': 'Criticism();'}),
		required=True)
	avoids_target_elaboration = forms.CharField(
		label=avoids_target_elaboration_WYM_label, 
		widget=forms.Textarea, 
		required=False)

	class Meta:
		model = Questionnaire_Shame
		fields = ['target_speaker_criticism', 'avoids_target', 'avoids_target_elaboration']








	#############################
	### THE FUTURE QUESTIONS ####
	#############################




#
# URL future/  :  controll group skips
#
locals_should_target_CSB_label = _('People who live in Kashubia should use Kashubian. ')
target_taught_to_schoolChildren_CSB_label = _('The Kashubian language should be taught to all children in Kashubia. ')
target_transmission_important_CSB_label = _('It is important that the Kashubian language is passed to the next generation and future generations after that. ')

class csb_Future(forms.ModelForm):
	locals_should_target = forms.ChoiceField(label=locals_should_target_CSB_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	target_taught_to_schoolChildren = forms.ChoiceField(label=target_taught_to_schoolChildren_CSB_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	target_transmission_important = forms.ChoiceField(label=target_transmission_important_CSB_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_Future
		fields = [
			'locals_should_target', 
			'target_taught_to_schoolChildren', 
			'target_transmission_important'
		]




locals_should_target_WYM_label = _('People who live in Wilamowice should use Wymysorys. ')
target_taught_to_schoolChildren_WYM_label = _('Wymysorys should be taught to all children in Wilamowice. ')
target_transmission_important_WYM_label = _('It is important that Wymysorys is passed to the next generation and future generations after that. ')

class wym_Future(forms.ModelForm):
	locals_should_target = forms.ChoiceField(label=locals_should_target_WYM_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	target_taught_to_schoolChildren = forms.ChoiceField(label=target_taught_to_schoolChildren_WYM_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	target_transmission_important = forms.ChoiceField(label=target_transmission_important_WYM_label,
												choices=AGREE_or_NOT,
												widget=forms.RadioSelect,
												required=True)
	class Meta:
		model = Questionnaire_Future
		fields = [
			'locals_should_target', 
			'target_taught_to_schoolChildren', 
			'target_transmission_important'
		]








	#################################
	### ANYTHING TO ADD QUESTIONS ####
	#################################




#
# URL anythingelse/
#
anything_to_add_label = _('This is the last page of the questionnaire. Do you want to add anything? ')

class AnythingElse(forms.ModelForm):
	anything_to_add = forms.CharField(label=anything_to_add_label, widget=forms.Textarea, required=False)

	class Meta:
		model = Questionnaire_AnythingElse
		fields = ['anything_to_add']