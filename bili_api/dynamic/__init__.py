r"""
{
    "code": int, 返回码，正常为0
    "msg": str, 返回消息
    "message": str, 返回消息
    "data": {
        "has_more": int, 是否有更多的动态
        "cards": [], 详细动态
        "next_offset": int, 下一个动态id
        "_gt_": int，未知
    }
}

card {
    "desc": {},
    "card": str,
    "extend_json": str,
    "extra": {},
    "display": {}
}

desc {
    "uid": int,
    "type": int,
    "rid": int,
    "acl": int,
    "view": int,
    "repost": int,
    "comment": int,
    "like": int,
    "is_liked": int,
    "dynamic_id": int,
    "timestamp": int,
    "pre_dy_id": int,
    "orig_dy_id": int,
    "orig_type": int,
    "user_profile": {},
    "uid_type": int,
    "stype": int,
    "r_type": int,
    "inner_id": int,
    "status": int,
    "dynamic_id_str": str,
    "pre_dy_id_str": str,
    "orig_dy_id_str": str,
    "rid_str": str,
    "origin": {}
}

extra {
    "is_space_top": int
}

display {
    "emoji_info": {}
    "origin": {},
    "relation": {},
    "comment_info": {},
    "add_on_card_info": []
}

origin {
    "topic_info": {
        "topic_details": []
    },
    "relation": {},
    "show_tip": {}
}

topic_detail {
    "topic_id": int,
    "topic_name": str,
    "is_activity": int,
    "topic_link": str
}

relation {
    "status": int,
    "is_follow": int,
    "is_followed": int
}

show_tip {
    "del_tip": str
}

comment_info {
    "comments": [],
    "comment_ids": str
}

comment {
    "uid": int,
    "name": str,
    "content": str
}
"""
