# TODO
# Write script here
# Script should delete previous build directory and compile hellocpp application
import os
import shutil

if os.path.exists(os.getcwd() + '/build/') :
	shutil.rmtree(os.getcwd() + '/build/')

os.mkdir('build')
os.chdir(os.getcwd() + '/build/')

print os.getcwd()
os.system('cmake ..')
os.system('cmake --build .')

