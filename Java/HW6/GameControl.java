package simple21;

import java.util.Scanner;

import java.util.Random;

/**
 * This is a simplified version of a common card game, "21". 
 */
public class GameControl {

	/**
	 * Human player.
	 */
	HumanPlayer human;

	/**
	 * Computer player.
	 */
	ComputerPlayer player1;

	/**
	 * Computer player.
	 */
	ComputerPlayer player2;

	/**
	 * Computer player.
	 */
	ComputerPlayer player3;

	/** 
	 * A random number generator to be used for returning random "cards" in a card deck.
	 * */
	private static int getRandomNumberInRange(int min, int max) {

		// set a min/max range for integers (1-10) return a random integer within that range
		Random r = new Random();
		return r.nextInt((max - min) + 1) + min;
	}

	/**
	 * The main method just creates a GameControl object and calls its run method.
	 * @param args Not used.
	 */
	public static void main(String args[]) { 

		// execute the run method
		new GameControl().run();
	}

	/**
	 * Prints a welcome method, then calls methods to perform each of the following actions:
	 * - Create the players (one of them a Human)
	 * - Deal the initial two cards to each player
	 * - Control the play of the game
	 * - Print the final results
	 */
	public void run() {

		System.out.println("Are you ready to play 21?!");
		System.out.println("You'll play against 3 other players (computers).");
		System.out.println("The goal is to get as close to 21 as possible, without going over.");
		System.out.println("What is your name?");

		// create scanner and create the user and set his/her name as the next input from the keyboard
		Scanner sc = new Scanner(System.in);
		String userName = sc.next();
		createPlayers(userName);

		// deal two cards to each player (one visible and one hidden)
		deal();

		boolean flag = false;

		// runs the control play function until all players have "passed" or busted
		while (flag == false) {
			controlPlay(sc);
			flag = checkAllPlayersHavePassed();
		}

		// close the scanner and print the results
		sc.close();
		printResults();
	}

	/**
	 * Creates one human player with the given humansName, and three computer players with hard-coded names.
	 * @param humansName for human player
	 */
	public void createPlayers(String humansName) {

		// create human with designated user input name, and all 3 computer players
		this.human = new HumanPlayer(humansName);
		this.player1 = new ComputerPlayer("Player1");
		this.player2 = new ComputerPlayer("Player2");
		this.player3 = new ComputerPlayer("Player3");

	}

	/**
	 * Deals two "cards" to each player, one hidden, so that only the player who gets it knows what it is, 
	 * and one face up, so that everyone can see it. (Actually, what the other players see is the total 
	 * of each other player's cards, not the individual cards.)
	 */
	public void deal() { 

		// call a random card and deal it to the human as a hidden card
		int card1 = nextCard();
		human.takeHiddenCard(card1);

		// call a second card and deal it to the human as a visible card
		int card2 = nextCard();
		human.takeVisibleCard(card2);

		System.out.println(" ");

		// repeat this process for the computer players
		int card3 = nextCard();
		player1.takeHiddenCard(card3);

		int card4 = nextCard();
		player1.takeVisibleCard(card4);

		System.out.println(" ");

		int card5 = nextCard();
		player2.takeHiddenCard(card5);

		int card6 = nextCard();
		player2.takeVisibleCard(card6);

		System.out.println(" ");

		int card7 = nextCard();
		player3.takeHiddenCard(card7);

		int card8 = nextCard();
		player3.takeVisibleCard(card8);

		System.out.println(" ");
	}

	/**
	 * Returns a random "card", represented by an integer between 1 and 10, inclusive. 
	 * The odds of returning a 10 are four times as likely as any other value (because in an actual
	 * deck of cards, 10, Jack, Queen, and King all count as 10).
	 * 
	 * Note: The java.util package contains a Random class, which is perfect for generating random numbers.
	 * @return a random integer in the range 1 - 10.
	 */
	public int nextCard() { 

		// gets a random integer between 1 and 13 (to include jack, queen, and king cards)
		int card = getRandomNumberInRange(1, 13);

		// sets the 11, 12, and 13 cards to value 10
		if (card == 11 || card == 12 || card == 13) {
			card = 10;
		}
		return card;
	}

