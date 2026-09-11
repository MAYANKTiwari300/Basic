public class KadaneAlgorithm {
    // Function to implement Kadane's Algorithm
    public static int maxSubArraySum(int[] arr) {
        int maxSoFar = arr[0];   // Initialize with first element
        int currentMax = arr[0]; // Current maximum sum

        for (int i = 1; i < arr.length; i++) {
            // Either extend the previous subarray or start a new one
            currentMax = Math.max(arr[i], currentMax + arr[i]);
            maxSoFar = Math.max(maxSoFar, currentMax);
        }

        return maxSoFar;
    }

    public static void main(String[] args) {
        int[] arr = {-2, -3, 4, -1, -2, 1, 5, -3};
        int maxSum = maxSubArraySum(arr);
        System.out.println("Maximum Subarray Sum is: " + maxSum);
    }
}

