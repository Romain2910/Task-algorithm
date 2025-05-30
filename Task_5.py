import heapq

class TransitNetwork:
    def __init__(self):
        self.network = {}

    def add_stop(self, stop):
        if stop not in self.network:
            self.network[stop] = []

    def add_route(self, from_stop, to_stop, time):
        self.add_stop(from_stop)
        self.add_stop(to_stop)
        self.network[from_stop].append((to_stop, time))
        self.network[to_stop].append((from_stop, time))

    def update_route_time(self, from_stop, to_stop, new_time):
        self._update_connection(from_stop, to_stop, new_time)
        self._update_connection(to_stop, from_stop, new_time)

    def _update_connection(self, from_stop, to_stop, new_time):
        self.network[from_stop] = [
            (stop, new_time if stop == to_stop else duration)
            for (stop, duration) in self.network[from_stop]
        ]

    def find_shortest_path(self, origin, destination):
        if origin not in self.network or destination not in self.network:
            return None, float('inf')

        min_distances = {stop: float('inf') for stop in self.network}
        previous_stop = {stop: None for stop in self.network}
        min_distances[origin] = 0
        priority_queue = [(0, origin)]

        while priority_queue:
            current_distance, current_stop = heapq.heappop(priority_queue)

            if current_stop == destination:
                break

            for neighbor, travel_time in self.network[current_stop]:
                distance = current_distance + travel_time
                if distance < min_distances[neighbor]:
                    min_distances[neighbor] = distance
                    previous_stop[neighbor] = current_stop
                    heapq.heappush(priority_queue, (distance, neighbor))

        path = []
        stop = destination
        while stop:
            path.insert(0, stop)
            stop = previous_stop[stop]

        return path, min_distances[destination]

def display_menu():
    print("\nPUBLIC TRANSPORT ROUTE PLANNER")
    print("1. Add a connection between two stops")
    print("2. Find a route between two stops")
    print("3. Update travel time between two stops")
    print("4. Show all connections")
    print("5. Exit")

def list_connections(network):
    print("\n--- Current Connections ---")
    for stop, connections in network.network.items():
        for neighbor, time in connections:
            print(f"{stop} <--> {neighbor} : {time} min")

if __name__ == "__main__":
    transport_map = TransitNetwork()

    while True:
        display_menu()
        user_choice = input("Choice: ")

        if user_choice == "1":
            stop_a = input("Enter the first stop: ")
            stop_b = input("Enter the second stop: ")
            try:
                travel_time = int(input("Travel time (in minutes): "))
                transport_map.add_route(stop_a, stop_b, travel_time)
                print("Connection added.")
            except ValueError:
                print("Invalid time input.")

        elif user_choice == "2":
            origin = input("Start stop: ")
            destination = input("Destination stop: ")
            route, total_time = transport_map.find_shortest_path(origin, destination)
            if route:
                print(f"Shortest path: {' -> '.join(route)} (Total time: {total_time} min)")
            else:
                print("One or more stops are unknown.")

        elif user_choice == "3":
            stop_a = input("Enter the first stop: ")
            stop_b = input("Enter the second stop: ")
            try:
                updated_time = int(input("New travel time (in minutes): "))
                transport_map.update_route_time(stop_a, stop_b, updated_time)
                print("Travel time updated.")
            except ValueError:
                print("Invalid time input.")
            except KeyError:
                print("Unknown stop or missing connection.")

        elif user_choice == "4":
            list_connections(transport_map)

        elif user_choice == "5":
            print("Exiting the program. Have a nice day!")
            break

        else:
            print("Invalid choice. Please try again.")