import filecmp
import sys

sys.stdout.write('\nstarting check same file script\n')

if sys.argv.__len__() < 3:
    sys.stderr.write('insufficient arguments\n\n')
    exit(-1)

file_path = sys.argv[1]
sys.stdout.write('file: ' + file_path + '\n')

other_file_path = sys.argv[2]
sys.stdout.write('other file: ' + other_file_path + '\n')

same = filecmp.cmp(file_path, other_file_path)
if same:
    sys.stdout.write('files are the same\n')
else:
    sys.stdout.write('files are different\n')
