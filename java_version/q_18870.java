package java_version;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class q_18870 {
    public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[n];
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        //배열 복사하기
		int[] copy = arr.clone();
		int idx = 0;
		Arrays.sort(copy);
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		
		for (int i = 0; i < copy.length; i++) {
			if(!map.containsKey(copy[i])) map.put(copy[i], idx++);
		}
		
		for (int i = 0; i < arr.length; i++) bw.write(map.get(arr[i]) + " ");
		bw.flush();
	}
}
