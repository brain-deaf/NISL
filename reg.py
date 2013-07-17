import _winreg
import re
import string

def reg_key_delete_value(reg_key_str, reg_key_value):

    if re.search(r'HKEY_LOCAL_MACHINE.+', reg_key_str):
        aReg = _winreg.ConnectRegistry(None, _winreg.HKEY_LOCAL_MACHINE)
        key_str = string.replace(reg_key_str, "HKEY_LOCAL_MACHINE\\", "")
    elif re.search(r'HKEY_CURRENT_USER.+', reg_key_str):
        aReg = _winreg.ConnectRegistry(None, _winreg.HKEY_CURRENT_USER)
        key_str = string.replace(reg_key_str, "HKEY_CURRENT_USER\\", "")
        
    key_list = []
    try:
        aKey = _winreg.OpenKey(aReg, key_str, 0, _winreg.KEY_ALL_ACCESS)
    except:
        print "could not open key!"
        return False

    for i in range(1024):
        try:
            key_list.append(_winreg.EnumValue(aKey, i))
        except:
            break
            
    for i, v in enumerate(key_list):
        if re.search(v[0], reg_key_value):
            _winreg.DeleteValue(aKey, reg_key_value)
            print reg_key_value + " was deleted from " + key_str
            return True
    
    return False 
        
#reg_key_delete_value(r"HKEY_CURRENT_USER\SOFTWARE\Native Instruments\Massive", r"AB2 AudioDevice")