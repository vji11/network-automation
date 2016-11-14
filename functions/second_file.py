import first_file

first_file.main()

print "seconds_file.py"

def main():
	print "This run's from the seconds_file.py... {}".format(__name__)

if __name__ == '__main__':
	main()