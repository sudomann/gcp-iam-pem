#!/usr/bin/env python

import json
import sys
from optparse import OptionParser

parser = OptionParser()

parser.add_option("-i", "--input", dest="input_json_filename",
                  help="Google JSON file", metavar="FILE")
parser.add_option("-o", "--output", dest="output_pem_filename",
                  help="Output PEM file", metavar="FILE")

(options, args) = parser.parse_args()

input_json_file = options.input_json_filename
output_pem_file = options.output_pem_filename

if input_json_file is None:
    parser.print_help()
    exit(1)

if output_pem_file is None:
    parser.print_help()
    exit(1)

with open(input_json_file) as infile:

    try:
        data = json.load(infile)
    except:
        print("Failed to parse '%s'" % input_json_file)
        exit(1)

    if not 'private_key' in data:
        print("Failed to find 'private_key' in json file '%s'" % input_json_file)
        exit(1)

    if not 'project_id' in data:
        print("Failed to find 'project_id' in json file '%s'" % input_json_file)
        exit(1)

    if not 'client_email' in data:
        print("Failed to find 'client_email' in json file '%s'" % input_json_file)
        exit(1)

    key = data['private_key']

    if len(key) == 0:
        print("'private_key' unexpectedly empty in json file '%s'" % input_json_file)
        exit(1) 

    project_id = data['project_id']

    if len(project_id) == 0:
        print("'project_id' unexpectedly empty in json file '%s'" % input_json_file)
        exit(1) 

    client_email = data['client_email']

    if len(client_email) == 0:
        print("'client_email' unexpectedly empty in json file '%s'" % input_json_file)
        exit(1) 

    with open(output_pem_file, 'w') as outfile:
        outfile.write(key)

print("Project ID: %s" % project_id)
print("Client Email: %s" % client_email)
print("Successfully wrote PEM file '%s'" % output_pem_file)

exit(0)

# End of python script
