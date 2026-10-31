

# Graph Work

class Graph:

    def __init__(self):
        # Dictionary to store locations and their roads
        self.graph = {}

    # Add a location (vertex)
    def add_location(self, location):
        if location not in self.graph:
            self.graph[location] = {}
            print(f"Location {location} added.")
        else:
            print(f"Location {location} already exists.")

    # Add an edge between two locations
    def add_road(self, source, destination, distance):
        if source not in self.graph or destination not in self.graph:
            print("Error: Both locations must exist first.")
            return

        if source == destination:
            print("Error: A road cannot connect a location to itself.")
            return

        if distance < 0:
            print("Error: Distance cannot be negative.")
            return

        # Store the road in both directions
        self.graph[source][destination] = distance
        self.graph[destination][source] = distance

        print(f"Road added: {source} <-> {destination}, {distance} km")

    # Display all locations and roads
    def display_graph(self):
        print("\nROUTEWISE ROAD NETWORK ")

        if not self.graph:
            print("No locations available.")
            return

        for location, roads in self.graph.items():
            print(f"{location} -> {roads}")

    # Display all locations
    def display_locations(self):
        print("\nAvailable locations:")

        for location in self.graph:
            print("-", location)

    # Show roads connected to a location
    def show_neighbours(self, location):
        if location not in self.graph:
            print("Location not found.")
            return

        print(f"\nRoads connected to {location}:")

        for neighbour, distance in self.graph[location].items():
            print(f"{location} -> {neighbour}: {distance} km")

    # Check whether two locations have a direct road
    def has_road(self, source, destination):
        if source not in self.graph:
            return False

        return destination in self.graph[source]

    # Get distance of a direct road
    def get_distance(self, source, destination):
        if self.has_road(source, destination):
            return self.graph[source][destination]

        return None

    # Calculate the distance of a given route
    def calculate_route_distance(self, route):
        total_distance = 0

        for i in range(len(route) - 1):
            source = route[i]
            destination = route[i + 1]

            distance = self.get_distance(source, destination)

            if distance is None:
                print(f"No direct road: {source} -> {destination}")
                return None

            total_distance += distance

        return total_distance



    # Find the shortest path using Dijkstra's algorithm
    def shortest_path(self, start, end):
        import heapq

        # Check whether both locations exist
        if start not in self.graph or end not in self.graph:
            print("Error: Location not found.")
            return None, None

        # Store distances from the starting location
        distances = {location: float("inf") for location in self.graph}
        distances[start] = 0

        # Store the previous location for each location
        previous = {location: None for location in self.graph}

        # Priority queue: (distance, location)
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current = heapq.heappop(priority_queue)

            # Skip an outdated distance
            if current_distance > distances[current]:
                continue

            # Stop when the destination is reached
            if current == end:
                break

            # Check all roads connected to current location
            for neighbour, road_distance in self.graph[current].items():
                new_distance = current_distance + road_distance

                # Update if a shorter route is found
                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    previous[neighbour] = current

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbour)
                    )

        # If no route exists
        if distances[end] == float("inf"):
            print("No route exists between these locations.")
            return None, None

        # Reconstruct the shortest route
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous[current]

        path.reverse()

        return path, distances[end]


# =====================================================
# Main Program: Create a Sample Road Network
# =====================================================

def main():
    road_network = Graph()

    # Add locations
    locations = ["A", "B", "C", "D", "E"]

    for location in locations:
        road_network.add_location(location)

    # Add roads and distances
    road_network.add_road("A", "B", 5)
    road_network.add_road("A", "C", 10)
    road_network.add_road("B", "C", 3)
    road_network.add_road("B", "D", 7)
    road_network.add_road("C", "D", 2)
    road_network.add_road("C", "E", 6)
    road_network.add_road("D", "E", 4)

    # Display the network
    road_network.display_graph()

    # Display available locations
    road_network.display_locations()

    # Display roads from one location
    road_network.show_neighbours("C")

    # Check a direct road
    print("\nIs there a direct road from A to B?")
    print(road_network.has_road("A", "B"))

    # Get a direct road's distance
    print("\nDirect distance from A to B:")
    print(road_network.get_distance("A", "B"), "km")

    # Calculate a route's distance
    sample_route = ["A", "B", "C", "D"]
    distance = road_network.calculate_route_distance(sample_route)

    print(f"\nRoute: {' -> '.join(sample_route)}")

    if distance is not None:
        print(f"Total route distance: {distance} km")


if __name__ == "__main__":
    main()
