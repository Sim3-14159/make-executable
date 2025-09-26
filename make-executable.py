#! /usr/bin/env python

import sys
import subprocess


if len(sys.argv) < 2:
    print('Example usage: make-executable your file name.txt')
    exit()

if sys.argv[1] == '-t' or sys.argv[1] == '--tool':
    if len(sys.argv) > 2:
        filename = ' '.join(sys.argv[2:])
    else:
        print('Example usage: make-executable -t your file name.txt')
        exit()
else:
    filename = ' '.join(sys.argv[1:])


f = open(filename, 'r')
line = f.readline()

formattedfilename = filename.replace("'", "\\'") 

if not line.startswith('#!'):
    text = f.read()
    text = line + text
    f.close()
    f = open(filename, 'w')
    f.write('#! /usr/bin/env python\n\n')
    f.write(text)
    f.close()
    subprocess.run(['chmod', '+x', formattedfilename])
    
else:
    subprocess.run(['chmod', '+x', formattedfilename])


print(f'Successfully made the file \'{filename}\' executable.')


if sys.argv[1] == '-t' or sys.argv[1] == '--tool':
    subprocess.run(['sudo', 'mv', filename, '/usr/local/bin/'])
    print(f'\'{filename}\' can now be run as a tool.')
