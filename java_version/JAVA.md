# 자바 언어에서의 핵심 코드 정리

## 초반 입력값 읽기 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    # 방법1
    Scanner in = new Scanner(System.in);
    int x = in.nextInt();
    # 방법2
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    StringTokenizer st = new StringTokenizer(br.readLine(), " ");
    int x = Integer.parseInt(st.nextToken());
  }
}
```

## 배열 문제의 핵심 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Arrays.sort(arr);
  }
}
```

## for 문제의 핵심 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    int x = Integer.parseInt(br.readLine());
    StringTokenizer st;
    for (int i = 0; i < x; i++) {
        st = new StringTokenizer(br.readLine(), " ");
        bw.write((Integer.parseInt(st.nextToken()) + Integer.parseInt(st.nextToken())) + "\n");
    }
    br.close();
    bw.flush();
    bw.close();
  }
}
```

## for 문제의 핵심 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    if(first == second && first == third && second == third){
        System.out.print(10000+(first*1000));
    }
    else if(first == second || first == third)
	  {
		  System.out.print(1000+(first*100));
	  }
	  else if(second == third)
	  {
      System.out.print(1000+(second*100));
	  }
	  else
	  {
		  System.out.print((Math.max(first, Math.max(second, third))*100));
	  }
  }
}
```
