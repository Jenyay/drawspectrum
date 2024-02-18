# -*- coding: UTF-8 -*-
"""
Действия, которые зависят от ОС, на которой запущена программа
"""

import os.path
import sys


def getCurrentDir ():
    return os.path.dirname (sys.argv[0])
