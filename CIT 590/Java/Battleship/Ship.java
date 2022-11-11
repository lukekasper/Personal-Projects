package battleship;

public abstract class Ship {

	// instance variables

	/**
	 * Row that contains the front part of the ship.
	 */
	private int bowRow;

	/**
	 * Column that contains front part of the ship.
	 */
	private int bowColumn;

	/**
	 * Length of the ship.
	 */
	private int length;

	/**
	 * A boolean that represents whether the ship is going to be placed
	 * horizontally or vertically.
	 */
	private boolean horizontal;

	/**
	 * An array of 4 booleans that indicate whether that part of the ship has been
	 * hit or not.
	 */
	private boolean[] hit;

	/**
	 * Default constructor for ANY ship.
	 * @param length of the ship
	 */
	public Ship(int length) {

		// sets the length of the ship
		this.length = length;

		// initializes the hit array
		this.hit = new boolean[length];
	}

	/**
	 * Gets the row location of the ship.
	 * @return row corresponding to the position of the bow 
	 */
	public int getBowRow() {
		return this.bowRow;
	}

	/**
	 * Sets the value of bowRow
	 * @param bowRow
	 */
	public void setBowRow(int row) {
		this.bowRow = row;
	}

	/**
	 * Gets the column location of the ship.
	 * @return column corresponding to the position of the bow
	 */
	public int getBowColumn() {
		return this.bowColumn;
	}

	/**
	 * Sets the value of bowColumn
	 * @param bowColumn
	 */
	public void setBowColumn(int column) {
		this.bowColumn = column;
	}

	/**
	 * Gets the length of the ship.
	 * @return length
	 */
	public int getLength() {
		return this.length;
	}

	/**
	 * Checks if the ship is horizontal or vertical.
	 * @return whether the ship is horizontal or not
	 */
	public boolean isHorizontal() {
		return this.horizontal;
	}

	/**
	 * Sets the value of the instance variable horizontal.
	 * @param horizontal true if ship is horizontal
	 */
	public void setHorizontal(boolean horizontal) {
		this.horizontal = horizontal;
	}

	/**
	 * Gets the hits on the ship.
	 * @return hit array
	 */
	public boolean[] getHit() {
		return this.hit;
	}

	/**
	 * Abstract class to define the ship type.
	 * @return type of ship as a string
	 */
	public abstract String getShipType();

	/**
	 * Checks whether it is legal to place ship at a given location.
	 * @param row to place the bow of the ship
	 * @param column to place the bow of the ship
	 * @param horizontal - is the ship horizontal
	 * @param ocean array of the ships in the ocean
	 * @return boolean - if the hit is legal or not
	 */
	boolean okToPlaceShipAt(int row, int column, boolean horizontal, Ocean ocean) {

		// initialize length variable as length of the current ship
		int length = this.getLength();

		// if the ship is vertical
		if (horizontal == false) {

			// check to make sure the ship within the array bounds (0-9) for both row and column
			// using the ships length
			if (row > 9 || column > 9 || row - length  + 1 < 0 || column < 0) {
				return false;
			}

			// check to make sure the ship will not overlap or be next to another ship
			else {	

				// initialize variables for ocean elements below, above, left, and right of the ship
				int down = (row == 9)?row:(row + 1);
				int up = (row - length + 1 == 0)?(row - length + 1):(row - length);
				int left = (column == 0)?column:(column - 1);
				int right = (column == 9)?column:(column + 1);

				// call helper function to see if any of these spaces are considered occupied
				if (this.judgeOccupied(down, up, left, right, ocean)) {
					return false;
				}
			}
		}	

		// if the ship is horizontal
		else  {

			// run the same check but considering the ships length in the horizontal direction
			if (row > 9 || column > 9 || row < 0 || column - length + 1 < 0) {
				return false;
			}

			// also check to see if the ship overlaps or is next to another ship
			else {

				// same logic here but for a horizontal ship
				int down = (row == 9)?row:(row + 1);
				int up = (row == 0)?row:(row - 1);
				int left = (column - length + 1 == 0)?(column - length + 1):(column - length);
				int right = (column == 9)?column:(column + 1);
				if (this.judgeOccupied(down, up, left, right, ocean)) {
					return false;
				}
			}
		}
		return true;
	}

