import threading
import time


semaphore = threading.Semaphore(5)


def ticketShop(customer):
    print(f"Welcome {customer} to Ticket Shop!")
    semaphore.acquire()
    print(f"{customer} occupied place for ticket")
    time.sleep(5)
    semaphore.release()


customer_names = [
    "Olivia", "Ethan", "Sofia", "Liam", "Ava",
    "Noah", "Emma", "Jackson", "Mia", "Lucas",
    "Isabella", "Aiden", "Charlotte", "Mason", "Harper"
]

threads = [threading.Thread(target=ticketShop, args=(customer,)) for customer in customer_names]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("All customers have bought their tickets. The ticket shop is now closed.")