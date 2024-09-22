class Solution {
    public int longestWPI(int[] hours) {
        int maxInterval = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int preSum = 0;
        for (int i = 0; i < hours.length; i++) {
            preSum += hours[i] > 8 ? 1 : -1;
            if (preSum > 0) {
                maxInterval = i + 1;
            } else {
                map.putIfAbsent(preSum, i);// if does not existing, will push, otherwise do nothing
                if (map.containsKey(preSum - 1)) {
                    int j = map.get(preSum - 1);
                    int interval = i - j;
                    maxInterval = Math.max(maxInterval, interval);
                }
            }
        }
        return maxInterval;
    }
}