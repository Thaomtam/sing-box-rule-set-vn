# Sing Box Rule Set - Vietnamese

## Giới thiệu
Đây là một bộ tập luật dành cho ứng dụng Sing Box, được tối ưu hóa cho người dùng tiếng Việt để chặn các quảng cáo và các nội dung không mong muốn khác trên internet.

## Bộ tập luật
Bộ tập luật này bao gồm các tập luật sau:
```
{
    "route": {
        "rule_set": [
            {
                "tag": "Geosite-vn",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/block.srs",
                "download_detour": "proxy"
            },
            {
                "tag": "Adway",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/adway.srs",
                "download_detour": "proxy"
            },
            {
                "tag": "Black",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/black.srs",
                "download_detour": "proxy"
            },
            {
                "tag": "Yoyo",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/yoyo.srs",
                "download_detour": "proxy"
            },
            {
                "tag": "MVPS",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/MVPS.srs",
                "download_detour": "proxy"
            },
            {
                "tag": "Easylist",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/easylist.srs",
                "download_detour": "proxy"
            },
			{
                "tag": "Threat",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/threat.srs",
                "download_detour": "proxy"
            },
			{
                "tag": "Casino",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/casino.srs",
                "download_detour": "proxy"
            }
        ]
    }
}
```
# Block 

- **Geosite-vn Rule Set:** [Download](/../../raw/rule-set/block.srs).[Link](/../../raw/rule-set/block.json)
- **Adway Rule Set:** [Download](/../../raw/rule-set/adway.srs).[Link](/../../raw/rule-set/adway.json)
- **MVPS Rule Set:** [Download](/../../raw/rule-set/MVPS.srs).[Link](/../../raw/rule-set/MVPS.json)
- **Easylist Rule Set:** [Download](/../../raw/rule-set/black.srs).[Link](/../../raw/rule-set/easylist.json)
- **Yoyo Rule Set:** [Download](/../../raw/rule-set/yoyo.srs).[Link](/../../raw/rule-set/yoyo.json)
- **Black Rule Set:** [Download](/../../raw/rule-set/black.srs).[Link](/../../raw/rule-set/black.json)
- **Threat Rule Set:** [Download](/../../raw/rule-set/threat.srs).[Link](/../../raw/rule-set/threat.json)
- **Casino Rule Set:** [Download](/../../raw/rule-set/casino.srs).[Link](/../../raw/rule-set/casino.json)

## Usage
GIỮ GÌN SỰ SẠCH ĐẸP MÔI TRƯỜNG MẠNG
