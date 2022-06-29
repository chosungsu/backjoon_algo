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

## if 문제의 핵심 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int first = sc.nextInt();
    int second = sc.nextInt();
    int third = sc.nextInt();
    
    if(first == second && first == third && second == third){
        System.out.print(10000+(first*1000));
    }
    else if(first == second || first == third){
	System.out.print(1000+(first*100));
    }
    else if(second == third){
        System.out.print(1000+(second*100));
    }
    else{
	System.out.print((Math.max(first, Math.max(second, third))*100));
    }
  }
}
```


## while 문제의 핵심 코드
```java
import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    # 형태 1 - while 조건에 break 조건 직접 생성
    while (sc.hasNextInt()) {
        int x = sc.nextInt();
        int y = sc.nextInt();
        System.out.println(x + y);
    }
    # 형태 2 - while 내부에 break 조건 생성
    int x = sc.nextInt();
    //사이클 길이 변수
    int cnt = 0;
    //동일한 수를 카피함
    int copy = x;
    while (true) {
        x = ((x % 10) * 10) + (((x / 10) + (x % 10)) % 10);
        cnt++;
        if (copy == x) {
            break;
        }
    }
    System.out.println(cnt);
  }
}
```

