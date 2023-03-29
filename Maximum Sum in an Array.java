import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();

        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int[] arr = new int[n];

            for (int j = 0; j < n; j++) {
                arr[j] = scanner.nextInt();
            }

            // Compute maximum contiguous subarray using Kadane's algorithm
            int max_so_far = arr[0];
            int max_ending_here = arr[0];
            for (int j = 1; j < n; j++) {
                max_ending_here = Math.max(arr[j], max_ending_here + arr[j]);
                max_so_far = Math.max(max_so_far, max_ending_here);
            }
            int max_contiguous = max_so_far;

            // Compute maximum non-contiguous subarray
            int max_non_contiguous = 0;
            int max_negative = Integer.MIN_VALUE;
            boolean has_positive = false;
            for (int j = 0; j < n; j++) {
                if (arr[j] > 0) {
                    max_non_contiguous += arr[j];
                    has_positive = true;
                } else {
                    max_negative = Math.max(max_negative, arr[j]);
                }
            }
            if (!has_positive) {
                max_non_contiguous = max_negative;
            }

            System.out.println(max_contiguous + " " + max_non_contiguous);
        }

        scanner.close();
    }
}
