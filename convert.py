import time
import csv

def csv_to_html():
  with open('/Users/guillaumevanleynseele/repos/python_tech_interview_junior/logs.csv', newline='') as logs:
    csv_data = csv.DictReader(logs)
    csv_data = sorted(csv_data, key=lambda row: time.strptime(row['date'], "%m/%d/%Y"))
    csv_data = sorted(csv_data, key=lambda row: row['country'], reverse=True)
    i = 0
    y = 1
    url = '/Users/guillaumevanleynseele/repos/python_tech_interview_junior/ip_data'+str(y)+'.html'
    html =  open (url, 'w+')
    start_table = '<table><thead><tr><th>id</th><th>ip</th><th>country</th><th>date</th></thead><tbody>'
    html.write('<a href="ip_data'+str(y+1)+'.html">Next</a>')
    html.write(start_table)
    end_table = '</tbody></table>'
    for row in range(len(csv_data)):
      html.write('<tr>')  
      for value in csv_data[row].values():
        html.write('<td>'+value+'</td>')
      html.write('</tr>')
      i += 1
      if i % 100 == 0 and i != 0 and i < 1000:
        html.write(end_table)
        html.close()
        y += 1
        url = '/Users/guillaumevanleynseele/repos/python_tech_interview_junior/ip_data'+str(y)+'.html'
        html = open(url, 'w+')
        if y == 10:
          html.write('<a href="ip_data'+str(y-1)+'.html">Previous</a>')
        if 1 < y < 10:
          html.write('<a href="ip_data'+str(y-1)+'.html">Previous</a>')
          html.write('<a href="ip_data'+str(y+1)+'.html">Next</a>')
        html.write(start_table)
  

if __name__ == '__main__':
  before = time.time()
  csv_to_html()
  after = time.time()
  print(f"Done in {after-before} seconds")

