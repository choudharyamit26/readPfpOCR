# import boto3
# import time
# from boto3 import Session

#
# def startJob():
#     response = None
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='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',
#                       region_name='us-east-2')
#     client = session.client('textract', 'us-east-2')
#     response = client.start_document_text_detection(
#         DocumentLocation={
#             'S3Object': {
#                 'Bucket': 'pagiupload',
#                 'Name': 'كيف تكسب الأصدقاء وتؤثر في الناس_35129_Foulabook.com_.pdf'
#             }
#         })
#     return response["JobId"]
#
#
# def isJobComplete(jobId):
#     # For production use cases, use SNS based notification
#     # Details at: https://docs.aws.amazon.com/textract/latest/dg/api-async.html
#     time.sleep(5)
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='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',
#                       region_name='us-east-2')
#     client = session.client('textract', 'us-east-2')
#     response = client.get_document_text_detection(JobId=jobId)
#     status = response["JobStatus"]
#     print("Job status: {}".format(status))
#
#     while (status == "IN_PROGRESS"):
#         time.sleep(5)
#         response = client.get_document_text_detection(JobId=jobId)
#         status = response["JobStatus"]
#         print("Job status: {}".format(status))
#     return status
#
#
# def getJobResults(jobId):
#     pages = []
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='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',
#                       region_name='us-east-2')
#     client = session.client('textract', 'us-east-2')
#     response = client.get_document_text_detection(JobId=jobId)
#
#     pages.append(response)
#     print("Resultset page recieved: {}".format(len(pages)))
#     nextToken = None
#     if ('NextToken' in response):
#         nextToken = response['NextToken']
#
#     while (nextToken):
#         response = client.get_document_text_detection(JobId=jobId, NextToken=nextToken)
#     pages.append(response)
#     print("Resultset page recieved: {}".format(len(pages)))
#     nextToken = None
#     if ('NextToken' in response):
#         nextToken = response['NextToken']
#     return pages
#
#
# # Document
# s3BucketName = "pagiupload"
# documentName = "كيف تكسب الأصدقاء وتؤثر في الناس_35129_Foulabook.com_.pdf"
# jobId = startJob()
# print("Started job with id: {}".format(jobId))
# if (isJobComplete(jobId)):
#     response = getJobResults(jobId)
# # print(response)
# # Print detected text
# for resultPage in response:
#     for item in resultPage["Blocks"]:
#         if item["BlockType"] == "LINE":
#             print('\033[94m' + item["Text"] + '\033[0m')


# import boto3
# import time

# def startJob(s3BucketName, objectName):
#     response = None
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='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',
#                       region_name='us-east-2')
#     client = session.client('textract', 'us-east-2')
#     response = client.start_document_text_detection(
#         DocumentLocation={
#             'S3Object': {
#                 'Bucket': s3BucketName,
#                 'Name': objectName
#             }
#         })
# response = client.detect_document_text(
#     DocumentLocation={
#         'S3Object': {
#             'Bucket': s3BucketName,
#             'Name': objectName
#         }
#     })
# for item in response['Blocks']:
#     if item['BlockType'] == 'LINE':
#         print('From 1st--------------->>>>>>>>', item['Text'])
#     return response["JobId"]


# def isJobComplete(jobId):
#     # time.sleep(5)
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='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',
#                       region_name='us-east-2')
#     client = session.client('textract', 'us-east-2')
#     response = client.get_document_text_detection(JobId=jobId)
#     status = response["JobStatus"]
#     print("Job status: {}".format(status))
#
#     while (status == "IN_PROGRESS"):
#         # time.sleep(5)
#         response = client.get_document_text_detection(JobId=jobId)
#         status = response["JobStatus"]
#         print("Job status: {}".format(status))
#
#     return status
#
#
# def getJobResults(jobId):
#     pages = []
#
#     # time.sleep(5)
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='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',
#                       region_name='us-east-2')
#     client = session.client('textract', 'us-east-2')
#     response = client.get_document_text_detection(JobId=jobId)
#
#     pages.append(response)
#     print("Resultset page recieved: {}".format(len(pages)))
#     nextToken = None
#     if ('NextToken' in response):
#         nextToken = response['NextToken']
#
#     while (nextToken):
#         # time.sleep(5)
#
#         response = client.get_document_text_detection(JobId=jobId, NextToken=nextToken)
#
#         pages.append(response)
#         print("Resultset page recieved: {}".format(len(pages)))
#         nextToken = None
#         if ('NextToken' in response):
#             nextToken = response['NextToken']
#
#     return pages
#


