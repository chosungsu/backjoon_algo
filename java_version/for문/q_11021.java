package java_version.for문;

import java.util.Scanner;

public class q_11021 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        
        for (int i = 1; i <= x; i++) {
            int y = sc.nextInt();
            int z = sc.nextInt();
            System.out.println("Case #" + i + ": " + (y+z));
        }
	}
}
