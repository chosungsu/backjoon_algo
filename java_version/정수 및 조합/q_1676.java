import java.io.*;
import java.util.*;

public class q_1676 {
    public static void main(String[] args) throws IOException{
        //1. 주어지는 값을 읽기
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
		int num = Integer.parseInt(br.readLine());

        //2. 주어진 값을 10 = 2*5로 나눈다면 0의 개수를 알 수 있다
		int count = 0;
		while (num >= 5) {
			count += num / 5;
			num /= 5;
		}
		System.out.println(count);
    }
}
