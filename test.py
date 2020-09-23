#print("a")
import xlrd
import os
import re
import math 
from datetime import datetime
allowed=['BEG', 'INT','ADV','PRO', 'APT' ]
titles=["", "PG", "PFTV", "GI", "VM", "DFW", "FDE"]

def getDownloadFileURL(url):
	#print(re.findall("https://drive.google.com",url))
	if(re.findall("https://drive.google.com",url)):
		url=url.replace("https://drive.google.com/open?id=", "")
		url=url.replace("https://drive.google.com/file/d/", "")
		url=url.replace("/view?usp=sharing", "")
		fileID=url
		#print(fileID)
		return "https://drive.google.com/uc?export=download&id="+fileID\

	return url
def formatText(textData):
	textData=str(textData)+""
	return textData

def copy0HTML(foldername):
	zerofile = open("0.html", "r")
	zerohtml=zerofile.read()
	zerofile.close()
	#destinationFilename=os.path.join(foldername, "0.html"),
	with open(os.path.join(foldername, "0.html"), 'wb') as temp_file:
			temp_file.write(bytes(zerohtml, 'utf-8'))




def main():
	xlFile=xlrd.open_workbook("Championship Questions V2.xlsx")
	indexTemplatefile = open("indexTemplate.html", "r")
	indexhtml=indexTemplatefile.read()
	indexTemplatefile.close()

	with open('index.html', 'wb') as temp_file:
			temp_file.write(bytes(indexhtml, 'utf-8'))
	
	#templateFile = open("template.html", "r")
	#templateHTML=templateFile.read()
	index=0
	for sheetname in xlFile.sheet_names():

		if(sheetname in allowed):
			print(sheetname)
			if not os.path.exists(sheetname):
				os.mkdir(sheetname)
			generateHTMLFiles(xlFile,index,sheetname)
			updateIndexFile(sheetname)
			copy0HTML(sheetname)
		index=index+1
	addDateInIndexFile()


def addDateInIndexFile():
	indexfile = open("index.html", "r")
	indexhtml=indexfile.read()
	indexfile.close()

	

	today = datetime.now()

	# dd/mm/YY
	d1 = today.strftime("%d/%m/%Y %T")	
	#print(d1)

	indexhtml=indexhtml.replace("#nextbutton","&nbsp;")
	indexhtml=indexhtml.replace("#date",d1)
	with open('index.html', 'wb') as temp_file:
			temp_file.write(bytes(indexhtml, 'utf-8'))

def updateIndexFile(lsheetname):
	indexfile = open("index.html", "r")
	indexhtml=indexfile.read()
	indexfile.close()

	buttonTemplate = open("buttonTemplate.html", "r")
	buttonHTML=buttonTemplate.read()
	buttonTemplate.close()


	buttonHTML=buttonHTML.replace("#link", lsheetname+'/0.html')
	buttonHTML=buttonHTML.replace("#sheetname", lsheetname)

	newindexhtml=indexhtml.replace("#nextbutton",buttonHTML)
	with open('index.html', 'wb') as temp_file:
			temp_file.write(bytes(newindexhtml, 'utf-8'))


def isURL(str):
	
	result= re.match('http', str)
	if(result):
		return True
	return False

def createImage(textData):
	textData=textData.strip()
	#textData=getDownloadFileURL(textData)
	if(isURL(textData)):
		return "<img src='"+textData+"' width='200px'>"
	return textData 	
	


def generateHTMLFiles(workbook, sheetIndex,foldername):
	templateFile = open("template.html", "r")
	templateHTML=templateFile.read()
	templateFile.close()

	
	sheet = workbook.sheet_by_index(sheetIndex)     
	rows=sheet.nrows
	#print(rows)
	# For row 0 and column 0     
	#print(sheet.cell_value(0, 0))
	#print(foldername)
	for row in range(1,rows):
		srno=formatText(sheet.cell_value(row, 0))
		qno=int(sheet.cell_value(row, 0))
		level=foldername
		status=sheet.cell_value(row, 9)
		
		#print(row)
		
		
		 
		day=formatText(sheet.cell_value(row, 1)) 
		dayKey=int(sheet.cell_value(row, 1))
		#category=formatText(sheet.cell_value(row, 5))
		question_text=formatText(sheet.cell_value(row, 2))
		question_image=formatText(sheet.cell_value(row, 3))

		#optionAImage=sheet.cell_value(row, 8)
		optionAText=formatText(sheet.cell_value(row, 4))

		#optionBImage=sheet.cell_value(row, 10)
		optionBText=formatText(sheet.cell_value(row, 5))

		#optionCImage=sheet.cell_value(row, 12)
		optionCText=formatText(sheet.cell_value(row, 6))

		#optionDImage=sheet.cell_value(row, 14)
		optionDText=formatText(sheet.cell_value(row, 7))
		answer=sheet.cell_value(row, 8)

		

		outputfileName=str(row)+".html"
		if(row!=1):
			previousfileName=str(row-1)+".html"
		else:
			previousfileName="index.html"	
		nextFileName=str(row+1)+".html"
		#outfile=open(outputfileName, 'w')
		htmlData=templateHTML

		htmlData=htmlData.replace("#QuestionNumber", formatText(srno))
		htmlData=htmlData.replace("#day", formatText(day))
		#htmlData=htmlData.replace("#version", str(version))
		
		htmlData=htmlData.replace("#Level", level)
		htmlData=htmlData.replace("#questionimage", createImage(question_image))
		htmlData=htmlData.replace("#selected", status)
		#selected
		#htmlData=htmlData.replace("#optionA", "<img src='"+optionAImage+"'>")
		
		#print(isURL(optionAText))
		key=titles[dayKey]+"_"+str(qno)

		htmlData=htmlData.replace("#key", key)
		htmlData=htmlData.replace("#optionA", createImage(optionAText))
		htmlData=htmlData.replace("#optionB", createImage(optionBText))
		htmlData=htmlData.replace("#optionC", createImage(optionCText))
		htmlData=htmlData.replace("#optionD", createImage(optionDText))
		
		htmlData=htmlData.replace("#question", question_text)
		htmlData=htmlData.replace("#AnswerOption", answer)
		htmlData=htmlData.replace("#previousLink", previousfileName)
		htmlData=htmlData.replace("#nextLink", nextFileName)
		htmlData=htmlData.replace("_"+answer, "correctAnswer")
		with open(os.path.join(foldername, outputfileName), 'wb') as temp_file:
			temp_file.write(bytes(htmlData, 'utf-8'))
		
	

main()
		

	





