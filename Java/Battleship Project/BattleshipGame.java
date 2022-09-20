package battleship;

import java.util.Arrays;
import java.util.Scanner;

public class BattleshipGame {
	
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String[] answers = {"n", "N", "no", "No", "f", "false"};
		while(true) {
			Ocean ocean = new Ocean();
			ocean.printHeading();
			ocean.placeAllShipsRandomly();
			while (!ocean.isGameOver()) {
				ocean.print();
				while(true) {
					System.out.println("Enter row and column within 0-9, separated by space:");
					String[] s = scan.nextLine().split(" ");
					try {
						int row = Integer.parseInt(s[0]);
						int column = Integer.parseInt(s[1]);
						ocean.shootAt(row, column);
						break;
					} catch(Exception e) {
						System.out.println("Invalid input! Try again");
					}
				}
			}
			ocean.print();
			System.out.println("Game over!");
			System.out.println("Your shot " + ocean.getShotsFired() + " times");
			System.out.println("You hit " + ocean.getHitCount() + " times");
			System.out.println("Do you want to play again? enter y/n");
			String ans = scan.nextLine();
			if (Arrays.asList(answers).contains(ans)) {
				break;
			}
		}
		scan.close();
	}
}