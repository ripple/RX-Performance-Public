# Read the first 100 lines from the file
with open('issuers_25k_1.csv', 'r') as file:
    lines = file.readlines()[:100]

# Swap the first 50 lines with the second 50 lines
swapped_lines = lines[50:] + lines[:50]

# Extract only the first column and write to the output file
with open('accounts_25k_Swapped_1.csv', 'w') as file:
    for line in swapped_lines:
        first_column = line.split(',')[0]
        file.write(first_column + '\n')
