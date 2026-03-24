# Power Grid Failure Analyzer 

def dfs(grid, node, visited):
    visited.add(node)
    for neighbor in grid[node]:
        if neighbor not in visited:
            dfs(grid, neighbor, visited)


def show_grid(grid):
    print("\nCurrent Power Grid:")
    for node in grid:
        print(f"{node} → {grid[node]}")


def analyze_failure(grid):
    start = input("\nEnter failed station: ")

    if start not in grid:
        print("Invalid station!")
        return

    affected = set()
    dfs(grid, start, affected)

    print("\n🚨 Affected Stations:")
    for a in affected:
        print("-", a)

    print(f"\nTotal affected: {len(affected)}")


def find_critical_nodes(grid):
    print("\n🔍 Finding Critical Stations...\n")

    impact = {}

    for node in grid:
        affected = set()
        dfs(grid, node, affected)
        impact[node] = len(affected)

    sorted_nodes = sorted(impact.items(), key=lambda x: x[1], reverse=True)

    print("Stations ranked by impact:")
    for node, count in sorted_nodes:
        print(f"{node}: affects {count} nodes")


def add_connection(grid):
    a = input("From station: ")
    b = input("To station: ")

    if a not in grid:
        grid[a] = []
    if b not in grid:
        grid[b] = []

    grid[a].append(b)
    print("Connection added!")


# initial grid
grid = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": ["F"],
    "F": []
}


while True:
    print("\n⚡ POWER GRID ANALYZER")
    print("1. Show Grid")
    print("2. Simulate Failure")
    print("3. Find Critical Stations")
    print("4. Add Connection")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_grid(grid)

    elif choice == "2":
        analyze_failure(grid)

    elif choice == "3":
        find_critical_nodes(grid)

    elif choice == "4":
        add_connection(grid)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
