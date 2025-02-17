import os
import sys
from zipfile import ZipFile

# read a zip file
def extract_zip(file):
    with ZipFile(file, 'r') as zip:
        zip.printdir()

        print('extracting zip file...')
        zip.extractall()
        print('extraction complete')

# write in a zip file
def get_allfile_path(directory=None,filenames=None):
    filepaths=[]

    if directory:
        for dirpath, dirname, fnames in os.walk(directory):
            for filename in fnames:
                filepath=os.path.join(dirpath,filename)
                filepaths.append(filepath)
    elif filenames:
        for filename in filenames:
            dirpath=os.path.dirname(os.path.abspath(sys.argv[0]))
            filepath=os.path.join(dirpath,filename)
            filepaths.append(filepath)
    return filepaths

def create_zip_file(directory=None,filenames=None):
    if directory:
        filepaths=get_allfile_path(directory=directory)
    elif filenames:
        filepaths=get_allfile_path(filenames=filenames)

    with ZipFile('newZip.zip', 'w') as zip:
        print('creating zip file')
        for filepath in filepaths:
            zip.write(filepath)
        print('zip file created')


extract_zip('videoPlayer.zip')
filenames=['components','images','source','Makefile','manifest']
create_zip_file(filenames=filenames)
