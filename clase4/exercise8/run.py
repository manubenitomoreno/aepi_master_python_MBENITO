import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r'C:\Users\ManuBenito\Documents\GitHub\aepi_master_python_MBENITO\env\Lib\site-packages\wkhtmltopdf')

options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'no-outline': None,
    'quiet': '',
    'footer-html': 'path/to/watermark.html',
    'password': 'your_password'
}

input_pdf = 'in_pdf.pdf'
output_pdf = 'output.pdf'

pdfkit.from_file(input_pdf, output_pdf, options=options)
