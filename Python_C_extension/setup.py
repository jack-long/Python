from distutils.core import setup, Extension
# from distutils.extension import Extension

modules = Extension('PDevapi',
                    sources = ['PDevapi.c', 'ctest.c'])

setup (name = 'PDevapi',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [modules])

'''
# name = packagename
setup(name='PDevapi',
    version='2.0',
    ext_modules=[Extension('PDevapi', ['PDevapi.c'])],
    )
'''
