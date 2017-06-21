# encoding: utf-8
import os


def doc2txt(path):

    # linux must be unoconv -f txt  temp.doc 生成temp.txt
    os.system('python c:\python27\unoconv -f txt  {}'.format(path))

doc2txt('temp.doc')