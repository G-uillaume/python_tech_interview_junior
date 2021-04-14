import time
import csv

def csv_to_html():
  with open('/Users/guillaumevanleynseele/repos/python_tech_interview_junior/logs.csv', newline='') as logs:
    csv_data = csv.DictReader(logs)
    csv_data = sorted(csv_data, key=lambda row: time.strptime(row['date'], "%m/%d/%Y"))
    csv_data = sorted(csv_data, key=lambda row: row['country'], reverse=True)
    i = 0
    y = 1
    url = '/Users/guillaumevanleynseele/repos/python_tech_interview_junior/ip_datas/ip_data'+str(y)+'.html'
    html =  open (url, 'w+')
    start_table = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta http-equiv="X-UA-Compatible" content="IE=edge">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>IP DATAS</title>\n<link rel="stylesheet" href="../style.css">\n</head>\n<body>\n<table>\n<thead>\n<tr>\n<th>id</th>\n<th>ip</th>\n<th>country</th>\n<th>date</th>\n</thead>\n<tbody>\n'
    html.write('<div class="links">\n<a href="ip_data'+str(y+1)+'.html">Next</a>\n</div>')
    html.write(start_table)
    end_table = '</tbody>\n</table>\n</body>\n</html>\n'
    for row in range(len(csv_data)):
      html.write('<tr>\n')  
      for value in csv_data[row].values():
        html.write('<td>'+value+'</td>\n')
      html.write('</tr>\n')
      i += 1
      if i % 100 == 0 and i != 0 and i < 1000:
        html.write(end_table)
        html.close()
        y += 1
        url = '/Users/guillaumevanleynseele/repos/python_tech_interview_junior/ip_datas/ip_data'+str(y)+'.html'
        html = open(url, 'w+')
        if y == 10:
          html.write('<div class="links">\n<a href="ip_data'+str(y-1)+'.html">Previous</a>\n</div>\n')
        if 1 < y < 10:
          html.write('<div class="links">\n<a href="ip_data'+str(y-1)+'.html">Previous</a>\n')
          html.write('<a href="ip_data'+str(y+1)+'.html">Next</a>\n</div>\n')
        html.write(start_table)
  

if __name__ == '__main__':
  before = time.time()
  csv_to_html()
  after = time.time()
  print(f"Done in {after-before} seconds")

