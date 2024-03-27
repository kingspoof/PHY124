


genetic_code_file = open("GeneticCode.txt", "r")
genetic_code = [line.rstrip() for line in genetic_code_file]
genetic_code_dict = {}

# read the genetic code and store the values like requested in a dictionary
for code in genetic_code:
    info = [
        code[:3],
        code[4:]
    ]
    if info[1] not in genetic_code_dict:
        genetic_code_dict[info[1]] = [info[0]]
    else:
        genetic_code_dict[info[1]].append(info[0])



# sort and print the 0'th value for Cysteine
cysteine_values = genetic_code_dict['Cysteine']
cysteine_values.sort()
print(genetic_code_dict)
#print(cysteine_values[0])