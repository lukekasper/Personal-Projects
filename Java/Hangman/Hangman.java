import java.util.ArrayList;

abstract class Hangman {

	// initialize private variables
	private String word;
	private ArrayList<String> currentWordFamily = new ArrayList<String>();
	private char[] status;
	private ArrayList<Character> wrongGuesses;
	private int statusLength;

	/**
	 * Constructor for general Hangman game.
	 * @param filePath to load list of words
	 */
	public Hangman(String filePath) {

		// call the words parse constructor to create a new list of words from the file located at the filepath
		wordsParse w = new wordsParse(filePath);
		
		// then read that file in order to set the words list
		w.readParse();
		
		// set the current word to a random word from the list and get the list of words
		this.word = w.getRandomWord();
		String[] wordsList = w.getWords();

		// iterate over the array of words
		for (String i : wordsList) {

			// add all of the words with the same length as the current word to the current word family list
			if (this.word.length() == i.length()) {
				currentWordFamily.add(i);
			}
		}

		// set the status array to an array of chars with length equal to the current word length
		this.status = new char[this.word.length()];

		// iterate over the length of the status
		for(int ix=0;ix<this.status.length;ix++) {

			// and set all the elements to '-'
			status[ix] = '-';
		}

		// initialize the wrongGuesses and statusLength variables
		this.wrongGuesses = new ArrayList<Character>();
		this.statusLength = this.status.length;
	}

	/**
	 * Abstract guess letter method to be implemented in subclasses.
	 * @param s - user input character guess
	 */
	abstract void guessLetter(char s);
	
	/**
	 * Gets the current word family.
	 * @return current word family
	 */
	public ArrayList<String> getCurrentWordFamily() {
		return this.currentWordFamily;
	}
	
	/**
	 * Sets the current word family to the specified arrayList.
	 * @param wordFamily to set current word family to
	 */
	public void setCurrentWordFamily(ArrayList<String> wordFamily) {
		this.currentWordFamily = wordFamily;
	}

	/**
	 * Gets the current word.
	 * @return the current word
	 */
	public String getWord() {
		return this.word;
	}
	
	/**
	 * Sets the current word to the specified parameter String.
	 * @param word to set to current word
	 */
	public void setWord(String word) {
		this.word = word;
	}

	/**
	 * Adds the guess to the wrong guesses array.
	 * @param s - guess to add to wrong guesses array
	 */
	public void setWrongGuesses(char s) {
		this.wrongGuesses.add(s);
	}

	public ArrayList<Character> getWrongGuesses() {
		return this.wrongGuesses;
	}
	
	/**
	 * Sets the status of the game.
	 * @param ix - index of status array
	 * @param s - character guess to set in status array
	 */
	public void setStatus(int ix, char s) {
		this.status[ix] = s;
	}

	/**
	 * Gets the length of the status.
	 * @return status length
	 */
	public int getstatusLength() {
		return this.statusLength;
	}

	/**
	 * Decreases the length of the status by 1.
	 */
	public void decreasestatusLength() {
		this.statusLength--;
	}
	
	/**
	 * Get current status
	 * @return status of the game
	 */
	public char[] getStatus() {
		return this.status;
	}

	/**
	 * Prints the status of the game.
	 */
	void printStatus() {
		System.out.println();
		System.out.println("Guess a letter");
		System.out.println(this.status);
		
		// if the wrong guesses array is not empty print it
		if (!this.wrongGuesses.isEmpty()) {
			
			System.out.println("Incorrect guesses: " + this.wrongGuesses.toString().replace(" ", ""));
		}
	}
}
