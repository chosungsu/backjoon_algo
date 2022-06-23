import java.io.*;
import java.util.*;

public class q_11478 {
    static HashSet<String> set;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        set = new HashSet<>();

        String name = "";
        for(int i = 0; i <= s.length(); i++) {
            name = "";
            for (int j = 0; j < s.length(); j++) {
                name += s.substring(j, j+1);
                set.add(name);
            }
        }
        System.out.println(set.size());
    }
}
