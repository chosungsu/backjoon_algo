package java_version;

import java.io.IOException;
import java.util.*;
public class q_3052 {
    public static void main(String args[]) throws IOException{
        Scanner in = new Scanner(System.in);
        HashSet<Integer> arr = new HashSet<Integer>();
		
		for (int i = 0; i < 10; i++) {
            int x = in.nextInt();
            arr.add(x % 42);
		}
        System.out.print(arr.size());
	}
}
