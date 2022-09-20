import java.io.File;
import java.util.Random;
import java.util.Scanner;

public class HangmanControl {

	/**
	 * Main method for game control.
	 * @param args
	 * @author lukekasper, shuliangtian
	 */
	public static void main(String[] args) {
		
		System.out.println("Ready to play Hangman?!");

		// initializes constructor for traditional and evil hangman using the filepath location
		Hangman h = null;
		String filePath = new File("").getAbsolutePath();
		filePath = filePath.concat("/src/words.txt");

		// creates a new scanner using user input
		Scanner sc = new Scanner(System.in);
		String s = null;

		// initialize random object and generate a random binary integer
		Random r = new Random();
		int gameChoice = r.nextInt(2);

		// choose the game based off of the random binary
		if (gameChoice == 0) {
			h = new HangmanTraditional(filePath);
		}
		else {h = new HangmanEvil(filePath);}

		// while the status length is greater than 0
		while (h.getstatusLength()>0) {
			h.printStatus();

			// while the loop is not broken
			while (true) {

				// prompt user for a character input
				s = sc.nextLine();

				// if it is a single lowercase letter, break
				if (s.length() == 1 && s.matches("[a-z]")) {
					break;
				}

				// otherwise print invalid message and re-prompt
				else {
					System.out.println("Invalid enter, please try again");
				}
			}

			// call function for guessing letter based on user input
			h.guessLetter(s.charAt(0));
		}

		// once the game has ended print closing message and close the 
		System.out.println("Congratulations! You succeed!");
		System.out.println("The word is: " + h.getWord());
		
		// print which game was being played
		if (gameChoice == 0) {
			System.out.println("You were playing Traditional Hangman");
		}
		else {
			System.out.println("You are playing Evil Hangman");
		}
		sc.close();
	}
}
