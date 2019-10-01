import os
from bs4 import BeautifulSoup
import urllib.request
import csv
from datetime import datetime
datestring = datetime.strftime(datetime.now(), '%Y-%m-%d-%H.mm.ss')
import filecmp
import requests

print("Welcome to BNPParibas PDF Scrap Program")
input("Press enter to continue")
print("Please wait...")

cwd = os.getcwd()
targetPath = os.path.join(cwd, "Draft");
while not os.path.exists(targetPath):
    os.mkdir(targetPath)

targetFile = os.path.join(targetPath, datestring+'.csv')
#--------------------------Create new directory for PDF------------------------------
targetPath_PDF = os.path.join(targetPath, datestring)
while not os.path.exists(targetPath_PDF):
	os.mkdir(targetPath_PDF)

resp1 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFRP/")
soup1 = BeautifulSoup(resp1,"html.parser")

resp2 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFPRII/")
soup2 = BeautifulSoup(resp2,"html.parser")

resp3 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFRP2/")
soup3 = BeautifulSoup(resp3,"html.parser")

resp4 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDPRIASIAU/")
soup4 = BeautifulSoup(resp4,"html.parser")

resp5 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDPRIMAUSD/")
soup5 = BeautifulSoup(resp5,"html.parser")

resp6 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFEQ/")
soup6 = BeautifulSoup(resp6,"html.parser")

resp7 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFS/")
soup7 = BeautifulSoup(resp7,"html.parser")

resp8 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDINT/")
soup8 = BeautifulSoup(resp8,"html.parser")

resp9 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFEK/")
soup9 = BeautifulSoup(resp9,"html.parser")

resp10 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFIP/")
soup10 = BeautifulSoup(resp10,"html.parser")

resp11 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDFPS/")
soup11 = BeautifulSoup(resp11,"html.parser")

resp12= urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDSOLARIS/")
soup12= BeautifulSoup(resp12,"html.parser")

resp13 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDSTAR/")
soup13 = BeautifulSoup(resp13,"html.parser")

resp14 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/ASTROUSD/")
soup14 = BeautifulSoup(resp14,"html.parser")

resp15 = urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDSFPA/")
soup15 = BeautifulSoup(resp15,"html.parser")

resp16= urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDSCAKRA/")
soup16= BeautifulSoup(resp16,"html.parser")

resp17= urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDISRI/")
soup17= BeautifulSoup(resp17,"html.parser")

resp18= urllib.request.urlopen("https://www.bnpparibas-ip.co.id/en/produk-dan-layanan/produk/RDI30F/")
soup18= BeautifulSoup(resp18,"html.parser")


for link in soup1.findAll('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup2.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()
 

for link in soup3.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup4.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup5.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup6.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup7.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup8.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup9.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup10.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup11.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup12.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup13.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup14.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup15.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup16.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup17.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'):
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()

for link in soup18.find_all('a', href=True):
	if(link['href'].split('.')[-1] == 'pdf'): 
		link['href'] = link['href'].split('/')[-1]
		name = link['href'].split('/')[-1]
		realName = name.replace("%20"," ")
		print(realName)
		f=open(targetFile, "a+")
		f.write(name.replace("%20"," ")+ "\n")
		f.close()


#sudah dapet semua file updated nya dari web bnpparibas , lalu tinggal dibedakan sama yang data kemarin
#updated = file terupdate 
#old = file sebelumnya


f1=open("old.csv","r")
f2=open(targetFile,"r")
i=0

for line1 in f1:
    for line2 in f2:
        if line1!=line2:
            print("======================\nDifferent File\n")
            print("Previous name : " + line1 + "\n")
            print("Updated name : " + line2 + "\n")
            print("Link : https://www.bnpparibas-ip.co.id/files/product/"+line2.replace(" ","%20"))
            print("======================")
            url=("https://www.bnpparibas-ip.co.id/files/product/"+line2.replace(" ","%20"))
            url2=url.replace("\n","")
            myfile = requests.get(url2)
            targetFile_PDF = os.path.join (targetPath_PDF, line2.replace("\n",("")))
            code = open(targetFile_PDF, 'wb').write(myfile.content)   
        break

f1.close()
f2.close()

compare = filecmp.cmp("old.csv", targetFile)

if (compare == True):
	print("=================")
	print ("File is the same, no need to update")
	print("=================")

os.system("pause")