	/**
	 * Helper function. Given a set of entries, judge whether one of them is occupied.
	 * @param down down bound
	 * @param up up bound
	 * @param left left bound
	 * @param right right bound
	 * @param ocean Ocean object
	 * @return false if all entries are empty, otherwise return true
	 */
	boolean judgeOccupied(int down, int up, int left, int right, Ocean ocean) {

		// loop through the parameters representing ocean elements 
		// up, down, left, and right of the current element being checked
		for (int r = down; r >= up; r--) {
			for (int c = right; c >= left; c--) {

				// call method in Ocean class to see if the specified element is occupied
				if (ocean.isOccupied(r, c)) {
					return true;
				}
			}
		}
		return false;
	}

	/**
	 * Places current ship at the specified row, column, and orientation in the Ocean.
	 * @param row to place bow at
	 * @param column to place bow at
	 * @param horizontal orientation of the ship
	 * @param ocean to place ship
	 */
	void placeShipAt(int row, int column, boolean horizontal, Ocean ocean) {

		// sets the bow and horizontal variable of the ship to the specified row, column, and orientation
		this.setBowColumn(column);
		this.setBowRow(row);
		this.setHorizontal(horizontal);

		// gets the ship array
		Ship[][] ships = ocean.getShipArray();

		// if the ship is horizontal
		if (horizontal == true) {

			// loop through the length of the ship in the ships array
			for (int c = column; c >= column - this.getLength() + 1; c--) {

				// set the array to the current ship object
				ships[row][c] = this;
			}
		}

		// otherwise do the same for the vertical orientation of the ship
		else {
			for (int r = row; r >= row - this.getLength() + 1; r--) {
				ships[r][column] = this;
			}
		}
	}

	/**
	 * Shoots at the ship object at the specified row and column.
	 * @param row to shoot at
	 * @param column to shoot at
	 * @return boolean true if there is a ship at that location
	 */
	boolean shootAt(int row, int column) {

		// if the ship here is sunk, return false
		if (this.isSunk()) {
			return false;
		}

		// set the bowC and bowR variables to the row and column of the bow of the ship in this location
		int bowC = this.getBowColumn();
		int bowR = this.getBowRow();

		// set the flag for if the ship is horizontal or vertical
		boolean flag = this.isHorizontal();

		// get the hits array of this ship
		boolean[] hits = this.getHit();
		int count = 0;

		// if it is horizontal
		if (flag == true) {

			// loop over the row from the bowC to the length of the ship
			for (int c = bowC; c >= bowC - this.getLength() + 1; c--) {

				// if column and row being shot at contains a ship
				if (column == c && row == bowR) {

					// update hit array with boolean true
					hits[count] = true;
					return true;
				}
				count++;
			}
		}

		// otherwise do the same thing but for the verticle orientation
		else if (flag == false) {
			for (int r = bowR; r >= bowR - this.getLength() + 1; r--) {
				if (column == bowC && row == r) {
					hits[count] = true;
					return true;
				}
				count++;
			}
		}
		return false;
	}

	/**
	 * Checks to see if the ship is sunk.
	 * @return true if the ship is sunk, otherwise return false
	 */
	boolean isSunk() {

		for (boolean i : this.getHit()) {
			if (i == false) {
				return false;
			}
		}
		return true;
	}

	@Override
	/**
	 * Overrides print method for ship.
	 * @return "s" if the ship is sunk, otherwise return "x"
	 */
	public String toString() {

		boolean flag = this.isSunk();

		if (flag == true) {
			return "s";
		}

		return "x";
	}
}

