abstract class B {
    int i;

    B(int i) {
        this.i = i;
    }

    abstract int m1(int i, int j);
}

class A extends D {
    int j;

    A(int i, int j) {
        super(i, "ABCDE");
        this.j = j;
    }

    String m2(String s) {
        return s + super.s;
    }

    class C {
        int k;

        C(int k) {
            this.k = k;
        }
    }
}
public class TestD {
    

    static int testCounter = 1;

    static void tester(boolean b) {
        String status = "Failed";
        if (b)
            status = "Passed";
        System.out.printf("Test #%02d %s.%n", testCounter++, status);
    }

    public static void main(String[] args) {
        A a = new A(5, 10);
        tester((a.i + a.j) == 15 && a.s == "ABCDE");
        tester(a.m1(20, 30) == 45 && a.m1(10, 20) == 25);
        tester(a.m2("341").equals("341ABCDE") && a.m2("END").equals("ENDABCDE"));
        tester(a.m2(30).k == 30 && a.m2(50).k == 50);
        B b = new D(15, "RST");
        tester(b.i == 15 && b.m1(10, 20) == 35);
        D d = (D) b;
        tester(d.s == "RST" && d.m1(10, 15) == 30);
        tester(d.m1("YV").equals("**RST||YV") && d.m1("789").equals("**RST||789"));
        tester(d.m3(1.1, 2.3) == 1.7 && d.m3(12.4, 23.6, 12.6) == 16.2);
        tester(d.m3(1.2, 2.3, 3.4, 4.5) == 2.85 && d.m3(2.1) == 2.1);
        tester(d.m2(25).k == 25 && d.m2(72).k == 72);
    }
}
