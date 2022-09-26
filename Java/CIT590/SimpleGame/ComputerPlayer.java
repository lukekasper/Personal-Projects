package simple21;

/**
 * Represents a computer player in this simplified version of the "21" card game.
 */
public class ComputerPlayer {

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
	 * Constructs a computer player with the given name.
	 * @param name of the user.
	 */
	public ComputerPlayer(String name) {

		// sets the specified name to this computer player
		this.name = name;
	}

	/**
	 * Decides whether to take another card. In order to make this decision, this player considers 
	 * their own total points (sum of visible cards + hidden card). 
	 * This player may also consider other players' sum of visible cards, but not the value 
	 * of other players' hidden cards.
	 * @param human The other human player
	 * @param player1 Another (computer) player
	 * @param player2 Another (computer) player
	 * @param player3 Another (computer) player
	 * @return true if this player wants another card
	 */
	public boolean offerCard(HumanPlayer human, ComputerPlayer player1, ComputerPlayer player2, ComputerPlayer player3) { 

		// get the score and name of whatever player calls this function
		int mySum = this.getScore();
		String myName = this.name;

		// initialize sums and set them to 0
		int sum1 = 0;
		int sum2 = 0;
		int sum3 = 0;
		int sum4 = 0;

		// if the name of the player calling this function is not human, get the visible sum of the humans cards
		if (myName.equals(human.name) == false) {
			sum1 = human.getSumOfVisibleCards();
		}

		// similarly do this for every player that does not share a name with the player calling this function
		if (myName.equals(player1.name) == false) {
			sum2 = player1.getSumOfVisibleCards();
		}

		if (myName.equals(player2.name) == false) {
			sum3 = player2.getSumOfVisibleCards();
		}

		if (myName.equals(player3.name) == false) {
			sum4 = player3.getSumOfVisibleCards();
		}

		// the player should take another card if his total score is <= 16
		if (mySum <= 16) {
			return true;
		}

		// the player should also take another card if his total sum is less than 
		// any of the visible sums of the other players plus 7 (arbitrary number to make the computer competitive)
		// unless that players sum + 7 is greater than 21
		else if ((mySum < (sum1 + 7) && (sum1 + 7) < 21) || 
				(mySum < (sum2 + 7) && (sum1 + 7) < 21) || 
				(mySum < (sum3 + 7) && (sum3 + 7) < 21) || 
				(mySum < (sum4 + 7) && (sum4 + 7) < 21)) {
			return true;
		}

		// otherwise print the name of the player and that they pass and set the "passed" flag to "true"
		else {
			this.passed = true;
			System.out.println(myName + " passes.");
			return false;
		}
	}

	/**    
	 * Puts the specified card in this player's hand as the hidden card.
	 * Prints a message saying that the card is being taken, but does not print the value of the hidden card.
	 * @param card being taken
	 */
	public void takeHiddenCard(int card) {

		// set the player calling the function's hidden card to the specified card parameter
		this.hiddenCard = card;
		System.out.println(this.name + " takes a hidden card.");	
	}

	/**
	 * Adds the given card to the sum of the visible cards for this player.
	 * Prints a message saying that the card is being taken.
	 * @param card being taken
	 */
	public void takeVisibleCard(int card) { 

		// get the sum of visible cards of the player calling this function
		int prevSum = this.getSumOfVisibleCards();

		// set the new sum to the previous sum + the specified card parameter
		this.sumOfVisibleCards = prevSum + card;
		System.out.println(this.name + " takes a " + card);	
	}

	/**
	 * Returns the total sum of this player's cards, not counting the hidden card. 
	 * @return sumOfVisibleCards
	 */
	public int getSumOfVisibleCards() { 

		// returns sum of visible cards of the player calling this function
		return this.sumOfVisibleCards;
	}

	/**
	 * Return this player's total score (the total of all this player's cards).
	 * That is to say, the sum of the visible cards + the hidden card.
	 * @return total score 
	 */
	public int getScore() { 

		// get the sum of visible cards and the hidden card of the player calling this function
		int sum = this.getSumOfVisibleCards();
		int hidden = this.hiddenCard;

		// add them together in variable "totalScore" and return that variable
		int totalScore = sum + hidden;
		return totalScore; 	
	}
}
