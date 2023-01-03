import PyPDF2
import sys


files = sys.argv[1:]
wm_pdf = sys.argv[2]
content_pdf = sys.argv[1]


def pdf_merger():
    global files
    merger = PyPDF2.PdfFileMerger()
    print('PDF Merger')
    proceed = input(f'Selected files to merge {files}. Proceed? Y/N: ')
    if proceed == 'Y' or proceed == 'y':
        for pdf in files:
            merger.append(pdf)
            print(f'Merging {pdf.title()}...')

        merger.write("merged-pdf.pdf")
        merger.close()
    else:
        print('Exiting PDF Merger')
        pass


def pdf_watermark():
    content_file = PyPDF2.PdfFileReader(open(content_pdf, 'rb'))
    wm_file = PyPDF2.PdfFileReader(open(wm_pdf, 'rb'))
    output = PyPDF2.PdfFileWriter()
    print(f'Adding watermark to --> ./{content_pdf}')
    for i in range(content_file.getNumPages()):
        page = content_file.getPage(i)
        page.mergePage(wm_file.getPage(0))
        output.addPage(page)

        with open('watermarked-output.pdf', 'wb') as file:
            output.write(file)

    print(f'Writing output file --> ./{file.name}')
    print('Process --> Completed successfully')


def rotate_pdf():
    with open('dummy.pdf', 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        page = reader.getPage(0)
        page.rotateCounterClockwise(90)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open('tilt.pdf', 'wb')as new_file:
            writer.write(new_file)


if __name__ == "__main__":
    # pdf_merger()
    pdf_watermark()
    # rotate_pdf()
