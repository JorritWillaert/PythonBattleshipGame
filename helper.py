

import os
import platform


def isWindows():
    """Check if running on windows"""
    return platform.system().lower() == 'windows'

def clear():
    """clear console output"""
    if isWindows():
        os.system('cls')
    else:
        os.system('clear')

