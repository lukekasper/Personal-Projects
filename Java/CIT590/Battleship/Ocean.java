package battleship;
import java.util.Random;

public class Ocean {

	/**
	 * Initializes ships as an empty 10x10 array.
	 */
	private Ship[][]ships = new Ship[10][10];

	/**
	 * Declare instance variables for shots, hits and ships sunk.
	 */
	private int shotsFired;
	private int hitCount;
	private int shipsSunk;

	/**
	 * Initializes current Status as 10x10 array for printing the ocean.
	 */
	private String[][] currentStatus = new String[10][10];

	/**
	 * Constructor for Ocean object.
	 */
	public Ocean() {
		
		// fills the ocean with ships by calling fillOcean method
		this.fillOcean();
		
		// sets shots, hit count, and ships sunk variables to 0
		this.shotsFired = 0;
		this.hitCount = 0;
		this.shipsSunk = 0;
		
		// for each element in the print array "currentStatus"
		for (int row = 0; row < this.currentStatus.length; row++ ) {
			for  (int col = 0; col < this.currentStatus[row].length; col++) {
				
				// fill with the print symbol for "not fired upon" : "."
				this.currentStatus[row][col] = ".";
			}
		}
	}
	/**
	 * Fills the ocean with empty ship objects.
	 */
	private void fillOcean() {
		
		// creates a new empty sea object
		EmptySea empty = new EmptySea();
		
		// loops through the elements of the ships array
		for (int row = 0; row < this.ships.length; row++ ) {
			for  (int col = 0; col < this.ships[row].length; col++) {
				
				// fills the ships array with empty ship objects
				this.ships[row][col] = empty;
			}
		}
	}

	/**
	 * Randomly places all the ships in the ocean.
	 */
	void placeAllShipsRandomly() {

		// creates the appropriate number of objects for each ship
		Submarine submarine1 = new Submarine();
		Submarine submarine2 = new Submarine();
		Submarine submarine3 = new Submarine();
		Submarine submarine4 = new Submarine();
		Destroyer destroyer1 = new Destroyer();
		Destroyer destroyer2 = new Destroyer();
		Destroyer destroyer3 = new Destroyer();
		Cruiser cruiser1 = new Cruiser();
		Cruiser cruiser2 = new Cruiser();
		Battleship battleship = new Battleship();

		// places the ships randomly in the ocean by calling place single ship helper function
		this.placeSingleShip(battleship);
		this.placeSingleShip(cruiser1);
		this.placeSingleShip(cruiser2);
		this.placeSingleShip(destroyer1);
		this.placeSingleShip(destroyer2);
		this.placeSingleShip(destroyer3);
		this.placeSingleShip(submarine1);
		this.placeSingleShip(submarine2);
		this.placeSingleShip(submarine3);
		this.placeSingleShip(submarine4);
	}

	/**
	 * Places a single ship in the ocean.
	 * @param ship to place
	 */
	void placeSingleShip(Ship ship) {

		// initialize flag and horizontal variables
		boolean flag = false;
		boolean horizontal;

		// create a new random object
		Random r = new Random(); 

		// loop while flag = false
		while (flag == false) {

			// generate a random integer 0-9 for the row and column of the bow
			int row = r.nextInt(10);
			int col = r.nextInt(10);
			
			// generate a random binary 0 or 1
			int binary = r.nextInt(2);

			// set horizontal to true or false depending on the binary (0 = true)
			horizontal = (binary == 0)?true:false;

			// check to see if it is ok to place the ship at this location in the ocean
			// by calling okToPlaceShipAt method
			flag = ship.okToPlaceShipAt(row, col, horizontal, this);
			
			// if it is ok to place the ship, place it in the ocean by calling method from Ship class
			if (flag) {
				ship.placeShipAt(row, col, horizontal, this);
			}
		}
	}

	/**
	 * Gets the array of ships in the ocean.
	 * @return array of ships
	 */
	Ship[][] getShipArray() {
		return this.ships;
	}

