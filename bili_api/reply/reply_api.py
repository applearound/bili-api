import datetime
import re

import bs4
import requests

VIDEO_API = "https://www.bilibili.com/video"
HOT_REPLY_API = "https://api.bilibili.com/x/v2/reply"
AV_PATTERN = re.compile(".*window.__INITIAL_STATE__=\\{\"aid\":(\\d+).*")


def get_video_page_content(bv: str) -> str:
    return requests.get(VIDEO_API + "/BV" + bv).text


def bv_to_av(bv: str) -> int:
    if bv.startswith("BV") or bv.startswith("bv"):
        bv = bv[2:]
    else:
        raise ValueError("bv")

    html_content = get_video_page_content(bv)
    soup = bs4.BeautifulSoup(html_content, "html.parser")
    scripts = soup.find_all("script")
    for script in scripts:
        if not script:
            continue

        if not script.string:
            continue

        matcher = AV_PATTERN.match(script.string)
        if matcher:
            return int(matcher.group(1))

    raise RuntimeError("av not found")


def get_replies(av: int, page: int = 1, type: int = 1, sort: int = 0) -> dict:
    # type 1 热度
    # sort 0 时间排序
    # sort 2 热度排序
    query_params = {
        # "callback": "jQuery33103988324956513716_1618491819366",
        # "jsonp": "jsonp",
        "pn": page,
        "type": type,
        "oid": av,
        "sort": sort,
        "_": int(datetime.datetime.now().timestamp() * 1000)
    }

    return requests.get(HOT_REPLY_API, params=query_params).json()
