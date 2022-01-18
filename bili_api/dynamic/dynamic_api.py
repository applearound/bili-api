from collections import deque

import requests


class Dynamics:
    def __init__(self, uid: int) -> None:
        self.__uid = uid

    def __iter__(self):
        return DynamicIter(self.__uid)


class DynamicIter():
    URL = "https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history"

    def __init__(self, uid: int) -> None:
        self.__cache = deque()
        self.__params = {
            "visitor_uid": 0,
            "host_uid": uid,
            "offset_dynamic_id": "0",
            "need_top": 0,
            "platform": "web",
        }

    def __next__(self):
        if len(self.__cache) != 0:
            return self.__cache.popleft()
        else:
            response_json = requests.get(url=self.URL,
                                         params=self.__params).json()

            data = response_json["data"]
            if not data["has_more"]:
                raise StopIteration()

            next_offset = data["next_offset"]
            for card in data["cards"][1:]:
                self.__cache.append(card)
                if card["desc"]["dynamic_id"] == next_offset:
                    self.__params["offset_dynamic_id"] = card["desc"][
                        "dynamic_id_str"]

            return data["cards"][0]
