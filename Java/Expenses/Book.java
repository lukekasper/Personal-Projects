package book;

import java.util.HashMap;
import java.util.Map.Entry;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Represents a book to be cataloged.
 * @author wcauser
 *
 */
public class Book {

	/**
	 * Default value for getting first n number of lines.
	 * See: getFirstLines method
	 */
	private static final int FIRST_LINES_DEFAULT = 10;

	/**
	 * Title of book.
	 */
	private String title;

	/**
	 * Author of book.
	 */
	private String author;

	/**
	 * Lines in book.
	 */
	private List<String> lines;

	/**
	 * Count of words in book.
	 */
	private int wordCount;

	/**
	 * Count of each word in book.
	 */
	private Map<String, Integer> wordCounts;

	/**
	 * Creates a book with the given list of lines.
	 * Parses the title and author of the book.
	 * Sets the total count of words, and the count of each word in the book.
	 * @param lines of text
	 */
	public Book(List<String> lines) {
		this.lines = lines;

		this.setTitleAndAuthor();
		this.countWords();
	}

	/**
	 * Parses the title and author of the book in the list of lines.
	 * 
	 * To get the title of the book, looks for "Title:" at the beginning of a line, and gets the text after it.
	 * Example: 
	 * - Title: Catcher in the Rye
	 * - "Catcher in the Rye" becomes the book title
	 * 
	 * To get the author of the book, looks for "Author:" at the beginning of a line, and gets the text after it.
	 * Example:
	 * - Author: J.D. Salinger
	 * - "J.D. Salinger" becomes the author
	 */
	private void setTitleAndAuthor() {
		// TODO Implement method
		// Hint: Iterate over each line and look for lines starting with "Title:" and "Author:"
		// Set the value of this.title and this.author accordingly.

		List<String> lines = this.lines;
		String regex1 = "Title:";
		String regex2 = "Author:";

		Pattern p1 = Pattern.compile(regex1);
		Pattern p2 = Pattern.compile(regex2);

		for (String line : lines) {
			Matcher m1 = p1.matcher(line);
			Matcher m2 = p2.matcher(line);

			if (m1.find()) {
				String[] lineSplit = line.split(":");
				this.title = lineSplit[1].strip();
			}

			else if (m2.find()) {
				String[] lineSplit = line.split(":");
				this.author = lineSplit[1].strip();
			}
		}
	}

	/**
	 * Counts the total number of words in the list of lines.
	 * Also counts the number of times each word appears in the list of lines.
	 * 
	 * For consistency, words should include a sequence of any of the following characters:
	 * a-z, A-Z, 0-9, _, %, +, -
	 * 
	 * Examples of valid words:
	 *  hello
	 *  HI
	 *  two-fold
	 *  34%
	 *  very_good
	 *  678
	 *  EdWaRd
	 *  1+2
	 */
	private void countWords() {
		// TODO Implement method
		// Hint: Iterate over each line and look for valid words by checking for subsequences
		// of any of the allowed characters above. You can use a character class regular expression.
		//
		// Set the value of this.wordCount to the total number of words.
		// Also, add key:value pairs to this.wordCounts where each key is a word and the value is the count of the word.

		List<String> lines = this.lines;
		Map<String, Integer> wordFreq = new HashMap<String, Integer>();

		Pattern p = Pattern.compile("[a-zA-Z0-9_%+-]");
		int totCount = 0;

		for(String line : lines) {

			Matcher m = p.matcher(line);

			if (m.find()) {

				String[] lineSplit = line.split("[\\s]+");

				for (String word : lineSplit) {

					word.strip();
					totCount++;

					if (!wordFreq.containsKey(word)) {
						wordFreq.put(word,1);
					}

					else {
						int value = wordFreq.get(word);
						wordFreq.replace(word,value++);
					}
				}
			}
		}
		this.wordCount = totCount;
		this.wordCounts = wordFreq;
	}

	/**
	 * Gets the book lines.
	 * @return lines in book
	 */
	public List<String> getLines() {
		return this.lines;
	}

	/**
	 * Gets the book title.
	 * Returns null if title doesn't exist.
	 * @return the title
	 */
	public String getTitle() {
		return this.title;
	}

	/**
	 * Gets the book author.
	 * Returns null if author doesn't exist.
	 * @return the author
	 */
	public String getAuthor() {
		return this.author;
	}

	/**
	 * Gets total count of all words.
	 * @return count of all words
	 */
	public int getTotalWordCount() {
		return this.wordCount;
	}

	/**
	 * Gets unique count of words.
	 * @return count of all words
	 */
	public int getUniqueWordCount() {
		
		Map<String, Integer> wordCount = this.wordCounts;
		int uniqueCount = 0;
		
		for (Entry<String, Integer> entry : wordCount.entrySet()) {
			Integer value = entry.getValue();
			uniqueCount += value;
		}
		return uniqueCount;
	}

	/**
	 * Gets the count of the given word.
	 * Returns 0 if the given word doesn't exist.
	 * @param word to count
	 * @return count of given word
	 */
	public int getSpecificWordCount(String word) {
		// TODO Implement method
		// Hint: First check if the given word is a key before getting the value
		
		Map<String, Integer> wordCount = this.wordCounts;
		
		if (wordCount.containsKey(word)) {
			return wordCount.get(word);
		}
		
		else {
			return 0;
		}
	}

	/**
	 * EXTRA CREDIT!
	 * 
	 * Gets the first Book.FIRST_LINES_DEFAULT lines in the book.
	 * @return the lines
	 */
	/*public List<String> getFirstLines() {
		// TODO Implement method
		// Hint: Call getFirstLines(int n)
	}

	/**
	 * EXTRA CREDIT!
	 * 
	 * Gets the first n lines in the book.
	 * @param n number of lines
	 * @return the lines
	 */
	/*public List<String> getFirstLines(int n) {
		// TODO Implement method
	}*/

	/**
	 * Returns the book title and author for printing.
	 */
	@Override
	public String toString() {
		return "Author: " + this.author + ", Title: " + this.title;
	}
}
