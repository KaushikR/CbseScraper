# All Imports
import requests
import pprint
import time
import html2text
import csv
from scrapy.selector import Selector

rollno = 5873511

while True:

	try:	
		rollno = rollno + 1
	
		# POST data format for reading data & reqd header 
		data={'regno': str(rollno), 'B1': 'Submit'}
		headers={'Referer':'http://cbseresults.nic.in/class12/cbse122015_all.htm'}
		r = requests.post("http://cbseresults.nic.in/class12/cbse122015_all.asp", data=data, headers=headers)
	
		# To verify if it holds valid data
		VerifyStr = Selector(text=r.text).xpath('/html/body/div[2]/div/font/p[1]/font/b').extract()
	
		if rollno == 5917335:
			print "DONE"
			break;
	
		if VerifyStr:			
			print str(rollno) + " : No data \n"		
		
		else:
		
			# To get the name of the person
			NameTable = Selector(text=r.text).xpath('/html/body/div[2]/table[2]').extract()
			NameStr = html2text.html2text(NameTable[0])		
			NameStr = NameStr.replace("*", "")				
			NameStr = NameStr.replace(u'\xa0', u' ')
			Name = NameStr[44:79]		
			TruncVal = Name.index('\n')
			Name = NameStr[44:43+TruncVal]
			print Name
				
			# To get the marks of a person
			MarksTable = Selector(text=r.text).xpath('/html/body/div[2]/div/center/table').extract()
			MarksStr = html2text.html2text(MarksTable[0])		
			MarksStr = MarksStr.replace("*", "")
			MarksStr = MarksStr.replace(" ", "")
			MarksStr = MarksStr.replace("|", ",")
			MarksStr = MarksStr.replace("\t", "")	
			MarksStr = MarksStr.replace("\s", "")			
			MarksStr = MarksStr.replace("\n", ",")			
			MarksStr = MarksStr.replace(u'\xa0', u' ')
			MarksStr = MarksStr.replace("    FT", "")
			MarksStr = MarksStr.replace("    F", "")
			MarksStr = MarksStr[90:]
			MarksStr = MarksStr[:-3]
			file = open("marks_58.csv", "a")
			file.write(str(rollno) + "," + Name + "," + MarksStr + "\n")		
			print str(rollno) + "\n" #+ MarksStr
				
			# Delays of 3 seconds
			# To prevent DDOS
			# time.sleep(0.1) 
	
	except Exception as e:
		print 'Going to sleep for 30 seconds...\n'
		time.sleep(30)
		continue

