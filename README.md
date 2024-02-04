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
            }
        ]
    }
}
```
