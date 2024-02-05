import time
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import re


# 合并文件内容
file_contents = []
file_paths = ["itvlist.m3u", "witvlist.m3u"]  # 替换为实际的文件路径列表
for file_path in file_paths:
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()
        file_contents.append(content)

# 写入合并后的文件
with open("hnitv.m3u", "w", encoding="utf-8") as output:
    output.write('\n'.join(file_contents))
