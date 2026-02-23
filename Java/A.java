package Java;

class A {
     int i;
     A(){

     }
     A(int i){
        this.i=i;

     }
     void m(){
        System.out.println(i);
     }
     void m2(int i){
        System.out.println(this.i);
     }
    
    
}

class Lab07 {
    public static void main(String[] args) {
        System.out.println("Lab07.main");
        A a = new A();
        System.out.println(a);
        A a2 = new A();
        System.out.println(a2);
        // A.i = 50; // ERROR
        System.out.println(a.i);
        a.i = 10; a2.i = 20;
        System.out.println(a.i+" "+a2.i);
        a.i += 5;
        System.out.println(a.i+" "+a2.i);
        a = a2; a.i += 5;
        System.out.println(a.i+" "+a2.i);
        a.m(); a2.m();
        a.m2(50); a2.m2(60);
        
        
    }
}