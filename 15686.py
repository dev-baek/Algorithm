from itertools import combinations

def chicken_distance(houses, chicken_stores, m):
    chicken_min_distance = float('inf')

    for selected_stores in combinations(chicken_stores, m):
        total_distance = 0
        for hx, hy in houses:
            house_min_distance = min(abs(hx - cx) + abs(hy - cy) for cx, cy in selected_stores)
            total_distance += house_min_distance
        chicken_min_distance = min(chicken_min_distance, total_distance)
    
    return chicken_min_distance

def find_houses_and_stores(city):
    houses = []
    chicken_stores = []
    for i in range(len(city)):
        for j in range(len(city[0])):
            if city[i][j] == 1:
                houses.append((i, j))
            elif city[i][j] == 2:
                chicken_stores.append((i, j))
    
    return houses, chicken_stores

if __name__ == "__main__":
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    houses, chicken_stores = find_houses_and_stores(city)
    print(chicken_distance(houses, chicken_stores, m))