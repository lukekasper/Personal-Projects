package expenses;

import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

/**
 * Represents a single expense for a particular month.
 * @author lbrandon
 */
public class Expense {

	/**
	 * Month of expense.
	 */
	int month;
	
	/**
	 * Amount of expense.
	 */
	double amount;
	
	/**
	 * Creates Expense with given month and amount.
	 * @param month for expense
	 * @param amount for expense
	 */
	public Expense(int month, double amount) {
		this.month = month;
		this.amount = amount;
	}
	
	/**
	 * Get month of expense.
	 * @return month
	 */
	public int getMonth() {
		return this.month;
	}
	
	/**
	 * Get amount of expense.
	 * @return amount
	 */
	public double getAmount() {
		return this.amount;
	}
	
	/**
	 * Returns the expense month and amount.
	 */
	@Override 
	public String toString() {
		return this.month + " : " + this.amount;
	}
	
	/**
	 * Compares two Expense objects for equality, based on the amounts.
	 * If the amounts are equal, the Expense objects are equal.
	 */
	@Override 
	public boolean equals(Object o) {
		if (o instanceof Expense) {
			Expense expense2 = (Expense)o;
			return (expense2.getAmount() == this.getAmount());
		}
		
		return false;
	}
}