package Java;
 class Bank{
    private String name;
    private String acc_no;
    private int balance;
    Bank(String name,String acc_no,int balance){
        this.name=name;
        this.acc_no=acc_no;
        this.balance=balance;
    }
    public void deposit(int amount){
        if(amount>0){
            System.err.println("deposit"+amount);
        }
        else{
            System.out.println("fail");
        }
    }
    public void withdraw(int amount){
        if(amount>0&&amount<=balance){
            System.out.println("withdrw");
        }
        else{
            System.out.println("fail");
        }
    }
     public void displayAccountInfo() {
        System.out.println("Account Holder: " + name);
        System.out.println("Account Number: " + acc_no);
        System.out.println("Balance: " + balance);
    }

 }


public class BankAccount {
    public static void main(String[] args) {
        Bank acc1 = new Bank("Rahim", "acc123", 10000);
        Bank acc2 = new Bank("karim", "acc1234", 10000);
        acc1.deposit(2000);
        acc1.withdraw(3000);
        acc1.displayAccountInfo();

        System.out.println("------------------");

        acc2.withdraw(6000);
        acc2.displayAccountInfo();

    }

}
