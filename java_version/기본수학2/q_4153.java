package java_version.기본수학2;

import java.util.Scanner;

public class q_4153 {
    public static void main(String[] args) {
    
        Scanner in = new Scanner(System.in);
        int[] arr = new int[3];
        while(true) {
            for (int i = 0; i < 3; i++) {
                arr[i] = in.nextInt();
            }
        	
			// 0 0 0 을 입력받으면 종료
            if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
                break;
            }
        	
        	if((arr[0] * arr[0] + arr[1] * arr[1]) == arr[2] * arr[2]) {
				System.out.println("right");
			}
        	else if(arr[0] * arr[0] == (arr[1] * arr[1] + arr[2] * arr[2])) {
				System.out.println("right");
			}
        	else if(arr[1] * arr[1] == (arr[2] * arr[2] + arr[0] * arr[0])) {
				System.out.println("right");
			}
        	else {
				System.out.println("wrong");
			}
        	
		}
 
	}
}
