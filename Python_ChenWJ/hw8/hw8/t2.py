import threading
from ticket_pool import TicketPool


class TicketBuyer(threading.Thread):
    def __init__(self, ticket_pool: TicketPool, num: int, name: str = None):
        """
            构造函数
            :param ticket_pool: 票池TicketPool类的对象
            :param num: 本线程要抢的票数
        """
        super().__init__(name=name)
        self.ticket_pool = ticket_pool
        self.num = num
        self._obtained = 0

    def run(self):
        """
            抢票过程(必须在Condition的保护下完成):
            查询票池中剩余的票数
            若当前余票为0 则陷入阻塞等待
            若当前存在余票 则抢走min(剩余票数, 还需抢票的数量)张票
            成功抢到票后 需唤醒正在等待的其他抢票者(线程)
            直到实际抢到的票达到本线程要抢的票数
        """
        # TODO: 实现抢票逻辑
        COND = self.ticket_pool.get_condition()
        COND.acquire()
        while self._obtained < self.num:
            REST = self.ticket_pool.get_rest()
            if not REST:
                COND.wait()
            else:
                NEED = self.num - self._obtained
                GRAB = min(REST, NEED)
                self.ticket_pool.reduce_rest(GRAB)
                self._obtained += GRAB
                COND.notify_all()
        COND.release()
    
    def get_obtained(self) -> int:
        """返回实际抢到的票的数量"""
        return self._obtained


class TicketRefunder(threading.Thread):
    def __init__(self, ticket_pool: TicketPool, num: int, name: str = None):
        """
            构造函数
            :param ticket_pool: 票池TicketPool类的对象
            :param num: 本线程要退的票数
        """
        super().__init__(name=name)
        self.ticket_pool = ticket_pool
        self.num = num

    def run(self):
        """
            退票过程(必须在Condition的保护下完成):
            退票 并唤醒所有等待中的抢票者
        """
        # TODO: 实现退票逻辑
        COND = self.ticket_pool.get_condition()
        COND.acquire()
        self.ticket_pool.add_rest(self.num)
        COND.notify_all()
        COND.release()