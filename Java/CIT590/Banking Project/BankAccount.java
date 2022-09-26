package banking;

public class BankAccount {
	
	/**
	 * Type of account (checking/savings).
	 */
	String accountType;
	double balance;
	Customer customer;
	
	public BankAccount(String accountType, Customer customer) {
		this.accountType = accountType;
		this.customer = customer;
	}
	
	public void deposit(double balance) {
		this.balance += balance;
	}
	
	public void withdraw(double amount) {
		this.balance -= amount; 
	}
	
	public String getAccountInfo() {
		return this.accountType + ": " + this.getBalance();
	}
	
	public double getBalance() {
		return Math.round(this.balance);
	}
	
	public String getCustomerInfo() {
		return this.getCustomerInfo().getName() + " from " + this.getCustomerInfo().getAddress();
	}
}
