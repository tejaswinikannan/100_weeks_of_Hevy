import csv
input_file = 'Hevy_workouts_log_100_weeks.csv'
rows_per_file = 4000  # Since there are 7.8k rows 
with open(input_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)
    file_count = 1
    rows = []
    for i, row in enumerate(reader):
        rows.append(row)
        if (i + 1) % rows_per_file == 0:
            with open(f'Hevy_workouts_log_part{file_count}.csv', 'w', newline='', encoding='utf-8') as out:
                writer = csv.writer(out)
                writer.writerow(header)
                writer.writerows(rows)
            file_count += 1
            rows = []
    if rows:
        with open(f'Hevy_workouts_log_part{file_count}.csv', 'w', newline='', encoding='utf-8') as out:
            writer = csv.writer(out)
            writer.writerow(header)
            writer.writerows(rows)