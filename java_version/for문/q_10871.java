package java_version.for문;

import java.util.Scanner;

public class q_10871 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        
        for (int i = 1; i <= x; i++) {
            int z = sc.nextInt();
            if (z < y) {
                System.out.print(z + " ");
            }
            
        }
	}
}
