def convert_rows_with_commas(input_file, output_file):
    with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
        for line in file_in:
            row = line.strip().split()
            row_with_commas =  '"' + ','.join(row) + '",'
            file_out.write(row_with_commas + '\n')

input_file = input("Enter the path of the input file: ")
output_file = input("Enter the path of the output file: ")

convert_rows_with_commas(input_file, output_file)