	/**
	 * Determines if a space in the ocean is occupied.
	 * @param row to check
	 * @param column in row to check
	 * @return boolean true of the space is occupied 
	 */
	boolean isOccupied(int row, int column) {
		
		// if the ship array at (row,column) is type "empty"
		// the spot is not occupied and return false
		if (this.getShipArray()[row][column].getShipType() == "empty") {
			return false;
		}

		else {
			return true;
		}
	}

	/**
	 * Shoots at the ship located at the specified row and column.
	 * @param row to shoot at
	 * @param column to shoot at
	 * @return boolean true if a ship was hit
	 */
	boolean shootAt(int row, int column)  {

		// calls the shootAt method in Ship class at the specified row and column
		boolean flag = this.getShipArray()[row][column].shootAt(row, column);
		
		// sets the currentStatus variable at that row and column 
		// to the appropriate print String defined in the toString method "-"
		this.currentStatus[row][column] = this.getShipArray()[row][column].toString();

		// if there is no ship there, increment shotsFired and return false
		if (flag == false) {
			this.shotsFired++;
			return false;
		}

		// if there is a ship there, increment shotsFired and hitCount
		else {
			this.shotsFired++;
			this.hitCount++;
			
			// if that shot sunk the ship (hit array is full), increment shipsSunk
			if (this.getShipArray()[row][column].isSunk()) {
				this.shipsSunk++;
				
				// initialize variables r and c and set them 
				// to the respective bowRow and bowColumn of the ship at element (row,column)
				int r = this.getShipArray()[row][column].getBowRow();
				int c = this.getShipArray()[row][column].getBowColumn();
				
				// initialize length to the length of the ship at this location
				int length = this.getShipArray()[row][column].getLength();
				
				// if the ship is horizontal
				if(this.getShipArray()[row][column].isHorizontal()) {
					
					// loop over the ship and set the currentStatus print variable at that location
					// to the String defined in toString method "s"
					for(int col = c;col >= c - length + 1; col--) {
						this.currentStatus[r][col] = this.getShipArray()[r][col].toString();
					}
				}
				
				// if the ship is not sunk
				else {
					
					// loop over the array and set currentStatus to "x"
					for(int row_ = r;row_ >= r - length + 1; row_--) {
						this.currentStatus[row_][c] = this.getShipArray()[row_][c].toString();
					}
				}
			}
			return true;  // if there was a hit of some kind
		}
	}

	/**
	 * Gets total number of shots fired.
	 * @return shots fired
	 */
	int getShotsFired() {
		return this.shotsFired;
	}

	/**
	 * Gets the total hits.
	 * @return hit count
	 */
	int getHitCount() {
		return this.hitCount;
	}

	/**
	 * Gets the total number of ships sunk.
	 * @return ships sunk
	 */
	int getShipsSunk() {
		return this.shipsSunk;
	}

	/**
	 * Checks to see if the game is over
	 * @return true if all 10 ships have been sunk
	 */
	boolean isGameOver() {
		return (this.getShipsSunk() == 10)?true:false;
	}

	/**
	 * Prints out the GUI representing the status of the hits as a game board.
	 */
	void print() {
		
		// initialize array of strings representing numbers 0-9
		String[] s = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
		
		// print a line of these numbers with a space in between preceded by two spaces
		System.out.println("  " + String.join(" ", s));
		
		// loop throw all the rows
		for (int r = 0; r < this.ships.length; r++) {
			
			// print an integer number for each row and then the current status for that row
			System.out.println(r + " " + String.join(" ", this.currentStatus[r]));
		}
	}
	
	/**
	 * Prints a heading with a key for the GUI
	 */
	void printHeading() {
		System.out.println("Ready to play Battleship?!");
		System.out.println(" ");
		System.out.println("Key:");
		System.out.println("x : hit");
		System.out.println("- : miss");
		System.out.println("s : ship is sunk");
		System.out.println(". : spot has not been shot at");
		System.out.println(" ");
	}
}
