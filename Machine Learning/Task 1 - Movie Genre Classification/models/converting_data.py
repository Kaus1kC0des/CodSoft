import csv

# Input and output file paths
input_file_path = 'data/train_data.txt'
output_file_path = 'data/train.csv'

# Open the input and output files
with open(input_file_path, 'r', encoding='utf-8') as infile, open(output_file_path, 'w', encoding='utf-8',
                                                                  newline='') as outfile:
    # Create a CSV writer
    csv_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Write the header
    csv_writer.writerow(['ID', 'TITLE', 'GENRE', 'DESCRIPTION'])

    # Process each line in the input file
    for line in infile:
        # Split the line into fields using ':::' as the delimiter
        fields = line.strip().split(' ::: ')

        # Write the fields to the CSV file
        csv_writer.writerow(fields)

print(f"Conversion completed. CSV file saved at {output_file_path}")