import os
import markdown
from weasyprint import HTML

def generate_pdf():
    file = '';
    if(len(sys.argv) == 2):
        file = sys.argv[1]

    html_content = ""
    if os.path.exists(file+'.html'):
        print('read file '+file+'.html')
        with open(file+'.html', "r", encoding="utf-8") as f:
            html_content = f.read()

    if(len(html_content) == 0):
        print('nothing generated')
    else:
        filename = file+".pdf"

        # Generation PDF avec WeasyPrint
        HTML(string=html_content).write_pdf(filename)
        print(f"PDF généré avec succès : {filename}")

if __name__ == "__main__":
    generate_pdf()
