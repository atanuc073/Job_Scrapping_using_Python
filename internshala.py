from bs4 import BeautifulSoup
import requests


url="https://internshala.com/internships/matching-preferences"
response=requests.get(url)
data=response.text
soup=BeautifulSoup(data,'html.parser')
internships=soup.find_all('div',{'class':'internship_meta'})
for internship in internships:
    internship_tag=internship.find('a')
    internship_title=internship_tag.text if internship_tag else "N/A"


    company_name_tag=internship.find('a',{'class':'link_display_like_text'})
    company_name=company_name_tag.text if company_name_tag else "N/A"


    internship_location_tag=internship.find('a',{'class':'location_link'})
    if internship_location_tag:
        internship_location=internship_location_tag.text if company_name_tag else "N/A"
    else:
        internship_location="N/A"



    start_date_tag=internship.find('div',{'id':'start-date-first'})
    start_date=start_date_tag.text if start_date_tag else "N/A"


    stipend_tag=internship.find('td',{'class':"stipend_container_table_cell"})
    stipend=stipend_tag.text if stipend_tag else "N/A"

    link='https://internshala.com'+internship.find('a').get('href')
    # link=link_tag.text if link_tag else "N/A"

    print("Internship Title :",internship_title,"\n\nCompany Name :",company_name,"\n\nInternship Location :",internship_location,"\n\nLink :",link,"\n\nStarting Date :",start_date,"\n\nStipened :",stipend,"\n==========")

    #
    # print(internship_title)
    # print(company_name)
    # print(internship_location)
    # print(start_date)
    # print(stipend)
    # print(link)

