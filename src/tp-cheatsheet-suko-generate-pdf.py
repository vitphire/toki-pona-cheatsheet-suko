import os
from weasyprint import HTML

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def create_final_html(template_content, main_content):
    return template_content.replace('<!--CONTENT_PLACEHOLDER-->', main_content)

base_dir = os.path.dirname(os.path.abspath(__file__))
template_two_page = 'tp-cheatsheet-suko-index-2pg.html'
template_four_page = 'tp-cheatsheet-suko-index-4pg.html'
main_content_file = 'tp-cheatsheet-suko-index.html'
output_two_page_pdf = '../output/tp-cheatsheet-suko-2pg.pdf'
output_four_page_pdf = '../output/tp-cheatsheet-suko-4pg.pdf'

main_content = read_file(main_content_file)

for template_path, output_pdf in [(template_two_page, output_two_page_pdf), (template_four_page, output_four_page_pdf)]:
    template_content = read_file(template_path)
    final_html_content = create_final_html(template_content, main_content)
    HTML(string=final_html_content, base_url=base_dir).write_pdf(output_pdf)

(output_two_page_pdf, output_four_page_pdf)