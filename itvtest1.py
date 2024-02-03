import os
import re
import time
import threading
from queue import Queue
import requests
import eventlet
eventlet.monkey_patch()

# 线程安全的队列，用于存储下载任务
task_queue = Queue()

# 线程安全的列表，用于存储结果
results = []

channels = []
error_channels = []

with open("itvlist.txt", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            channel_name, channel_url = line.split(',')
            channels.append((channel_name, channel_url))

# 定义工作线程函数



# 创建多个工作线程
num_threads = 10
for _ in range(num_threads):
    t = threading.Thread(target=worker, daemon=True)  # 将工作线程设置为守护线程
    t.start()

# 添加下载任务到队列
for channel in channels:
    task_queue.put(channel)

# 等待所有任务完成
task_queue.join()


def channel_key(channel_name):
    match = re.search(r'\d+', channel_name)
    if match:
        return int(match.group())
    else:
        return float('inf')  # 返回一个无穷大的数字作为关键字

# 对频道进行排序
results.sort(key=lambda x: (x[0], -float(x[2].split()[0])))
results.sort(key=lambda x: channel_key(x[0]))

# 将结果写入文件
with open("itv_results1.txt", 'w', encoding='utf-8') as file:
    for result in results:
        channel_name, channel_url, speed = result
        file.write(f"{channel_name},{channel_url},{speed}\n")

with open("itv_speed1.txt", 'w', encoding='utf-8') as file:
    for result in results:
        channel_name, channel_url, speed = result
        file.write(f"{channel_name},{channel_url}\n")


result_counter = 5  # 每个频道需要的个数

with open("itvlist.m3u", 'w', encoding='utf-8') as file:
    channel_counters = {}
    file.write('#EXTM3U\n')
    for result in results:
        channel_name, channel_url, speed = result
        if 'CCTV' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="央视",{channel_name}\n{channel_url}\n')
                    channel_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="央视",{channel_name}\n{channel_url}\n')
                channel_counters[channel_name] = 1
        channel_counters = {}
    for result in results:
        channel_name, channel_url, speed = result
        if '河南' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="河南",{channel_name}\n{channel_url}\n')
                    channel_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="河南",{channel_name}\n{channel_url}\n')
                channel_counters[channel_name] = 1
    channel_counters = {}
    for result in results:
        channel_name, channel_url, speed = result
        if '卫视' in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="卫视",{channel_name}\n{channel_url}\n')
                    channel_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="卫视",{channel_name}\n{channel_url}\n')
                channel_counters[channel_name] = 1
    channel_counters = {}
    for result in results:
        channel_name, channel_url, speed = result
        if 'CCTV' not in channel_name and '卫视' not in channel_name  and '河南' not in channel_name and '测试' not in channel_name:
            if channel_name in channel_counters:
                if channel_counters[channel_name] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="其他",{channel_name}\n{channel_url}\n')
                    channel_counters[channel_name] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel_name}" tvg-logo="https://epg.112114.xyz/logo/{channel_name}.png" group-title="其他",{channel_name}\n{channel_url}\n')
                channel_counters[channel_name] = 1
