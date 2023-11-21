import os
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import re
from collections import Counter

# response html
async def download_webpage(session, url):
    async with session.get(url) as response:
        return await response.text()

# 解析 web
def parse_webpage(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    return text

# 文本处理
def process_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    return text

# count
def count_word_frequency(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts

# 网页处理
async def process_url(session, url):
    html = await download_webpage(session, url)
    text = parse_webpage(html)
    processed_text = process_text(text)
    word_frequencies = count_word_frequency(processed_text)
    return word_frequencies

# 爬虫
async def web_crawler(urls):
    word_frequencies = Counter()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(process_url(session, url))
            tasks.append(task)
        
        # 并发地执行所有任务
        results = await asyncio.gather(*tasks)
        
        # 合并所有单词频率结果
        for result in results:
            word_frequencies += Counter(result)
    
    return word_frequencies

if __name__ == '__main__':
    current_directory = os.path.dirname(os.path.abspath(__file__))
    resource_directory = os.path.join(current_directory, '..', 'resource')
# 从外部文件读取URL列表
    input_file = resource_directory + '/urls.txt'  # 输入文件名
    urls = []
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                urls.append(line)

    loop = asyncio.get_event_loop()
    word_frequencies = loop.run_until_complete(web_crawler(urls))
    loop.close()

    output_file = resource_directory + '/word_frequencies.txt'  # 输出文件名
    with open(output_file, 'w', encoding='utf-8') as file:
        sorted_word_frequencies = dict(sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True))
        for word, frequency in sorted_word_frequencies.items():
            file.write(f'{word}: {frequency}\n')

    print('Word frequencies have been written to the output file.')