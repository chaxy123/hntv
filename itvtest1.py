import os
import re
import time
import threading
from queue import Queue
import requests
import eventlet
eventlet.monkey_patch()

# 读取itvlist.txt文件，提取频道信息
channels = []
with open('itvlist.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            channel_name, channel_url = line.split(',')
            channels.append((channel_name, channel_url))
# 对频道进行排序
channels.sort()
# 自定义排序函数，提取频道名称中的数字并按数字排序
def channel_name_key(channel_name):
    match = re.search(r'\d+', channel_name)
    if match:
        return int(match.group())
    else:
        return float('inf')  # 返回一个无穷大的数字作为关键字

# 对频道进行排序
channels.sort(key=lambda x: channel_name_key(x[0]))

# 生成itvlist.m3ut文件
with open('itvlist.m3u', 'w', encoding='utf-8') as file:
   channel_name_counters = {}
    file.write('#EXTM3U\n')
    for result in results:
        channel_name, channel_url, speed = result
        if 'CCTV' in channel_name:
            if channel_name in channel_name_counters:
                if channel_name_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="央视",{channel_name}\n{channel_url}\n')
                    channel_name_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="央视",{channel_name}\n{channel_url}\n')
                channel_name_counters[channel_name] = 1
        channel_name_counters = {}
    for result in results:
        channel_name, channel_url, speed = result
        if '河南' in channel_name:
            if channel_name in channel_name_counters:
                if channel_name_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="河南",{channel_name}\n{channel_url}\n')
                    channel_name_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="河南",{channel_name}\n{channel_url}\n')
                channel_name_counters[channel_name] = 1
    channel_name_counters = {}
    for result in results:
        channel_name, channel_url, speed = result
        if '卫视' in channel_name:
            if channel_name in channel_name_counters:
                if channel_name_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="卫视",{channel_name}\n{channel_url}\n')
                    channel_name_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="卫视",{channel_name}\n{channel_url}\n')
                channel_name_counters[channel_name] = 1
    channel_name_counters = {}
    for result in results:
        channel_name, channel_url, speed = result
        if 'CCTV' not in channel_name and '卫视' not in channel_name  and '河南' not in channel_name and '测试' not in channel_name:
            if channel_name in channel_name_counters:
                if channel_name_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="其他",{channel_name}\n{channel_url}\n')
                    channel_name_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="其他",{channel_name}\n{channel_url}\n')
                channel_name_counters[channel_name] = 1

