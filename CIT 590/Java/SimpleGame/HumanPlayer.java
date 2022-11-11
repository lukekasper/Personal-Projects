package simple21;

import java.util.Scanner;

/**
 * Represents a human player in a game of Simple 21.
 */
public class HumanPlayer {

	/** 
	 * The name of the player.
	 */
	String name;

	/**
	 * The player's one hidden card (a value from 1 - 10).
	 */
	private int hiddenCard = 0;

	/** 
	 * The sum of the player's cards, not counting the hidden card. 
	 */
	private int sumOfVisibleCards = 0;

	/**
	 * Flag indicating if the player has passed (asked for no more cards).
	 */
	boolean passed = false;

	/**
	 * Constructs a human player with the given name.
	 * @param name of the user.
	 */
	public HumanPlayer(String name) {

		// sets the specified name to the user
		this.name = name;
	}

	/**
	 * Asks the Human player whether to take another card and uses the given scanner to prompt for a response.
	 * @param human This human player
	 * @param player1 Another (computer) player
	 * @param player2 Another (computer) player
	 * @param player3 Another (computer) player
	 * @param scanner To use for scanning for human input
	 * @return true if this human player wants another card
	 */
	public boolean offerCard(HumanPlayer human, ComputerPlayer player1, ComputerPlayer player2, ComputerPlayer player3, Scanner scanner) {

		//initializes a response flag as "true"
		boolean response = true;

		// shows the cards of all the players
		this.showCards(this, player1, player2, player3);

		// asks the player calling this function if they would like another card and scans for a response
		// sets the response flag to the boolean value returned by the function
		response = this.getYesOrNoToQuestion("Take another card?", scanner);

		// if the player passes, set the passed flag to true for this player
		if (!response) this.passed = true;

		return response;
	}

	/**
	 * Prints the sum of all of this Human's cards, and the sum of each of the other (computer) players' 
	 * visible cards.
	 * @param human This human player
	 * @param player1 Another (computer) player
	 * @param player2 Another (computer) player
	 * @param player3 Another (computer) player
	 */
	public void showCards(HumanPlayer human, ComputerPlayer player1, ComputerPlayer player2, ComputerPlayer player3) {

		// sets the variable userVisible to the sum of the human's visible cards by calling the function "getSumOfVisibleCards()"
		int userVisible = human.getSumOfVisibleCards();

		// sets the variable userHidden to the humans hidden card
		int userHidden = human.hiddenCard;

		// gets the sum of both variables userHidden and userVisible and prints it
		int sum1 = userVisible + userHidden;
		System.out.println("The users total is: " + sum1);

		// gets the sum of visible cards for each computer player and prints them
		int player1Visible = player1.getSumOfVisibleCards();
		System.out.println(player1.name + "'s total of visibile cards is: " + player1Visible);

		int player2Visible = player2.getSumOfVisibleCards();
		System.out.println(player2.name + "'s total of visibile cards is: " + player2Visible);

		int player3Visible = player3.getSumOfVisibleCards();
		System.out.println(player3.name + "'s total of visibile cards is: " + player3Visible);	
	}

	/**
	 * Displays the given question and prompts for user input using the given scanner.
	 * @param question to ask
	 * @param scanner to use for user input
	 * @return true if the user inputs 'y'
	 */
	public boolean getYesOrNoToQuestion(String question, Scanner scanner) {

		// initializes a boolean response flag to "true"
		boolean response = true;

		String answer;

		System.out.println();
		System.out.print(question + " ");

		// run loop until break is specified
		while(true) {

			// scan for the next input from the keyboard and set that to "answer"
			answer = scanner.next();

			// if the first character of that response is a 'Y' or 'y', response is "true" and break the loop
			if (answer.toLowerCase().charAt(0) == 'y') {
				response = true;
				break;

				// if the first character of that response is a 'N' or 'n', response is "false" and break the loop
			} else if (answer.toLowerCase().charAt(0) == 'n') {
				response = false;
				break;
			}
		}

		return response;
	}

	/**    
	 * Puts the specified card in this human's hand as the hidden card.
	 * Prints a message saying that the card is being taken, and prints the value of the hidden card.
	 * @param card being taken
	 */
	public void takeHiddenCard(int card) {

		// sets the user's hidden card to the specified card parameter and print the user's name and card taken
		this.hiddenCard = card;
		System.out.print(this.name + " takes a " + card + " as a hidden card.");
		System.out.println(" ");
	}

	/**
	 * Adds the given card to the sum of the visible cards for this human player.
	 * Prints a message saying that the card is being taken.
	 * @param card being taken
	 */
	public void takeVisibleCard(int card) { 

		// get the user's sum of visible cards
		int prevSum = this.getSumOfVisibleCards();

		// set the new user's sum to the previous sum + the specified card
		this.sumOfVisibleCards = prevSum + card;

		// print that the user has taken the card and print its value
		System.out.print(this.name + " takes a " + card);	
		System.out.println(" ");
	}

	/**
	 * Returns the total sum of this player's cards, not counting the hidden card. 
	 * @return sumOfVisibleCards
	 */
	public int getSumOfVisibleCards() { 

		// return sum of user's visible cards
		return this.sumOfVisibleCards;
	}

	/**
	 * Return this player's total score (the total of all this human player's cards).
	 * That is to say, the sum of the visible cards + the hidden card.
	 * @return total score 
	 */
	public int getScore() { 

		// get the user's sum of visible cards and hidden card
		int sum = this.getSumOfVisibleCards();
		int hidden = this.hiddenCard;

		// sum them together and return this as the user's total score
		int totalScore = sum + hidden;
		return totalScore;
	}
}
