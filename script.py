import re
import csv
csv_location = '/home/hyco/Desktop/email_domain_changer/1millionemails.csv'
domain = r'@yahoo.com$'
new_domain = r'@haykdomain.com'
new_file_location = '/home/hyco/Desktop/email_domain_changer/new_emails.csv'


    

with open(new_file_location,'w') as new_file:
    data = csv.writer(new_file)

    with open(csv_location,'r') as csv_file:
        emails = csv.reader(csv_file)
        for i in emails:
            if re.search(domain,i[0]):
                result = re.sub(domain,new_domain,i[0])
                data.writerow(result.split(','))
            else:
                data.writerow(i)


        




