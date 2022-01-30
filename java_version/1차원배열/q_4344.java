package java_version;

import java.util.Scanner;

public class q_4344 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        //전체 케이스 수
		int x = in.nextInt();
        int[] arr;
		for (int i = 0; i < x; i++) {
            //학생수
            int N = in.nextInt();
            arr = new int[N];

            double sum = 0;
            for (int j = 0; j < N; j++) {
                int val = in.nextInt();
                arr[j] = val;
                sum += val;
            }
            double mean = (sum / N);
            double cnt = 0;
            for (int j = 0; j < N; j++) {
                if (arr[j] > mean) {
                    cnt++;
                }
            }
            System.out.printf("%.3f%%\n", (cnt/N) * 100);
		}
	}
}
