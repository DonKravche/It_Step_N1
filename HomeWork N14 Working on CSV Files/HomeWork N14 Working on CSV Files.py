# 1

import csv

with open("titanic.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    survivors_index = header.index('Survived')

    with open("survived.csv", 'w', newline='') as survived_file:
        writer = csv.writer(survived_file)

        for survivor in reader:
            if survivor[survivors_index] == '1':
                writer.writerow(survivor)


# 2

import csv

with open("organizations-100.csv", 'r') as organizations_file:
    reader = csv.reader(organizations_file)
    header = next(reader)
    number_of_employees_index = header.index('Number of employees')

    with open("sorted_organizations.csv", 'w', newline='') as sorted_organizations_file:
        writer = csv.writer(sorted_organizations_file)
        writer.writerow(header)

        number_of_sorted_employees = sorted(list(reader), key=lambda row: int(row[number_of_employees_index]))
        writer.writerows(number_of_sorted_employees)

# 3

import csv

with open("organizations-100.csv", 'r', newline='') as organizations_ssl_file:
    reader = csv.reader(organizations_ssl_file)
    header = next(reader)
    website_addresses = header.index('Website')

    with open('ssl_companies.csv', 'a', newline='') as ssl_certified_websites_file:
        writer = csv.writer(ssl_certified_websites_file)
        writer.writerow(header)

        for row in reader:
            website = row[website_addresses]
            sliced_website_addresses = website.split(',')
            for address in sliced_website_addresses:
                split_address = address.split(':')
                if split_address[0] == 'https':
                    writer.writerow(row)