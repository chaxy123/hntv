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

# 生成iptv_list.m3u文件
with open('itvlist.m3u', 'w', encoding='utf-8') as file:
    file.write('#EXTM3U\n')
    for channel, address in channels:
        if 'cctv' in channel.lower():
            file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="央视",{channel}\n{address}\n')

    for channel, address in channels:
        if '河南' in channel:
            file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="河南",{channel}\n{address}\n')

    for channel, address in channels:
        if '卫视' in channel:
            file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="卫视",{channel}\n{address}\n')
    
    for channel, address in channels:
        if '凤凰' in channel:
            file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="香港",{channel}\n{address}\n')
    
    for channel, address in channels:
        if 'cctv' not in channel.lower() and '卫视' not in channel and '河南' not in channel and '凤凰' not in channel:
            file.write(f'#EXTINF:-1 tvg-id="{channel}" tvg-logo="https://epg.112114.xyz/logo/{channel}.png" group-title="其他",{channel}\n{address}\n')
