import os
from bs4 import BeautifulSoup

def analyze_html_files():
    # current_directory = os.getcwd()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    resource_directory = os.path.join(current_directory, '../..', 'resource')

    html_files = [file for file in os.listdir(resource_directory) if file.endswith('.html')]
    urls = []
    for file_name in html_files:
        file_path = os.path.join(resource_directory, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            html = file.read()
            soup = BeautifulSoup(html, 'html.parser')
            href_values = []
            for a_tag in soup.find_all('a'):
                href = a_tag.get('href')
                if href:
                    href_values.append(href)
            if href_values:
                urls.extend(href_values)
    
    # Add prefix to URLs
    prefix = 'https://docs.aws.amazon.com/apigateway/latest/api/'
    urls_with_prefix = [prefix + url for url in urls]
    
   # Write URLs to the specified file
    output_file = os.path.join(resource_directory, 'urls.txt')
    output_directory = os.path.dirname(output_file)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        for url in urls_with_prefix:
            file.write(f"{url}\n")


if __name__ == '__main__':
    analyze_html_files()