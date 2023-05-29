import os, sys, traceback
def resource_path(relative_path):
        
        
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except Exception:
            pass
            base_path = os.path.abspath(".")
            #print(traceback.format_exc())
            #print('error ', os.path.join(base_path, relative_path))
        print(os.path.join(base_path, relative_path))
        return os.path.join(base_path, relative_path)