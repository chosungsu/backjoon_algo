import java.io.*;
import java.util.*;

public class q_11478 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        String s = br.readLine();

        HashSet<String> set = new HashSet<>();
        for (int i = 0; i <= s.length(); i++) {
            for (int j = 0; j <= s.length(); j++) {
                set.add(s.substring(i, j));
            }
        }
        
        StringBuilder sb = new StringBuilder();
        sb.append(set.size());
        System.out.println(sb.toString());
        br.close();
    }
}
