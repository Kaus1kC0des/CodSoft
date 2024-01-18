import csv

input_files = {"train": "data/train_data.txt", "test": "data/test_data.txt",
               "test_data_solution": "data/test_data_solution.txt"}

for i in input_files:
    input_file_path = input_files[i]
    output_file_path = f"data/{i}.csv"
    with (open(input_file_path, 'r', encoding='utf-8') as infile,
          open(output_file_path, 'w', newline='',encoding="utf-8") as outfile):

        writer = csv.writer(outfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if i == "test":
            writer.writerow(["ID", "TITLE", "DESCRIPTION"])
        else:
            writer.writerow(["ID", "TITLE", "GENRE", "DESCRIPTION"])

        for line in infile:
            data = line.strip().split(" ::: ")
            writer.writerow(data)

    print(f"Data of {input_file_path} successfully written to {output_file_path} ")
