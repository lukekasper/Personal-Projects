package banking;

import java.util.Scanner;

/**
 * Bank controlling customers and their accounts.
 * @author lukekasper
 *
 */

public class Bank {

	public static void main(String[] args) {
		// create single instance of bank
		Bank bank = new Bank();
			
		//run program from inside run method
		bank.run();
	}
	
	public void run() {
		
		//creates scanner for getting user input
		Scanner scanner = new Scanner(System.in);
		
		System.out.println("Welcome to the Bank!  What's your name?");
		
		String name = scanner.next();
		
		Customer customer = new Customer(name);
		
		System.out.println("What is your address?");
		
		String address = scanner.next();
		customer.setAddress(address);
		
		BankAccount checkingAccount = new BankAccount("checking", customer);
		BankAccount savingsAccount = new BankAccount("savings", customer);
		
		System.out.println("For customer: " + checkingAccount.getCustomerInfo());
		
		System.out.println(checkingAccount.getAccountInfo());
		System.out.println(savingsAccount.getAccountInfo());
		
		System.out.println()
		System.out.println()
	}

}
