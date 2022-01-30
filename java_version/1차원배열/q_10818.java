package java_version;

import java.util.Arrays;
import java.util.Scanner;

//최소, 최대 구하기
public class q_10818 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        //저장할 배열 선정
        int[] arr = new int[x];
        for (int i = 0; i < x; i++) {        
            arr[i] = sc.nextInt();
        }
        //배열 정렬
        Arrays.sort(arr);
        System.out.print(arr[0] + " " + arr[x - 1]);
	}
}
