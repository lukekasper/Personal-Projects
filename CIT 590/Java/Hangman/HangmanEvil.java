import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Random;
import java.util.Set;

public class HangmanEvil extends Hangman {

	// initialize map for the current word
	// map contains each character as a key, and an integer list denoting index position in the word
	private Map<Character, ArrayList<Integer>> map;
	// initialize set to store correctly-guessed letters
	private Set<Character> set;

	/**
	 * Constructor for Evil Hangman game.
	 * @param filePath for list of words to pull from
	 */
	public HangmanEvil(String filePath) {

		super(filePath);
		set = new HashSet<Character>();
	}
	/**
	 * Overrides abstract class to dictate what happens when the user guesses a letter in Evil Hangman.
	 * @param s - user input character guess
	 */
	@Override
	void guessLetter(char s) {

		// Revising the words list and setting the new random word.

		// initialize random object and empty arrayList for the word family
		Random r = new Random();
		ArrayList<String> wordFamily = new ArrayList<String>();

		// revise and set the current word family list based on the users next guess
		this.reviseWordFamily(s,this.getCurrentWordFamily());
		wordFamily = this.getCurrentWordFamily();

		// get a random index for the revised list 
		// set the current word to the word in the list at that random index
		int wordIndex = r.nextInt(wordFamily.size());
		this.setWord(wordFamily.get(wordIndex));

		// construct the hashMap
		map = new HashMap<Character, ArrayList<Integer>>();

		// get the word set in the previous part
		String word = this.getWord();


		// Setting the map.

		// iterating through the the length of the word
		for (int ix = 0; ix < word.length();ix++) {
			if (set.contains(word.charAt(ix))) {
				continue;
			}
			// if the map does not yet contain the specified character in the word
			if(!map.containsKey(word.charAt(ix))) {

				// create that character key
				map.put(word.charAt(ix), new ArrayList<Integer>());
			}

			// then place the index as the key value (can have multiple indexes)
			map.get(word.charAt(ix)).add(ix);
		}

		// Applying the guess to the map of the word's characters.

		// if both the map and set does not contain the user's guess
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

		// otherwise if the key is contained within the map
		else {

			// while the specified key still has a value associated
			while(!map.get(s).isEmpty()) {

				// change the game status at the keys specified value to the user's guess
				this.setStatus(map.get(s).get(map.get(s).size()-1), s);

				// then remove that character from the map and decrease the status length
				map.get(s).remove(map.get(s).size() - 1);
				set.add(s);
				this.decreasestatusLength();
			}
		}
	}

	/**
	 * Revises the word family based on the user's previous guess.
	 * @param s - user input character guess
	 * @param wordFamily to revise
	 */
	private void reviseWordFamily(char s, ArrayList<String> wordFamily) {  

		// initialize HashMap which will contain new word families
		HashMap <String, ArrayList<String>> newWordFamilies = new HashMap <String,ArrayList<String>>();

		// iterating over the current word family
		for (String word : wordFamily) {

			// initialize an empty string and arrayList
			String key = "";
			ArrayList<String> wordFamilyList = new ArrayList<String>();

			// iterate over the characters of each word in the list
			for (int i = 0; i < this.getWord().length(); i++ ) {

				// if the word contains the user input character, and that index location to the key
				if (word.charAt(i) == s) {
					key += i + ", ";
				}
			}

			// if the new family of words does not contain the previously defined key
			if(!newWordFamilies.containsKey(key)) {

				// add that key to the HashMap
				newWordFamilies.put(key, wordFamilyList);
			}

			// then add the word as the value to that key (each index list can contain multiple words)
			// this is how we will partition the word families based on character location
			newWordFamilies.get(key).add(word);
		}

		ArrayList<String> keys = new ArrayList<String>(newWordFamilies.keySet());
		// initialize an empty arrayList of integers to represent the size of each word family
		ArrayList<Integer> numWords = new ArrayList<Integer>();

		// iterate over the keys of the new word families
		for (String w : keys) {

			// add the length of each word family to the new arrayList of integers
			numWords.add(newWordFamilies.get(w).size());
		}

		// find the max of the list and its index
		int max = Collections.max(numWords);
		int maxIndex = numWords.indexOf(max);

		// use that index to find the word family with the most words and set that to the new current word family
		this.setCurrentWordFamily(newWordFamilies.get(keys.get(maxIndex)));
	}
}
