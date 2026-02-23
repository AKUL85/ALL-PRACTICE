package Java;

class A {
    static { i = 30; } // forward reference
    // static { i++; } // error: illegal forward reference
    { i = 30; } // not a forward reference
    // static {k=20;} //error: cannot find symbol
    static int i = 10;
    int j = 20;
    // { i++; }
    // static { i++; }    
    // static { j++; } //error: non-static variable j cannot be referenced from a static context
    // int i; //error: variable i is already defined in class A
    void m() { System.out.println("m():"+i);        
        // m2();
     }
    static void m2() { 
        // System.out.println("m2():"+j); // error: non-static variable j cannot be referenced from a static context
        System.out.println("m2():"+i);
        // m(); // error: non-static method m() cannot be referenced from a static context
    }
}
public class Lab09_part2 {
    public static void main(String[] args) {   
        A.m2();     
        A a = new A(); a.m();
        // A.i = 15;
        // A a2 = new A(); a2.m();
    }
}