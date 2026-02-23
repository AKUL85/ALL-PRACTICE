package Java;

class A { int i=10;
    A() {System.out.println("A()");}
    A(int i) {
         this();
        // this.i = i; //error: cannot assign initialized field 'i' before supertype constructor has been called
        // A();//error: cannot find symbol        A();
        System.out.println("BeforeThis");
       
        this.i = i;
        System.out.println("A(i)");}    
    A(String s) {System.out.println("A(s)");}  
    //  void A() {System.out.println("mA()");}  
    // void m() {
    //     this(); //error: explicit constructor invocatSystem.outn may only appear within a constructor body
    // }
}
class Lab08_part4 {
    public static void main(String[] args) {
        new A(); new A(0); new A("ABC");
    }
}