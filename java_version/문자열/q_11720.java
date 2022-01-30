package java_version.문자열;

import java.util.Scanner;

public class q_11720 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int ch = in.nextInt();
        String a = in.next();
        int sum = 0;
        for (int i = 0; i < ch; i++) {
            sum += a.charAt(i) - '0';
        }
        System.out.println(sum);
	}
}
