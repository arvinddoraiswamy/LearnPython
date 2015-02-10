import argparse

def get_cli_arguments():
    """
    Read command line arguments.
    """
    parser= argparse.ArgumentParser()
    parser.add_argument('file', nargs=1, help='Enter the name of the file you want to reverse engineer here')
    parser.add_argument('-s', action="store_false", help='SHA256 hashes of all sections')
    args = parser.parse_args()

    return args.file, args.s

value_arg_file, value_arg_s= get_cli_arguments()
print "Here are the command line arguments passed to the program"
print value_arg_file, value_arg_s
