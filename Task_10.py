import time
import heapq
from collections import deque
from dataclasses import dataclass, field

@dataclass(order=True)
class ChatMessage:
    priority: int
    timestamp: float = field(compare=False)
    from_user: str = field(compare=False)
    to_user: str = field(compare=False)
    body: str = field(compare=False)

class MessagingSystem:
    def __init__(self):
        self.regular_messages = deque()
        self.urgent_messages = []

    def enqueue_message(self, from_user: str, to_user: str, body: str, is_urgent=False):
        timestamp = time.time()
        priority = 0 if is_urgent else 1
        message = ChatMessage(priority=priority, timestamp=timestamp, from_user=from_user, to_user=to_user, body=body)
        if is_urgent:
            heapq.heappush(self.urgent_messages, message)
            print(f"URGENT message sent from {from_user} to {to_user}: \"{body}\"")
        else:
            self.regular_messages.append(message)
            print(f"Standard message sent from {from_user} to {to_user}: \"{body}\"")

    def process_next_message(self):
        if self.urgent_messages:
            message = heapq.heappop(self.urgent_messages)
            print(f"Delivering URGENT message from {message.from_user} to {message.to_user}: {message.body}")
        elif self.regular_messages:
            message = self.regular_messages.popleft()
            print(f"Delivering message from {message.from_user} to {message.to_user}: {message.body}")
        else:
            print("No messages to process.")

def run_messaging_app():
    system = MessagingSystem()
    print("Welcome to the Priority Messaging System.")

    while True:
        print("\nSelect an action:")
        print("1. Send a message")
        print("2. Deliver next message")
        print("3. Exit")

        option = input("Your choice (1/2/3): ").strip()

        if option == "1":
            sender = input("Sender: ").strip()
            recipient = input("Recipient: ").strip()
            message_text = input("Message: ").strip()
            urgent_input = input("Is it urgent? (yes/no): ").strip().lower()
            is_urgent = urgent_input in ["yes", "y"]
            system.enqueue_message(sender, recipient, message_text, is_urgent)

        elif option == "2":
            system.process_next_message()

        elif option == "3":
            print("Shutting down.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    run_messaging_app()
