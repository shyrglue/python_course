import threading
from ticket_pool import TicketPool


class Ticket(threading.Thread):
    # TODO: 你可能需要在这里定义所有线程共享的锁
    lock = threading.Lock()

    def __init__(self, ticket_pool: TicketPool, num: int):
        """
            构造函数
            :param ticket_pool: 票池TicketPool类的对象
            :param num: 本线程要抢的票数
        """
        super().__init__()
        self.ticket_pool = ticket_pool
        self.num = num
        self._obtained = 0

    def run(self):
        """
            抢票过程(必须在锁的保护下完成):
            查询票池中剩余的票数
            如果剩余票数不少于要抢的票数 则在票池中抢走需要的票数
            如果剩余票数小于需要的票数 则在票池中抢走剩余的票数
        """
        # TODO: 在锁的保护下，实现抢票逻辑
        Ticket.lock.acquire()
        GRAB = min(self.ticket_pool.get_rest(), self.num)
        if GRAB > 0:
            self.ticket_pool.reduce_rest(GRAB)
            self._obtained = GRAB
        Ticket.lock.release()

    def get_obtained(self) -> int:
        """返回实际抢到的票的数量"""
        return self._obtained