class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Get the number of gas stations
        n = len(gas)
        
        # Initialize the total remaining gas after completing the circuit
        remain_gas = 0
        # Calculate the total remaining gas after visiting each station
        for i in range(n):
            remain_gas += gas[i] - cost[i]

        # If the total remaining gas is negative, it's impossible to complete the circuit
        if remain_gas < 0:
            return -1
        
        # Initialize the current gas in the tank and the starting station index
        current_gas = 0
        start = 0
        i = 0
        # Traverse the gas stations
        while i < n:
            # Update the current gas in the tank after visiting the i-th station
            current_gas += gas[i] - cost[i]

            # If the current gas is non-negative, move to the next station
            if current_gas >= 0:
                i += 1
            else:
                # If the current gas is negative, reset the current gas
                # and set the next station as the new starting point
                current_gas = 0
                i += 1
                start = i
        
        # Return the starting station index
        return start