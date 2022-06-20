import java.util.Scanner;

public class q_2525 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int h = sc.nextInt();
		int m = sc.nextInt();
		int n = sc.nextInt();
		
		
		// 모든 시간을 분으로 바꾼다!
		int a = h*60 + m + n;
		h = a/60;
		m = a%60;
		
		//h가 24를 넘는다면?
		if (h>=24) {
			h= h-24;
		}
		
		System.out.println(h + " "+ m);

	}
}
