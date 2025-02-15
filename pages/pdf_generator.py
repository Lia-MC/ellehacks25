# importing modules 
from reportlab.pdfgen import canvas 
from reportlab.pdfbase.ttfonts import TTFont 
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 
from spire.pdf.common import *
from spire.pdf import *

def generate_pdf(name_input, response_text):
    fileName = 'advice.pdf'
    documentTitle = 'advice'
    title = 'Advice for ' + name_input + ' <3'
    subTitle = 'Overview:'
    textLines = [ 
        response_text
    ] 

    pdf = canvas.Canvas(fileName) 
  
    pdf.setTitle(documentTitle) 

    for i in range(pdf.Pages.Count):
        page = pdf.Pages[i]
        page.BackgroundColor = Color.get_LightPink()

    # pdf.SaveToFile("output/SetBackgroundColor.pdf")

  
# registering a external font in python 
# pdfmetrics.registerFont( 
#     TTFont('abc', 'SakBunderan.ttf') 
# ) 
  
# # creating the title by setting it's font  
# # and putting it on the canvas 
# pdf.setFont('abc', 36) 
# pdf.drawCentredString(300, 770, title) 
  
# # creating the subtitle by setting it's font,  
# # colour and putting it on the canvas 
# pdf.setFillColorRGB(0, 0, 255) 
# pdf.setFont("Courier-Bold", 24) 
# pdf.drawCentredString(290, 720, subTitle) 
  
    # drawing a line 
    pdf.line(30, 710, 550, 710) 
  
    # creating a multiline text using  
    # textline and for loop 
    text = pdf.beginText(40, 680) 
    text.setFont("Times New Roman", 18) 
    text.setFillColor(colors.black) 
    for line in textLines: 
        text.textLine(line) 
    pdf.drawText(text) 
  
    # saving the pdf 
    pdf.save()

    return pdf