"""点赞状态追踪 —— 起始文件。

只用标准库。没有 web 框架,没有数据库。
实现下面两个方法。需求见 SPEC.md。
"""


class ReactionTracker:
    """追踪每个 target 当前有哪些用户处于「已点赞」状态。

    ``record`` 会被多个线程同时调用。
    """

    def __init__(self) -> None:
        raise NotImplementedError

    def record(
        self,
        event_id: str,
        user_id: str,
        target_id: str,
        kind: str,
        ts: int,
    ) -> None:
        """接收一条点赞事件。

        ``kind`` 是 ``"like"`` 或 ``"unlike"``。
        ``ts`` 是生产方打上的整数时间戳。

        事件可能以任意顺序到达,可能被投递多次,
        也可能以不同的 ``event_id`` 重复出现。
        """
        raise NotImplementedError

    def like_count(self, target_id: str) -> int:
        """``target_id`` 上当前处于已点赞状态的不同用户数。"""
        raise NotImplementedError
