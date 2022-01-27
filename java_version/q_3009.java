package java_version;

import java.util.Scanner;

//직사각형의 마지막 점을 찾아라.
public class q_3009 {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] x = new int[3];
		int[] y = new int[3];
		int dx, dy;
		
		for(int i = 0; i < 3; i++) {
			x[i] = sc.nextInt();
			y[i] = sc.nextInt();
		}
		
		if(x[1] == x[2])
			dx = x[0];
		else
			dx = (x[0] == x[1]) ? x[2] : x[1];
		
		if(y[1] == y[2])
			dy = y[0];
		else
			dy = (y[0] == y[1]) ? y[2] : y[1];
			
		System.out.println(dx + " " + dy);
	}
}
