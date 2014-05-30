import os, urllib

myfile = 'placeholder.jpg'
directory = '.' # current directory
os.chdir(directory)

## if file exists, delete it ##
if os.path.isfile(myfile):
    os.remove(myfile)
    print("File deleted!")
else:    ## Show an error ##
    print("Warn: %s file not found. Downloading now..." % myfile)
    f = open(myfile, 'wb')
    f.write(urllib.urlopen('http://placekitten.com/200/300').read())
    ## placekitten.com is a professional website for placeholers using cat.
    print("Inage downloaded.")
    f.close()

#os.getcwd() Show current directory