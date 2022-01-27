package java_version;

import java.util.Scanner;

//총합 구하기
public class q_8393 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = 0;
        
        for (int i = 1; i <= x; i++) {
            y += i;
        }
        System.out.println(y);
	}
}