# # # Document
# s3BucketName = "pagiupload"
# documentName = "كيف تكسب الأصدقاء وتؤثر في الناس_35129_Foulabook.com_.pdf"
# # documentName = "EPG Technical Documentation v1.1.pdf"
#
# jobId = startJob(s3BucketName, documentName)
# print("Started job with id: {}".format(jobId))
# if (isJobComplete(jobId)):
#     response = getJobResults(jobId)
#     #     print('<<<<<<<<<<<<<<>>>>>>>>>>>>', response)
#
#     # Print detected text
#     for resultPage in response:
#         # print('------------------->>>>>>>', resultPage)
#         for item in resultPage["Blocks"]:
#             # print('________________________________', item)
#             if item["BlockType"] == "LINE":
#                 print(item["Text"])

# DetectDocumentText API in Amazon Textract to extract text
# from cStringIO import StringIO
#


# import boto3

# Document
# s3BucketName = "pagiupload"
# documentName = "client_arabic_pdf_pages-9.png"
# #
# # # Amazon Textract client
# session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                   aws_secret_access_key='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',
#                   region_name='us-east-2')
# #     client = session.client('textract', 'us-east-2')
# textract = session.client('textract', 'us-east-2')
#
# # Call Amazon Textract
# response = textract.detect_document_text(
#     Document={
#         'S3Object': {
#             'Bucket': s3BucketName,
#             'Name': documentName
#         }
#     })
#
# # print(response)
#
# # Print detected text
# for item in response["Blocks"]:
#     if item["BlockType"] == "LINE":
#         print('\033[94m' + item["Text"] + '\033[0m')


############################## Amazon rekgnition ########
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

# import boto3

#
# def detect_text(photo, bucket):
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='8YWGYm4TOACOjxHOzQqgRAzAanzO70lICTys540k',
#                       region_name='us-east-2')
#     client = session.client('rekognition', 'us-east-2')
#
#     response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})
#
#     textDetections = response['TextDetections']
#     # print('Detected text\n----------')
#     for text in textDetections:
#         text = ' '.join(text['DetectedText'])
#         print(text)
#         # print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
#         # print('Id: {}'.format(text['Id']))
#         # if 'ParentId' in text:
#         #     print('Parent Id: {}'.format(text['ParentId']))
#         # print('Type:' + text['Type'])
#         print()
#     return len(textDetections)
#
#
# def main():
#     bucket = 'pagiupload'
#     photo = 'client_arabic_pdf_pages-9.png'
#     text_count = detect_text(photo, bucket)
#     print("Text detected: " + str(text_count))
#
#
# if __name__ == "__main__":
#     main()

# import PyPDF2 as pdf
# import codecs
#
# # file = open('arabic.pdf', 'rb')
# file = 'arabic.pdf'
# # file = open('arabic.pdf', mode="r", encoding="utf-8")
# output_filepath = "output.txt"  # output text file path
# output_file = open(output_filepath, "wb")
# # pdf_reader = pdf.PdfFileReader(file)
# pdf_reader = pdf.PdfFileReader(codecs.open(file, "rb"), strict=False)
# print(pdf_reader.getNumPages())
# page1 = pdf_reader.getPage(0).extractText()
# # print(page1)
# for page in pdf_reader.pages:  # loop through pagesre
#     page_text = page.extractText()  # get text from page
#     print(page_text)
#     # page_text = page_text.encode().decode(encoding='utf-8')#decode
#     # page_text = page_text.decode(encoding='utf-8')#decode
#     # print(type(page_text))
#     # page_text = bytes(page_text, 'utf-8')
#     page_text = page_text.encode('utf-8')
#     print('----', page_text.decode('utf-8'))
#     output_file.write(page_text)  # write to file
# output_file.close()

