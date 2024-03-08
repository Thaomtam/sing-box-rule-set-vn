# Sing Box Rule Set - Vietnamese

## Giới thiệu
Đây là một bộ tập luật dành cho ứng dụng Sing Box, được tối ưu hóa cho người dùng tiếng Việt để chặn các quảng cáo và các nội dung không mong muốn khác trên internet.

## Bộ tập luật

### Tập luật chặn quảng cáo
Bộ tập luật này chứa các quy tắc để chặn quảng cáo và các nội dung không mong muốn.

- **Geosite-vn Rule Set:** [Download](/../../raw/rule-set/block.srs) | [Link](/../../raw/rule-set/block.json)
- **Adway Rule Set:** [Download](/../../raw/rule-set/adway.srs) | [Link](/../../raw/rule-set/adway.json)
- **MVPS Rule Set:** [Download](/../../raw/rule-set/MVPS.srs) | [Link](/../../raw/rule-set/MVPS.json)
- **Easylist Rule Set:** [Download](/../../raw/rule-set/easylist.srs) | [Link](/../../raw/rule-set/easylist.json)
- **Yoyo Rule Set:** [Download](/../../raw/rule-set/yoyo.srs) | [Link](/../../raw/rule-set/yoyo.json)
- **d3host Rule Set:** [Download](/../../raw/rule-set/d3host.srs) | [Link](/../../raw/rule-set/d3host.json)
- **Black Rule Set:** [Download](/../../raw/rule-set/black.srs) | [Link](/../../raw/rule-set/black.json)
- **Anudeep Rule Set:** [Download](/../../raw/rule-set/anudeep.srs) | [Link](/../../raw/rule-set/anudeep.json)
- **Xiaomi-ads Rule Set:** [Download](/../../raw/rule-set/xiaomi.srs) | [Link](/../../raw/rule-set/xiaomi.json)
- **Dan-ads Rule Set:** [Download](/../../raw/rule-set/dan.srs) | [Link](/../../raw/rule-set/dan.json)
- **Spam404 Rule Set:** [Download](/../../raw/rule-set/spam404.srs) | [Link](/../../raw/rule-set/spam404.json)
- **Kninja Rule Set:** [Download](/../../raw/rule-set/Kninja.srs) | [Link](/../../raw/rule-set/Kninja.json)
- **Facebook Rule Set:** [Download](/../../raw/rule-set/Facebook.srs) | [Link](/../../raw/rule-set/Facebook.json)
- **Redirect Rule Set:** [Download](/../../raw/rule-set/Redirect.srs) | [Link](/../../raw/rule-set/Redirect.json)
- **Abpvn Rule Set:** [Download](/../../raw/rule-set/abpvn.srs) | [Link](/../../raw/rule-set/abpvn.json)

### Tập luật chặn các loại nội dung cụ thể
Bộ tập luật này chứa các quy tắc để chặn các loại nội dung cụ thể như mạng đen, trò chơi cá cược và các trang web quảng cáo.

- **Threat Rule Set:** [Download](/../../raw/rule-set/threat.srs) | [Link](/../../raw/rule-set/threat.json) (*Chặn các trang web đe dọa*)
- **Casino Rule Set:** [Download](/../../raw/rule-set/casino.srs) | [Link](/../../raw/rule-set/casino.json) (*Chặn các trang web trò chơi cá cược*)

### Tập luật chặn quảng cáo từ các máy chủ quảng cáo
Bộ tập luật này chứa các quy tắc để chặn quảng cáo từ các máy chủ quảng cáo đã biết.

- **Adservers Rule Set:** [Download](/../../raw/rule-set/adservers.srs) | [Link](/../../raw/rule-set/adservers.json) (*Chặn các máy chủ quảng cáo*)

*Ghi chú: Việc sử dụng các bộ tập luật này giúp giữ gìn sự sạch đẹp môi trường mạng bằng cách chặn các quảng cáo và các nội dung không mong muốn khác trên internet.*
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
            },
            {
                "tag": "Adservers",
                "type": "remote",
                "format": "binary",
                "url": "https://raw.githubusercontent.com/thaomtam/sing-box-rule-set-vn/rule-set/adservers.srs",
                "download_detour": "proxy"
            }
        ]
    }
}
```
