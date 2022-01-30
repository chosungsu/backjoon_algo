package java_version.문자열;

import java.util.Scanner;

public class q_2675 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int cnt = in.nextInt();
        for (int i = 0; i < cnt; i++) {
            int num = in.nextInt();
            String S = in.next();

            for (int j = 0; j < S.length(); j++) {
                for (int k = 0; k < num; k++) {
                    System.out.print(S.charAt(j));
                }
            }
            System.out.println();
        }
        
	}
}
