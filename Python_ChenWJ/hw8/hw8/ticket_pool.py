import random
import time
import threading

class TicketPool:
    def __init__(self, initial: int):
        if initial < 0:
            raise ValueError("Initial tickets must be non-negative")
        self._rest = initial # 剩余票数量
        self._cond = threading.Condition() # 条件变量,用于第二小题

    def get_rest(self) -> int:
        # 查询当前剩余票数
        trest = self._rest
        time.sleep(random.random() * 0.02)
        return trest

    def reduce_rest(self, delta: int) -> None:
        # 减少剩余票数,即抢票
        if delta < 0:
            raise ValueError("Delta must be non-negative")
        time.sleep(random.random() * 0.02)
        self._rest -= delta

    def add_rest(self, delta: int) -> None:
        # 增加剩余票数,即退票
        if delta < 0:
            raise ValueError("Delta must be non-negative")
        time.sleep(random.random() * 0.02)
        self._rest += delta
    
    def get_condition(self) -> threading.Condition:
        # 获取Condition,用于第二小题
        return self._cond