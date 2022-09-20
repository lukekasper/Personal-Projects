package expenses;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.Map.Entry;

import expenses.file.ExpenseFileReader;

/**
 * Keeps track of expense information for different months.
 * @author lbrandon
 */
public class Expenses {

	/**
	 * List of monthly expenses, each one storing the month number and expense amount.
	 */	
	private List<Expense> monthlyExpenses;
	
	/**
	 * Mappings to match a month abbreviation with a month number.
	 * For example, it should look like this:
	 *   {"jan"=1, "feb"=2, ...}
	 */
	private Map<String, Integer> monthlyMappings;
	
	/**
	 * Creates Expenses for storing and managing individual monthly expenses.
	 * Initializes list of monthly expenses and creates mappings to match a month abbreviation with a month number.
	 */
	public Expenses() {
		
		//to store list of expenses
		this.monthlyExpenses = new ArrayList<Expense>();
		
		//to store month abbreviations and month numbers
		this.monthlyMappings = new HashMap<String, Integer>();
		
		//create String array of month abbreviations
		String[] months = {"jan", "feb", "march",  "april", "may", "june", 
				"july", "aug", "sept", "oct", "nov", "dec"};
		
		int monthCount = 1;
		for (String month : months) {
			this.monthlyMappings.put(month, monthCount++);
		}
	}
	
	/**
	 * Gets list of monthly expenses.
	 * @return list of expenses
	 */
	public List<Expense> getMonthlyExpenses() {
		return this.monthlyExpenses;
	}
	
	/**
	 * Gets mappings to match a month abbreviation with a month number.
	 * @return map of month names and month numbers
	 */
	public Map<String, Integer> getMonthlyMappings() {
		return this.monthlyMappings;
	}
	
	/**
	 * Converts each expense in the given list to an Expense object,
	 * and adds it to the internal list of monthly expenses.
	 * @param expenses to add
	 */
	public void addExpenses(List<Map<Integer, Double>> expenses) {
		
		for (Map<Integer, Double> expenseEntry : expenses) {
		
			for (Entry<Integer, Double> monthlyExpenseEntry : expenseEntry.entrySet()) {
				
				int month = monthlyExpenseEntry.getKey();
				double amount = monthlyExpenseEntry.getValue();
				
				Expense expense = new Expense(month, amount);
				
				this.addExpense(expense);
			}
		}
	}
	
	/**
	 * Adds given Expense object to the internal list of monthly expenses.
	 * @param expense to add
	 */
	public void addExpense(Expense expense) {
		this.monthlyExpenses.add(expense);
	}
	
	/**
	 * Gets expenses for given month.
	 * Maps given month name to month number.
	 * @param month to look up
	 * @return expenses for given month
	 */
	public List<Double> getMonthlyExpenses(String month) {
		
		int monthInt = this.getMonthlyMappings().get(month);
		return getMonthlyExpenses(monthInt);
	}
	
	/**
	 * Gets expenses for given month.
	 * @param month to look up
	 * @return expenses for given month
	 */
	public List<Double> getMonthlyExpenses(int month) {
		
		List<Double> expenses = new ArrayList<Double>();
		
		for (Expense expense : this.monthlyExpenses) {
			
			if (expense.month == month) {
				expenses.add(expense.getAmount());
			}
		}
		return expenses;
	}

	/**
	 * Gets total of expenses for given month.
	 * @param month to look up
	 * @return total expenses for given month
	 */
	public double getTotalMonthlyExpenses(String month) {
		
		List<Double> monthExpenses = this.getMonthlyExpenses(month);
		int sum = 0;
		
		for (Double amount : monthExpenses) {
			sum += amount;
		}
		
		return sum;
	}
	
	/**
	 * Calculates the month with the highest expenses.
	 * @return Expense object with information for most expensive month
	 */
	public Expense getMostExpensiveMonth() {
		
		List<Expense> monthlyExpenses = this.getMonthlyExpenses();
		List<Double> totalExpense = new ArrayList<Double>();
		
		Set<Entry<String,Integer>> monthMap = this.getMonthlyMappings().entrySet();
		
		Double maxAmount = 0.0;
		int maxMonth = 0;
		
		for (Entry<String,Integer> entry : monthMap) {
			
			String month = entry.getKey();
			int monthInt = entry.getValue();
			
			Double total = this.getTotalMonthlyExpenses(month);
			
			if (maxAmount < total) {
				
				maxAmount = total;
				maxMonth = monthInt;
			}
		}
		
		return new Expense(maxMonth, maxAmount);
	}
	
	public static void main (String[] args) {
		Expenses expenses = new Expenses();
		
		//load expense file
		List<String> expenseList = ExpenseFileReader.loadExpenses("expenses.txt");
		
		//clean expenses
		List<Map<Integer, Double>> monthlyExpenses = ExpenseFileReader.parseExpenses(expenseList);
				
		//add expenses to internal list of expenses
		expenses.addExpenses(monthlyExpenses);
		
		//get oct expenses
		List<Double> octMonthlyExpenses = expenses.getMonthlyExpenses("oct");
		System.out.println("Oct. Expenses: " + octMonthlyExpenses);
		
		System.out.println();
		
		//get jan expenses
		List<Double> janMonthlyExpenses = expenses.getMonthlyExpenses("jan");
		System.out.println("Jan. Expenses: " + janMonthlyExpenses);
		
		//get total jan expenses
		double totalJanMonthlyExpenses = expenses.getTotalMonthlyExpenses("jan");
		System.out.println("Total: " + totalJanMonthlyExpenses);
				
		System.out.println();
		
		//get feb (2) expenses
		List<Double> febMonthlyExpenses = expenses.getMonthlyExpenses(2);
		System.out.println("Feb. Expenses: " + febMonthlyExpenses);
		
		//get total feb expenses
		double totalFebMonthlyExpenses = expenses.getTotalMonthlyExpenses("feb");
		System.out.println("Total: " + totalFebMonthlyExpenses);
		
		System.out.println();
		
		//get highest expense
		Expense mostExpensiveMonth = expenses.getMostExpensiveMonth();
		System.out.println("Most Expensive Month: " + mostExpensiveMonth);
		
	}
}