# import pdftotext
# import io
#
# # file = open('كيف تكسب الأصدقاء وتؤثر في الناس_35129_Foulabook.com_.pdf', 'rb')
# file = '/EPG Technical Documentation v1.1.pdf'
# memory_file = io.BytesIO(file)
#
# pdf = pdftotext.PDF(memory_file)
# print(pdf)
# for page in pdf:
#     print(page)
#
# from io import StringIO
#
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.pdfpage import PDFPage
# from pdfminer.pdfparser import PDFParser
# # from cStringIO import StringIO
# #
# output_string = StringIO()
# # with open('EPG Technical Documentation v1.1.pdf', 'rb') as in_file:
# with open('كيف تكسب الأصدقاء وتؤثر في الناس_35129_Foulabook.com_.pdf', 'rb') as in_file:
#     parser = PDFParser(in_file)
#     doc = PDFDocument(parser)
#     rsrcmgr = PDFResourceManager()
#     device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     for page in PDFPage.create_pages(doc):
#         interpreter.process_page(page)
#
# print(output_string.getvalue())
# from pdfminer.pdfinterp import PDFResourceManager, process_pdf
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from cStringIO import StringIO
#
#
# def convert_pdf(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#
#     fp = file(path, 'rb')
#     process_pdf(rsrcmgr, device, fp)
#     fp.close()
#     device.close()
#
#     str = retstr.getvalue()
#     retstr.close()
#     return str


# x = convert_pdf('كيف تكسب الأصدقاء وتؤثر في الناس_35129_Foulabook.com_.pdf')
# print(x)


# import boto3
#
#
# def read_pdf(s3BucketName, objectName):
#     session = Session(aws_access_key_id='AKIAU4GHOSL2LRH2BYHQ',
#                       aws_secret_access_key='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',
#                       region_name='us-east-2')
#     textract = session.client('textract', 'us-east-2')
#     s3 = boto3.resource('s3')
#     try:
#         response = textract.detect_document_text(
#             Document={
#                 'S3Object': {
#                     'Bucket': s3BucketName,
#                     'Name': objectName
#                 }
#             })
#         print('')
#         for item in response["Blocks"]:
#             if item["BlockType"] == "LINE":
#                 print(item['Text'])
#                 return print('Correct')
#     except Exception as e:
#         return print(e)
#
#
# s3BucketName = "pagiupload"
# # documentName = "كيف تكسب الأصدقاء وتؤثر في الناس_35129_Foulabook.com_.pdf"
# documentName = "Screenshot.png"
# # documentName = "EPG Technical Documentation v1.1.pdf"
#
# jobId = read_pdf(s3BucketName, documentName)


#########Tesseract OCR #########
# USAGE
# python ocr_non_english.py --image images/german.png --lang deu

# import the necessary packages
# from textblob import TextBlob
import pytesseract
import argparse
import cv2
from PIL import Image

# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
# 	help="path to input image to be OCR'd")
# ap.add_argument("-l", "--lang", required=True,
# 	help="language that Tesseract will use when OCR'ing")
# ap.add_argument("-t", "--to", type=str, default="en",
# 	help="language that we'll be translating to")
# ap.add_argument("-p", "--psm", type=int, default=13,
# 	help="Tesseract PSM mode")
# args = vars(ap.parse_args())
#
# # load the input image and convert it from BGR to RGB channel
# # ordering
# image = cv2.imread(args["image"])
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# OCR the image, supplying the country code as the language parameter
# options = "-l {} --psm {}".format(args["lang"], args["psm"])
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# text = pytesseract.image_to_string(rgb, config=options)
#
# # show the original OCR'd text
# print("ORIGINAL")
# print("========")
# print(text)
# print("")

# translate the text to a different language
# tb = TextBlob(text)
# translated = tb.translate(to=args["to"])
#
# # show the translated text
# print("TRANSLATED")
# print("==========")
# print(translated)
from pdf2image import convert_from_path


def pdf_image(pdf):
    # poppler_cmd = r'C:\User\Poppler\poppler-0.68.0_x86\poppler-0.68.0\bin'
    page = convert_from_path(pdf, 500)
    for i, image in enumerate(page):
        print(image)
        fname = "pdf" + str(i) + ".png"
        image.save(fname, "PNG")
        return fname
    # page.save('out.png', 'PNG')
    # return page


img = pdf_image('arabic.pdf')
print(img)


def ocr_core(img):
    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(img, lang='ara')
    return text


img = cv2.imread(img)


def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def remove_noise(image):
    return cv2.medianBlur(image, 5)


def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


img = get_grayscale(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))
