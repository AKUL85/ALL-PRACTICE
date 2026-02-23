package Java;

class Lab08 {
    {
        System.out.println("BL00|"); //error: illegal forward reference
       
    }   
     {System.out.println("BL01");} //error: <identifier> expected
    int i;
  
     {i = 20;}
    {System.out.println("BL01|"+i);} // Normal Initiallizer Block Executes on Object Creation
    String s = "AB";
    // s = "DEF"; // error: <identifier> expected
    {System.out.println("BL02");
    s += "123"; 
    A:{System.out.println("BL02:SBL01");}
    m();
    } 
    Lab08() {
       System.out.println("Const.");
    }
    void m() {System.out.println("m()");}    
    public static void main(String[] args) {
        System.out.println("Main Starts");
      
        Lab08 a = new Lab08();
       System.out.println(a.i);
    }
    {System.out.println("BL03"); i++;}
}