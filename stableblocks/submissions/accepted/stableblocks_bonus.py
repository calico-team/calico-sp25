from bisect import bisect
from functools import cache


def solve(N: int, X0: list[int], Y0: list[int], X1: list[int], Y1: list[int]) -> bool:
    # group blocks together by their vertical position
    groups = {}
    for i in range(N):
        if Y0[i] not in groups:
            groups[Y0[i]] = []
        groups[Y0[i]].append((X0[i], i))
    
    # sort blocks within each group by their horizontal position
    for bottoms in groups.values():
        bottoms.sort()
    
    @cache
    def blocks_resting_on_block(i):
        nonlocal groups
        
        if Y1[i] not in groups:
            return []
        candidates = groups[Y1[i]]
        
        resting_blocks = []
        for index in range(bisect(candidates, (X1[i], -1)) - 1, -1, -1):
            _, j = candidates[index]
            if X1[j] < X0[i]:
                break
            resting_blocks.append(j)
        
        return resting_blocks
    
    @cache
    def mass_of_block(i):
        return (X1[i] - X0[i]) * (Y1[i] - Y0[i])
    
    @cache
    def relevant_mass_of_block(i):
        mass = mass_of_block(i)
        for j in blocks_resting_on_block(i):
            mass += relevant_mass_of_block(j)
        return mass
    
    @cache
    def center_of_mass_of_block(i):
        return (X0[i] + X1[i]) / 2, (Y0[i] + Y1[i]) / 2
    
    @cache
    def relevant_center_of_mass_of_block(i):
        x_center_i, y_center_i = center_of_mass_of_block(i)
        mass_i = mass_of_block(i)
        
        x_centers, y_centers, masses = [x_center_i], [y_center_i], [mass_i]
        for j in blocks_resting_on_block(i):
            x_center_j, y_center_j = relevant_center_of_mass_of_block(j)
            mass_j = relevant_mass_of_block(j)
            x_centers.append(x_center_j)
            y_centers.append(y_center_j)
            masses.append(mass_j)
        
        x = sum(x * m for x, m in zip(x_centers, masses)) / sum(masses)
        y = sum(y * m for y, m in zip(x_centers, masses)) / sum(masses)
        
        return x, y
        
    for i in range(N):
        for j in blocks_resting_on_block(i):
            x, y = relevant_center_of_mass_of_block(j)
            if not X0[i] < x < X1[i]:
                return False
    
    return True


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        X0, Y0, X1, Y1 = zip(*(map(int, input().split()) for _ in range(N)))
        if solve(N, X0, Y0, X1, Y1):
            print('Stable')
        else:
            print('Unstable')


if __name__ == '__main__':
    main()
