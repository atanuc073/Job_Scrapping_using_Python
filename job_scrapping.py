from bs4 import BeautifulSoup
import requests
url ="https://boston.craigslist.org/search/sof"
while True:
    response = requests.get(url)
    print(response)
    data=response.text
    # print(data)

    soup=BeautifulSoup(data,'html.parser')
    titles=soup.find_all('a',{"class":"result-title"})
    for title in titles:
        pass
        # print(title.text)


    addresses=soup.find_all("span",{"class":"result-hood"})
    for address in addresses:
        # print(address.text)
        pass

    jobs=soup.find_all('p',{'class':'result-info'})
    for job in jobs:
        job_title=job.find('a',{'class':'result-title'}).text
        location_tag=job.find('span',{'class':'result-hood'})
        job_location=location_tag.text if location_tag else "N/A"
        date=job.find('time',{'class':'result-date'}).text
        link=job.find('a',{'class':'result-title'}).get('href')


        job_response=requests.get(link)
        job_data=job_response.text
        job_soup=BeautifulSoup(job_data,'html.parser')
        job_description=job_soup.find('section',{'id':'postingbody'}).text
        job_attributes_tag=job_soup.find('p',{'class':'attrgroup'})
        job_attributes=job_attributes_tag.text if job_attributes_tag else "N/A"
        print('job title :', job_title, '\nLocation :', job_location, '\nDate', date, '\nLink', link, '\nJob Description :',job_description, '\n-------')


    url_tag=soup.find('a',{'title':'next page'})
    if url_tag.get('href'):
        url='https://boston.craigslist.org'+url_tag.get('href')
        print(url)

    else:
        break


