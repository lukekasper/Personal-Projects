import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class HangmanTraditional extends Hangman {

	// initialize map of the current word
	private Map<Character, ArrayList<Integer>> map;

	/**
	 * Constructor for Traditional Hangman game.
	 * @param filePath to load words list from
	 */
	public HangmanTraditional(String filePath) {

		// extension of Hangman
		super(filePath);
		
		// constructor for map of current word
		map = new HashMap<Character, ArrayList<Integer>>();
		
		// get the current word
		String word = this.getWord();

		// iterate over the length of the word
		for (int ix = 0; ix < word.length(); ix++) {

			// if the map does not contain the character at this index
			if(!map.containsKey(word.charAt(ix))) {

				// add the key to the map
				map.put(word.charAt(ix), new ArrayList<Integer>());
			}
			
			// then, add the index as the value for that key
			map.get(word.charAt(ix)).add(ix);
		}
	}

	/**
	 * Denotes the action to take after the user guesses a letter.
	 * @param s - user input character guess
	 */
	@Override
	void guessLetter(char s) {

		// if the map does not contain the user input as a key
		if (!map.containsKey(s) && !this.getWrongGuesses().contains(s)) {

			// add this to the wrong guesses
			this.setWrongGuesses(s);
		}

		else if (!map.containsKey(s) && this.getWrongGuesses().contains(s)) {
			
			// let the user know to stop guessing this letter
			System.out.println("Honey, no more of this letter!");
		}
		
		// otherwise if the key is present but no longer is associated with a value
		else if (map.get(s).isEmpty()) {

			// let the user know to stop guessing this letter
			System.out.println("Honey, no more of this letter!");
		}

		// otherwise if the key
		else {
			
			// and while it still has a value
			while(!map.get(s).isEmpty()) {

				// set the status at that position to the character
				this.setStatus(map.get(s).get(map.get(s).size()-1), s);

				// remove that character from the map and decrease the status length
				map.get(s).remove(map.get(s).size() - 1);
				this.decreasestatusLength();
			}
		}
	}
}
