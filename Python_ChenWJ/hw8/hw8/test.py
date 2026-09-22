import random
import time
from ticket_pool import TicketPool

# 加载数据
def load_ticket_class(problem_id: int):
    if problem_id == 1:
        from t1 import Ticket as Ticket
    elif problem_id == 2:
        from t2 import TicketBuyer as Ticket
    else:
        raise ValueError("Invalid problem ID")
    return Ticket

# 小题1测试
def test_basic(problem_id: int, tot_tickets: int, num_customers: int) -> bool:
    Ticket = load_ticket_class(problem_id)
    pool = TicketPool(tot_tickets)
    avg = tot_tickets / num_customers if num_customers > 0 else 0
    customers = []
    total_req = 0

    for _ in range(num_customers):
        req = round((random.random() / 2 + 1) * avg)
        customers.append(Ticket(pool, req))
        total_req += req

    for c in customers:
        c.start()
    for c in customers:
        c.join()

    actual = sum(c.get_obtained() for c in customers)
    rest = pool.get_rest()
    expected_actual = min(total_req, tot_tickets)
    expected_rest = max(0, tot_tickets - total_req)

    return (
        actual == expected_actual and
        rest == expected_rest and
        rest >= 0 and actual <= tot_tickets
    )

# 小题2测试
def test_with_refund(problem_id: int, tot_tickets: int, num_buyers: int, num_refunders: int) -> bool:
    from t2 import TicketRefunder
    TicketBuyer = load_ticket_class(problem_id)

    pool = TicketPool(tot_tickets)
    buyers = []
    refunders = []
    total_buy_req = 0

    for i in range(num_buyers):
        req = 3 + random.randint(0, 2)
        buyers.append(TicketBuyer(pool, req, name=f"buyer-{i}"))
        total_buy_req += req

    for i in range(num_refunders):
        refund = 10 + random.randint(0, 5)
        refunders.append(TicketRefunder(pool, refund, name=f"refunder-{i}"))

    for b in buyers:
        b.start()
    time.sleep(1)

    for r in refunders:
        r.start()

    for b in buyers:
        b.join(timeout=2.0)
        if b.is_alive():
            return False
        
    for r in refunders:
        r.join(timeout=1.0)

    total_obtained = sum(b.get_obtained() for b in buyers)
    final_rest = pool.get_rest()
    total_refunded = sum(r.num for r in refunders)
    expected_total_available = tot_tickets + total_refunded

    if total_obtained > expected_total_available:
        return False

    if final_rest != expected_total_available - total_obtained:
        return False

    if not all(0 <= b.get_obtained() <= b.num for b in buyers):
        return False

    return True

# 主函数
def main():
    random.seed(42)
    print("=== Testing Problem 1 ===")
    basic_cases = [
        (30,1), 
        (100,5),
        (300,10), 
        (500,30), 
        (3000,100)
    ]
    all_pass = True
    for tot_t, num_c in basic_cases:
        ok = test_basic(1, tot_t, num_c)
        print(f"Case ({tot_t}, {num_c}): {'Accept' if ok else 'Wrong Answer'}")
        if not ok:
            all_pass = False

    print("=== Testing Problem 2 ===")
    basic_cases = [
        (10, 1, 1),
        (0, 2, 1),
        (0, 5, 3),
        (5, 4, 2),
        (10, 10, 5)
    ]
    for tot_t, num_b, num_r in basic_cases:
        ok = test_with_refund(2, tot_t, num_b, num_r)
        print(f"Case ({tot_t}, {num_b}, {num_r}): {'Accept' if ok else 'Wrong Answer'}")
        if not ok:
            all_pass = False
   
    print("\n" + "="*40)
    if all_pass:
        print("All tests passed!")
    else:
        print("Some tests failed.")

if __name__ == "__main__":
    main()