package java_version;

import java.util.Scanner;

public class q_2798 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n, m;
        n = sc.nextInt();
        m = sc.nextInt();
        int sum = 0;
        int card[] = new int[n];

        for (int i = 0; i < n; i++) {
            card[i] = sc.nextInt();
        }
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    if (card[i] + card[j] + card[k] <= m && m - (card[i] + card[j] + card[k]) < m - sum) {
                        sum = card[i] + card[j] + card[k];
                    }
                }
            }
        }
        
        System.out.println(sum);
        
    }
}
