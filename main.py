import csv

def read_lookup_table(filename):
    lookup = {}
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (row['dstport'], row['protocol'].lower())
            lookup[key] = row['tag']
    return lookup

def process_flow_logs(log_filename, lookup_table):
    tag_counts = {}
    port_protocol_counts = {}
    with open(log_filename, mode='r') as file:
        for line in file:
            parts = line.strip().split()
            dstport = parts[5]
            protocol_number = parts[7]
            protocol = 'tcp' if protocol_number == '6' else 'udp' if protocol_number == '17' else 'icmp'

            pp_key = (dstport, protocol)
            port_protocol_counts[pp_key] = port_protocol_counts.get(pp_key, 0) + 1

            if (dstport, protocol) in lookup_table:
                tag = lookup_table[(dstport, protocol)]
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            else:
                tag_counts['Untagged'] = tag_counts.get('Untagged', 0) + 1

    return tag_counts, port_protocol_counts


def write_to_file(filename, tag_counts, port_protocol_counts):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(['Tag Counts:'])
        writer.writerow(['Tag', 'Count'])
        for tag, count in sorted(tag_counts.items()):
            writer.writerow([tag, count])

        writer.writerow([]) 

        writer.writerow(['Port/Protocol Combination Counts:'])
        writer.writerow(['Port', 'Protocol', 'Count'])
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            writer.writerow([port, protocol, count])


def main():
    lookup_table = read_lookup_table('lookup_table.csv')
    tag_counts, port_protocol_counts = process_flow_logs('flow_logs.txt', lookup_table)

    write_to_file('output_counts.csv', tag_counts, port_protocol_counts)

    print("Tag counts and port/protocol combination counts have been written to 'output_counts.csv'.")


if __name__ == '__main__':
    main()
