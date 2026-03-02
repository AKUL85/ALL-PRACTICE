package Facade;
class Computer {

    public void getElectricShock() {
        System.out.println("Ouch!");
    }

    public void makeSound() {
        System.out.println("Beep beep!");
    }

    public void showLoadingScreen() {
        System.out.println("Loading...");
    }

    public void ready() {
        System.out.println("Ready to be used!");
    }

    public void closeEverything() {
        System.out.println("Closing everything...");
    }

    public void pullCurrent() {
        System.out.println("Pulling current...");
    }

    public void sleep() {
        System.out.println("Zzzzz");
    }
}
class ComputerFacade {

    private Computer computer;

    public ComputerFacade(Computer computer) {
        this.computer = computer;
    }

    public void turnOn() {
        computer.getElectricShock();
        computer.makeSound();
        computer.showLoadingScreen();
        computer.ready();
    }

    public void turnOff() {
        computer.closeEverything();
        computer.pullCurrent();
        computer.sleep();
    }
}
public class facade {
    public static void main(String[] args) {

        ComputerFacade computer = new ComputerFacade(new Computer());

        computer.turnOn();
        System.out.println("-----");
        computer.turnOff();
    }
}
