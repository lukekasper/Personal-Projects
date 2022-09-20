package seconds_converter;
import java.util.Scanner;

/**
 * Simple game with 2 options:
 * - Convert seconds to hour, minute, and seconds.
 * - Add all the digits in an Integer.
 */
public class SimpleGame {

	/**
	 * Write a method to convert the given seconds to hours: minutes: seconds.
	 * @param seconds to convert
	 * Example: If input seconds is 86399, print output in the format: 23:59:59
	 */
	
	int seconds;
	int input;
	
	public void convertTime(int seconds){
		this.seconds = seconds;
		int hours = seconds/3600;
		seconds -= hours*3600;
		int minutes = seconds/60;
		seconds -= minutes*60;
		System.out.println(hours + ":" + minutes + ":" + seconds);						
	}

	/**
	 * Write a method that adds all the digits in the given integer.
	 * @param input to add digits
	 * Example: If input is 565, print 16.
	 */
	
	public void digitsSum(int input){
		this.input = input;
		int inp1 = input/100;
		input -= inp1*100;
		int inp2 = input/10;
		input -= inp2*10;
		int inp3 = input;
		int tot = inp1 + inp2 + inp3;
		System.out.println("The sum of all of the digits is: " + tot);	
	}
	
	public static void main(String[] args) {
		
		SimpleGame game = new SimpleGame();
		
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Which game would you like to play?");
		System.out.println("Enter '1' to convert seconds to time and enter '2' to sum the digits.");
		
		int flag = 0;
		
		while (flag ==  0) {
			int game_choice = sc.nextInt();
			if (game_choice == 1) {
				System.out.println("Choose the total number of seconds.");	
				int second_input = sc.nextInt();
				game.convertTime(second_input);
				flag = 1;
			} 	
			else if (game_choice == 2) {
				System.out.println("Choose an integer to sum the digits.");
				int integer_sum = sc.nextInt();
				game.digitsSum(integer_sum);
				flag = 1;
			} 	
			else {
				System.out.println("You did not enter a valid integer choice");
			}
		}
		
		sc.close();
		}
	}
	
