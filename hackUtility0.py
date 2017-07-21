from objc_util import *
import time
from ctypes import *

can_run_script = 2

def hide_statusbar():
	global can_run_script
	if can_run_script:
		time.sleep(1)
		print("\nTrying to hide the status bar.")
		time.sleep(2)
		print('Code loaded! Status bar is now hidden.\n')
		ObjCClass('UIApplication').sharedApplication().statusBar().setHidden_(1)
	else:
		time.sleep(1)
		print('\nScript is not running. Please type: start_script() to load it.')
	
def show_statusbar():
	global can_run_script
	if can_run_script:
		time.sleep(1)
		print("\nTrying to show back the status bar.")
		time.sleep(2)
		print('Code loaded! Status bar is now back.\n')
		ObjCClass('UIApplication').sharedApplication().statusBar().setHidden_(0)
	else:
		time.sleep(1)
		print('\nScript is not running. Please type: start_script() to load it.')
	
def change_statusbar_color(color):
	global can_run_script
	if can_run_script:
		time.sleep(1)
		print('\nTrying hard to change status bar color, to your chosen one.')
		time.sleep(4)
		if color == 'black':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').blackColor())
		elif color == 'white':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').whiteColor())
		elif color == 'red':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').redColor())
		elif color == 'green':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').greenColor())
		elif color == 'blue':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').blueColor())
		elif color == 'gray':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').grayColor())
		elif color == 'orange':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').orangeColor())
		elif color == 'purple':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').purpleColor())
		elif color == 'yellow':
			ObjCClass('UIApplication').sharedApplication().statusBar().setForegroundColor_(ObjCClass('UIColor').yellowColor())
		print('Status bar color is now ' + color + '.\n')
	else:
		time.sleep(1)
		print('\nScript is not running. Please type: start_script() to load it.')


def mess_up_resolution():
	global can_run_script
	if can_run_script:
		time.sleep(1)
		print("\nTrying to mess up the phone's Resolution.")
		time.sleep(2)
		print('Code loaded! Messed up graphics.')
		ObjCClass('UIScreen').mainScreen()._setScale_(0.5)
		print('Ouch! This looks horrible!\n')
	else:
		time.sleep(1)
		print('\nScript is not running. Please type: start_script() to load it.')
	


def fix_resoltion():
	global can_run_script
	if can_run_script:
		time.sleep(1)
		print("\nTrying to fix the phone's Resolution")
		time.sleep(2)
		print('Code loaded! Fixed graphics')
		ObjCClass('UIScreen').mainScreen()._setScale_(3)
		print('Thanks god! This is how it should be!\n')
	else:
		time.sleep(1)
		print('\nScript is not running. Please type: start_script() to load it.')
	
	
	
def help_me(help_for=''):
	global can_run_script
	if can_run_script:
		if help_for == '':
			print("\nFor help on a specific command type: help_me(start_script()) or help_me('change_statusbar_color(color), etc.\n\nFor help on all commands type: help_me('everything')\n\n")
		elif help_for == 'everything':
			print("\n1. help_me() provides help and guidance for the commands.\n2. start_script() will start or re-start the execution of this utilitty when exited using exit() command.\n3. hide_statusbar() will hide the statusbar inside Pythonista App.\n4. show_statusbar() will reveal the hidden status bar.\n5. change_starusbar_color(color) command will change the statusbar color inside Pythonista App. Example: change_statusbar_color('red'). Available colors: black, white, red, blue, green, gray, orange, purple, yellow.\n6. mess_up_resolution() will dramatically reduce phone's resolution within Pythonista App.\n7. fix_resolution() will increase phone's resolution back to normal, ouf!\n8. quit_script() will quit the utility and you will have to use start_script() to re-run it.\n")
		elif help_for == 'start_sciprt()':
			print("\nstart_script() will start or re-start the execution of this utilitty when exited using exit() command.\n")
		elif help_for == 'hide_starusbar':
			print("\nhide_statusbar() will hide the statusbar inside Pythonista App.")
		elif help_for == 'show_statusbar':
			print("\nshow_statusbar() will reveal the hidden status bar.")
		elif help_for == 'change_statusbar_color(color)':
			print("\nchange_starusbar_color(color) command will change the statusbar color inside Pythonista App. Example: change_statusbar_color('red'). Available colors: black, white, red, blue, green, gray, orange, purple, yellow.")
		elif help_for == 'mess_up_resolution()':
			print("\nmess_up_resolution() will dramatically reduce phone's resolution within Pythonista App.")
		elif help_for == 'fix_resoltion()':
			print("\nfix_resolution() will increase phone's resolution back to normal, ouf!")
		elif help_for == 'quit_script()':
			print("\nquit_script() will quit the utility and you will have to use start_script() to re-run it.")
		else:
			print('\nWrong command.')
	else:
		time.sleep(1)
		print('\nScript is not running. Please type: start_script() to load it.')
		
def quit_script():
	global can_run_script
	can_run_script = 0
	time.sleep(1)
	print('\nQuitting script!')
	time.sleep(2)
	print('......')
	time.sleep(2)
	print('............')
	time.sleep(2)
	print('........................')
	time.sleep(1)
	print('Script has stopped execution. To re-start it, type: start_script()')

def start_script():
	global can_run_script
	if can_run_script == 0:
		time.sleep(2)
		print('Loading script...')
		time.sleep(2)
		print('Loading library...')
		time.sleep(2)
		print('......')
		time.sleep(2)
		print('............')
		time.sleep(2)
		print('........................\n')
		time.sleep(1)
		
		print("\nWelcome to the hack utility\n\nCommands:\n1.help_me()\n2.start_script()\n3.hide_statusbar()\n4.show_statusbar()\n5.change_statusbar_color(color)\n6.mess_up_resolution()\n7.fix_resolution()\n8.quit_script()")
	elif	can_run_script == 2:
		print("\nWelcome to the hack utility\n\nCommands:\n1.help_me()\n2.start_script()\n3.hide_statusbar()\n4.show_statusbar()\n5.change_statusbar_color(color)\n6.mess_up_resolution()\n7.fix_resolution()\n8.quit_script()")
	else:
		print("\nScript is already running!")
	
	can_run_script = 1


if __name__ == '__main__':
	start_script()
