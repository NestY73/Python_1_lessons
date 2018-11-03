#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      User
#
# Created:     03.11.2018
# Copyright:   (c) User 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import sys

def move_to_dir(dir_name):
    try:
        dir_path = os.path.join(os.getcwd(),dir_name)
        return os.chdir(dir_path)
    except FileExistsError:
        return'Такая директория уже существует'

def del_dir(dir_name):
    try:
        dir_path = os.path.join(os.getcwd(),dir_name)
        return os.rmdir(dir_path)
    except FileExistsError:
        return 'Такая директория не существует'

def create_dir(dir_name):
    try:
        dir_path = os.path.join(os.getcwd(),dir_name)
        return os.mkdir(dir_path)
    except FileExistsError:
        return 'Такая директория не существует'

def listdir():
    try:
        dir_path = os.path.join(os.getcwd())
        return os.listdir(dir_path)
    except FileExistsError:
        return 'Такая директория не существует'

