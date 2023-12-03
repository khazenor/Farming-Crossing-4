from lib import mcfunction
from input import dialog

def deployDialogFunctions():
	for dialogInst in dialog.dialogs:
		commandText = ""
		for dialogText in dialogInst[dialog.textsKey]:
			commandText += dialogTellRaw(dialogInst[dialog.speakerKey], dialogText) + '\n'
		mcfunction.writeFunction(dialogInst[dialog.nameKey], commandText)

def dialogTellRaw(name, dialogText):
	return f'tellraw @p ["",{{"text":"<{name}> ","color":"aqua"}},{{"text":"{dialogText}","color":"white"}}]'