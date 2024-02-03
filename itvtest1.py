import re
# 读取itvlist.txt文件，提取频道信息
channels = []
with open('itvlist.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            channel, address = line.split(',')
            channels.append((channel, address))
# 对频道进行排序
channels.sort()
# 自定义排序函数，提取频道名称中的数字并按数字排序
def channel_key(channel):
    match = re.search(r'\d+', channel)
    if match:
        return int(match.group())
    else:
        return float('inf')  # 返回一个无穷大的数字作为关键字

# 对频道进行排序
channels.sort(key=lambda x: channel_key(x[0]))

# 生成itvlist.m3ut文件
with open('itvlist.m3u', 'w', encoding='utf-8') as file:
   channel_counters = {}
    file.write('#EXTM3U\n')
    for result in results:
        channel, address, speed = result
        if 'CCTV' in channel:
            if channel in channel_counters:
                if channel_counters[channel] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="央视",{channel}\n{address}\n')
                    channel_counters[channel] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="央视",{channel}\n{address}\n')
                channel_counters[channel] = 1
        channel_counters = {}
    for result in results:
        channel, address, speed = result
        if '河南' in channel:
            if channel in channel_counters:
                if channel_counters[channel] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="河南",{channel}\n{address}\n')
                    channel_counters[channel] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="河南",{channel}\n{address}\n')
                channel_counters[channel] = 1
    channel_counters = {}
    for result in results:
        channel, address, speed = result
        if '卫视' in channel:
            if channel in channel_counters:
                if channel_counters[channel] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="卫视",{channel}\n{address}\n')
                    channel_counters[channel] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="卫视",{channel}\n{address}\n')
                channel_counters[channel] = 1
    channel_counters = {}
    for result in results:
        channel, address, speed = result
        if 'CCTV' not in channel and '卫视' not in channel  and '河南' not in channel and '测试' not in channel:
            if channel in channel_counters:
                if channel_counters[channel] >= result_counter:
                    continue
                else:
                    file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="其他",{channel}\n{address}\n')
                    channel_counters[channel] += 1
            else:
                file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="其他",{channel}\n{address}\n')
                channel_counters[channel] = 1