	/**
	 * Gives each player in turn a chance to take a card, until all players have passed. Prints a message when 
	 * a player passes. Once a player has passed, that player is not given another chance to take a card.
	 * @param scanner to use for user input
	 */
	public void controlPlay(Scanner scanner) {

		// starts off the game (after the deal) by asking the user if he/she would like another card
		// unless they have already passed
		if (human.passed == false) {
			boolean anotherCard = human.offerCard(human, player1, player2, player3, scanner);

			// as long as the user keeps requesting another card 'y', continuously runs the loop
			if (anotherCard == true) {

				// adds a random card to the user's visible card total
				int card = nextCard();
				human.takeVisibleCard(card);

				// if the user goes over 21, they "bust" and their turn is over
				if (human.getScore() > 21) {
					System.out.println("You busted!");
					human.passed = true;
				}
			}
			else {
				System.out.println(human.name + " passes.");
			}
		} else {
			System.out.println(human.name + " passes.");
		}

		System.out.println(" ");

		// same syntax for computer players
		if (player1.passed == false) {
			boolean anotherCard1 = player1.offerCard(human, player1, player2, player3);

			if (anotherCard1 == true) {
				int card = nextCard();
				player1.takeVisibleCard(card);
				if (player1.getScore() > 21) {
					System.out.println(player1.name + " busted!");
					player1.passed = true;
				}
			}
		} else {
			System.out.println(player1.name + " passes.");
		}

		System.out.println(" ");

		if (player2.passed == false) {
			boolean anotherCard2 = player2.offerCard(human, player1, player2, player3);

			if (anotherCard2 == true) {
				int card = nextCard();
				player2.takeVisibleCard(card);	
				if (player2.getScore() > 21) {
					System.out.println(player2.name + " busted!");
					player2.passed = true;
				}
			}
		} else {
			System.out.println(player2.name + " passes.");
		}

		System.out.println(" ");

		if (player3.passed == false) {
			boolean anotherCard3 = player3.offerCard(human, player1, player2, player3);

			if (anotherCard3 == true) {
				anotherCard3 = player3.offerCard(human, player1, player2, player3);
				int card = nextCard();
				player3.takeVisibleCard(card);
				if (player3.getScore() > 21) {
					System.out.println(player3.name + " busts!");
					player3.passed = true;
				}
			}
		} else {
			System.out.println(player3.name + " passes.");
		}

		System.out.println(" ");
	}


	/**
	 * Checks if all players have passed.
	 * @return true if all players have passed
	 */
	public boolean checkAllPlayersHavePassed() {

		// if all of the players have their flag "passed" set to true, then return true
		if (human.passed == true && player1.passed == true && player2.passed == true && player3.passed == true) {
			return true;
		}
		else {
			return false;
		}
	}

	/**
	 * Prints a summary at the end of the game.
	 * Displays how many points each player had, and if applicable, who won.
	 */
	public void printResults() { 

		// print all of the players names and score.
		System.out.println("Game Over!");
		System.out.println(human.name + " has a total score of " + human.getScore() + " points.");
		System.out.println(player1.name + " has a total score of " + player1.getScore() + " points.");
		System.out.println(player2.name + " has a total score of " + player2.getScore() + " points.");
		System.out.println(player3.name + " has a total score of " + player3.getScore() + " points.");
		printWinner();
	}

	/**
	 * Determines who won the game, and prints the results.
	 */
	public void printWinner() { 

		// get the score for each player
		int score1 = human.getScore();
		int score2 = player1.getScore();
		int score3 = player2.getScore();
		int score4 = player3.getScore();

		// create a new variable "tempScore(n)" and set it to the score for each player
		int tempScore1 = score1;
		int tempScore2 = score2;
		int tempScore3 = score3;
		int tempScore4 = score4;

		// if any of the player's scores are > 21, set the respective tempScore to 0
		if (score1 > 21) {
			tempScore1 = 0;
		}

		if (score2 > 21) {
			tempScore2 = 0;
		}

		if (score3 > 21) {
			tempScore3 = 0;
		}

		if (score4 > 21) {
			tempScore4 = 0;
		}

		// if this players score tempScore is greater than all of the other scores,
		// print a message saying that they win and their score.
		if (tempScore1 > tempScore2 && tempScore1 > tempScore3 && tempScore1 > tempScore4) {
			System.out.println("You win! With a score of " + score1);
		}
		else if (tempScore2 > tempScore1 && tempScore2 > tempScore3 && tempScore2 > tempScore4) {
			System.out.println(player1.name + " wins! With a score of " + score2);
		}
		else if (tempScore3 > tempScore1 && tempScore3 > tempScore2 && tempScore3 > tempScore4) {
			System.out.println(player2.name + " wins! With a score of " + score3);
		}
		else if (tempScore4 > tempScore1 && tempScore4 > tempScore2 && tempScore4 > tempScore3) {
			System.out.println(player3.name + " wins! With a score of " + score4);
		}
		else {
			System.out.println("Tie! Nobody wins.");
		}
	}
}
