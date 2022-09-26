import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Pattern;

public class wordsParse {
	
	// initialize private variables
	private Scanner sc;
	private String word;
	private String[] listWords;
	private Random r;
	
	/**
	 * Constructor to read the file through a scanner and set the random object.
	 * @param filePath to read words list from
	 */
	public wordsParse(String filePath) {
		
		// try to scan this file
		try {
			this.sc = new Scanner(new File(filePath));
		
		// catch the exception if the file is not found in this filepath
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
		// initialize the random object
		this.r = new Random();
	}
	
	/**
	 * Read the words in the file and set the list of words to those containing only lower case letters.
	 */
	public void readParse() {
		
		// initialize a hashSet of strings
		Set<String> setWords = new HashSet<String>();
		
		// create a pattern matcher to filter out any words containing the below criteria
		Pattern p = Pattern.compile("[A-Z.'\\- 0-9]");
		
		// while the scanner has something to scan
		while(this.sc.hasNext()) {
			
			// set the current word to the next line
			word = this.sc.nextLine();
			
			// if it does not contain any of the specified characters/integers
			if (!p.matcher(word).find()) {
				
				// add it to the hashSet of words
				setWords.add(word);
			}
		}
		
		// close the scanner and change the hashSet to an array
		this.sc.close();
		this.listWords = setWords.toArray(new String[0]);
		setWords = null;
	}
	
	/**
	 * Gets a random word from the list.
	 * @return a String representing a random word from the list
	 */
	public String getRandomWord() {
		
		// return a word from the list at a random index from 0 to the length of the word - 1
		return this.listWords[this.r.nextInt(this.listWords.length)];
	}
	
	/**
	 * Gets the list of words.
	 * @return the list of words
	 */
	public String[] getWords() {
		return this.listWords;
	}
}
