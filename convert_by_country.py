import time
import csv

def csv_to_html():
  with open('/Users/guillaumevanleynseele/repos/python_tech_interview_junior/logs.csv', newline='') as logs:
    csv_data = csv.DictReader(logs)
    csv_data = sorted(csv_data, key=lambda row: time.strptime(row['date'], "%m/%d/%Y"))
    csv_data = sorted(csv_data, key=lambda row: row['country'], reverse=True)
    
    
    country = csv_data[0]['country']
    url = '/Users/guillaumevanleynseele/repos/python_tech_interview_junior/countries/'+country+'.html'
    html =  open (url, 'w+')
    start_table = '<table>\n<thead>\n<tr>\n<th>id</th>\n<th>ip</th>\n<th>country</th>\n<th>date</th>\n</thead>\n<tbody>\n'
    html.write(start_table)
    end_table = '</tbody>\n</table>'
    for row in range(len(csv_data)):
        if csv_data[row]['country'] != csv_data[row-1]['country']:
            html.write(end_table)
            html.close()
            country = csv_data[row]['country'] if csv_data[row]['country'] != '' else 'unknown'
            url = '/Users/guillaumevanleynseele/repos/python_tech_interview_junior/countries/'+country+'.html'
            html = open(url, 'w+')
            html.write(start_table)
        html.write('<tr>\n')  
        for value in csv_data[row].values():
            html.write('<td>'+value+'</td>\n')
        html.write('</tr>\n')
  
if __name__ == '__main__':
  before = time.time()
  csv_to_html()
  after = time.time()
  print(f"Done in {after-before} seconds")

