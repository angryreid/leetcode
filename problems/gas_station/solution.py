class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remain_gas = 0
        for i in range(n):
            remain_gas += gas[i] - cost[i]

        if remain_gas < 0:
            return -1
        
        current_gas = 0
        start = 0
        i = 0
        while i < n:
            current_gas += gas[i] - cost[i]

            if current_gas >= 0:
                i += 1
            else:
                current_gas = 0
                i += 1
                start = i
        return start


        