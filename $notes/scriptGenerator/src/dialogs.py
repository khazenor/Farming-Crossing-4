from lib import mcfunction
from input import dialog

def deployDialogFunctions():
	dialogFunctionParent = 'fc_dialogs'
	mcfunction.clearFunctionFiles(dialogFunctionParent)
	for dialogInst in dialog.dialogs:
		commandText = ""
		for dialogText in dialogInst[dialog.textsKey]:
			commandText += dialogTellRaw(dialogInst[dialog.speakerKey], dialogText) + '\n'
		mcfunction.writeFunction(dialogFunctionParent, dialogInst[dialog.nameKey], commandText)

def dialogTellRaw(name, dialogText):
	return f'tellraw @p ["",{{"text":"<{name}> ","color":"aqua"}},{{"text":"{dialogText}","color":"white"}}]'