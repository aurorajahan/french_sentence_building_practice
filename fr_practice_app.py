from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice
import keyboard

# BUILD THE PROGRAM

class Ui_fr_app(object):
	
	# SETUP UI
	
	def setupUi(self, fr_app):
		fr_app.setObjectName("fr_app")
		fr_app.resize(800, 600)
		
		self.centralwidget = QtWidgets.QWidget(fr_app)
		self.centralwidget.setObjectName("centralwidget")
		
		self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
		self.textBrowser.setGeometry(QtCore.QRect(40, 20, 721, 221))
		self.textBrowser.setObjectName("textBrowser")
		self.textBrowser.setFontPointSize(18)
		
		self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox.setGeometry(QtCore.QRect(40, 270, 70, 17))
		self.checkBox.setObjectName("checkBox")
		self.checkBox.setChecked(True)
		
		self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_2.setGeometry(QtCore.QRect(100, 270, 70, 17))
		self.checkBox_2.setObjectName("checkBox_2")
		self.checkBox_2.setChecked(True)
		
		self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_3.setGeometry(QtCore.QRect(150, 270, 70, 17))
		self.checkBox_3.setObjectName("checkBox_3")
		self.checkBox_3.setChecked(True)
		
		self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_4.setGeometry(QtCore.QRect(240, 270, 70, 17))
		self.checkBox_4.setObjectName("checkBox_4")
		self.checkBox_4.setChecked(True)
		
		self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_5.setGeometry(QtCore.QRect(310, 270, 70, 17))
		self.checkBox_5.setObjectName("checkBox_5")
		self.checkBox_5.setChecked(True)
		
		self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_6.setGeometry(QtCore.QRect(370, 270, 70, 17))
		self.checkBox_6.setObjectName("checkBox_6")
		self.checkBox_6.setChecked(True)
		
		self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_7.setGeometry(QtCore.QRect(40, 310, 81, 17))
		self.checkBox_7.setObjectName("checkBox_7")
		self.checkBox_7.setChecked(True)
		
		self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_8.setGeometry(QtCore.QRect(150, 310, 70, 17))
		self.checkBox_8.setObjectName("checkBox_8")
		self.checkBox_8.setChecked(True)
		
		self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_9.setGeometry(QtCore.QRect(40, 350, 81, 17))
		self.checkBox_9.setObjectName("checkBox_9")
		self.checkBox_9.setChecked(True)
		
		self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_10.setGeometry(QtCore.QRect(150, 350, 151, 17))
		self.checkBox_10.setObjectName("checkBox_10")
		self.checkBox_10.setChecked(True)
		
		self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
		self.checkBox_11.setGeometry(QtCore.QRect(40, 390, 91, 17))
		self.checkBox_11.setObjectName("checkBox_11")
		self.checkBox_11.setChecked(True)
		
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(40, 430, 321, 71))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(lambda: self.generate_prompt())
		
		fr_app.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(fr_app)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
		self.menubar.setObjectName("menubar")
		
		fr_app.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(fr_app)
		self.statusbar.setObjectName("statusbar")
		
		fr_app.setStatusBar(self.statusbar)

		self.retranslateUi(fr_app)
		QtCore.QMetaObject.connectSlotsByName(fr_app)
	
	# MAKE THE PROMPT GENERATOR FUNCTION
	
	def generate_prompt(self):
		
		# CHOOSE THE SUBJECT ACCORDING TO CHECKBOXES
		
		subject_list = []
		
		if self.checkBox.isChecked() == True:
			subject_list.append('I')
		
		if self.checkBox_2.isChecked() == True:
			subject_list.append('you (informal)')
		
		if self.checkBox_3.isChecked() == True:
			subject_list.extend(['he', 'she', 'one'])
		
		if self.checkBox_4.isChecked() == True:
			subject_list.append('we')
		
		if self.checkBox_5.isChecked() == True:
			subject_list.append('you (formal)')
		
		if self.checkBox_6.isChecked() == True:
			subject_list.extend(['they (masculine)', 'they (feminine)'])
		
		if subject_list == []:
			self.textBrowser.clear()
			self.textBrowser.append('No subjects selected')
			return
		else:
			subject = choice(subject_list)
		
		# CHOOSE THE VERB
		
		with open("verbs.txt", "r") as verbs_txt:
			verb_list = verbs_txt.readlines()
		verb_list = [verb.strip() for verb in verb_list]

		verb = choice(verb_list)
		
		# CHOOSE THE NEGATIVE ACCORDING TO CHECKBOXES
		
		negative_list = []
		
		if self.checkBox_7.isChecked() == True:
			negative_list.append('affirmative')
		
		if self.checkBox_8.isChecked() == True:
			negative_list.append('negative')
		
		if negative_list == []:
			self.textBrowser.clear()
			self.textBrowser.append('Neither affirmative nor negative selected')
			return
		else:
			negative = choice(negative_list)

		# CHOOSE THE QUESTION ACCORDING TO CHECKBOXES
		
		question_list = []
		
		if self.checkBox_9.isChecked() == True:
			question_list.append('declarative')
		
		if self.checkBox_10.isChecked() == True:
			question_list.append('interrogative')
		
		if question_list == []:
			self.textBrowser.clear()
			self.textBrowser.append('Neither declarative nor interrogative selected')
			return
		else:
			question = choice(question_list)
		
		# CHOOSE THE IMPERATIVE ACCORDING TO CHECKBOXES
		
		imperative_list = ['not imperative']
		
		if self.checkBox_11.isChecked() == True:
			imperative_list.append('imperative')
			
		if question == 'declarative':
			if subject == 'you (informal)' or subject == 'you (formal)' or subject == 'we':
				imperative = choice(imperative_list)
			else:
				imperative = 'not imperative'
		else:
			imperative = 'not imperative'
		
		# GENERATE THE PROMPT
		
		if negative == 'affirmative':
			if imperative == 'imperative':
				prompt = f'Make an {negative}, {question}, {imperative} sentence with {subject} and {verb}.'
			else:
				prompt = f'Make an {negative}, {question} sentence with {subject} and {verb}.'
		else:
			if imperative == 'imperative':
				prompt = f'Make a {negative}, {question}, {imperative} sentence with {subject} and {verb}.'
			else:
				prompt = f'Make a {negative}, {question} sentence with {subject} and {verb}.'

		# SHOW THE PROMPT
		
		self.textBrowser.clear()
		self.textBrowser.append(prompt)

	# GIVE NAMES TO THE UI ITEMS
	
	def retranslateUi(self, fr_app):
		_translate = QtCore.QCoreApplication.translate
		fr_app.setWindowTitle(_translate("fr_app", "French sentence building practice"))
		fr_app.setWindowIcon(QtGui.QIcon('logo.png'))
		self.checkBox.setText(_translate("fr_app", "Je"))
		self.checkBox_2.setText(_translate("fr_app", "Tu"))
		self.checkBox_3.setText(_translate("fr_app", "Il/ Elle/ On"))
		self.checkBox_4.setText(_translate("fr_app", "Nous"))
		self.checkBox_5.setText(_translate("fr_app", "Vous"))
		self.checkBox_6.setText(_translate("fr_app", "Ils/ Elles"))
		self.checkBox_7.setText(_translate("fr_app", "Affirmative"))
		self.checkBox_8.setText(_translate("fr_app", "Negative"))
		self.checkBox_9.setText(_translate("fr_app", "Declarative"))
		self.checkBox_10.setText(_translate("fr_app", "Interrogative"))
		self.checkBox_11.setText(_translate("fr_app", "Imperative"))
		self.pushButton.setText(_translate("fr_app", "Generate Prompt!"))

# RUN THE PROGRAM

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	fr_app = QtWidgets.QMainWindow()
	ui = Ui_fr_app()
	ui.setupUi(fr_app)
	fr_app.show()
	sys.exit(app.exec_())
