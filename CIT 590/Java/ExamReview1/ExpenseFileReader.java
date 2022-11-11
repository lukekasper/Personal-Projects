package expenses.file;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Manages the loading of expense files.
 * @author lbrandon
 *
 */
public class ExpenseFileReader {

	/**
	 * Loads the given filename and adds each line to a list.
	 * Ignores lines with only whitespace.
	 * @param fileName to load
	 * @return list of lines from the file
	 */
	public static List<String> loadExpenses(String fileName) {

		File file = new File(fileName);
		List<String> expensesList = new ArrayList<String>();
		FileReader fileReader = null;
		BufferedReader bufferedReader = null;

		try {
			fileReader = new FileReader(file);
			bufferedReader = new BufferedReader(fileReader);
			
			
			String line = "";

			while ((line = bufferedReader.readLine()) != null) {
				line = line.strip();
				if (!line.isEmpty()) {
					expensesList.add(line);
				}
			}
			
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

		finally {
			try {
				fileReader.close();
				bufferedReader.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

		return expensesList;
	}

	/**
	 * Parses month and expense amount from given list of expenses.
	 * Each row has a month number, a delimiter, and an expense amount.
	 * Delimiters can include a comma (,), a colon (:), or multiple spaces ('    ').
	 * 
	 * Stores expenses in list of maps, each one consisting of a month number and expense amount.
	 * For example:
	 *   [{1=57.38}, {5=5.06}, {10=456.99}, {5=3.99}, ...]
	 *   Where 1 is the month (for jan) and 57.38 is an expense for that month.  
	 *   5 is the month (for may) and 5.06 is an expense amount for that month.  
	 *   There is also a second expense of 3.99 for month 5.
	 * @param expenseList to parse
	 * @return map of monthlyExpenses
	 */
	public static List<Map<Integer, Double>> parseExpenses(List<String> expenseList) {
		
		List<Map<Integer, Double>> monthlyExpenses = new ArrayList<Map<Integer, Double>>();
		
		for (String expense : expenseList) {
			
			String[] expenseLine = expense.split("[,.:\\s]+");
			int month = Integer.parseInt(expenseLine[0].strip());
			double amount = Double.parseDouble(expenseLine[1].strip());
			
			Map<Integer, Double> expenseEntry = new HashMap<Integer, Double>();
			expenseEntry.put(month, amount);
			
			monthlyExpenses.add(expenseEntry);
		}
		
		return monthlyExpenses;
	}
}