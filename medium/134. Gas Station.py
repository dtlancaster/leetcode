class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        num_stations = len(gas)
        total_gas = 0
        current_gas = 0
        index = 0
        
        for i in range(num_stations):
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            if current_gas < 0:
                current_gas = 0
                index = i + 1
        return -1 if (total_gas < 0) else index
