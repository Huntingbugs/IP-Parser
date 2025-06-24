
import re
# Imports the regex module for pattern matching

def parse_ips_from_file(input_file, output_file):
    # Defines a function to parse IP addresses from a file and write them to another file

    ip_pattern = re.compile(
        r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b|'
        r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b'
    )
    # Compiles a regex pattern to match both IPv4 and IPv6 addresses

    seen = set()
    # Initializes a set to store unique IPs

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # Opens the input file for reading and output file for writing

        for line in infile:
            # Iterates over each line in the input file

            for ip in ip_pattern.findall(line):
                # Finds all IP addresses in the current line

                if ip not in seen:
                    # Checks if the IP is unique

                    outfile.write(ip + '\n')
                    # Writes the unique IP to the output file

                    seen.add(ip)
                    # Adds the IP to the seen set

if __name__ == "__main__":
    # Entry point for script execution
    parse_ips_from_file(r'sample_firewall_rules.txt', 'parsed_ips.txt')
    # Calls the function with the input and output file names
