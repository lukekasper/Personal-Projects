package hw7;

public class Fraction {

	/**
	 * Declare instance variables of numerator and denominator of a fraction.
	 */
	int numerator;
	int denominator;

	/**
	 * Constructor to create Fraction object with numerator and denominator parameters.
	 * Sets numerator and denominator instance variables.
	 * Properly formats negative fractions.
	 * @param numerator
	 * @param denominator
	 */
	public Fraction(int numerator, int denominator) {

		// set instance variables with given parameters
		this.numerator = numerator;
		this.denominator = denominator;

		// properly assign negative value to numerator only
		if (denominator < 0) {
			this.numerator = -numerator;
			this.denominator = -denominator;
		}
	}

	/**
	 * Reduces fraction by eliminating common factors.
	 */
	public void reduceToLowestForm() {

		// initializes boolean flag to false
		boolean flag = false;

		// while the flag is false continue to check for greatest common factor
		while (flag == false) {

			// if the numerator is 0, then the denominator is automatically 1
			if (this.numerator == 0) {
				this.denominator = 1;
				break;
			}

			// otherwise, find the gcd of the numerator and denominator
			else {
				int factor = gcd(this.numerator,this.denominator);
				if (factor == 1) {
					flag = true;
				}

				// then divide num and denom by the gcd and set those as the new
				// numerator and denominator
				this.numerator = this.numerator/factor;
				this.denominator = this.denominator/factor;
			}
		}
	}

	/**
	 * Adds the current fraction to the given otherFraction.
	 * @param otherFraction to be added to the current fraction.
	 * @return Returns a new Fraction that is the sum of the two Fractions.
	 */
	public Fraction add(Fraction otherFraction) {

		// set the new denominator as a common denominator of both fractions
		int new_denom = otherFraction.denominator*this.denominator;

		// multiply the numerators so that the fractions are now unreduced,
		// but with the above denominator
		int num1 = otherFraction.numerator*this.denominator;
		int num2 = this.numerator*otherFraction.denominator;

		// add the numerators
		int new_num = num1 + num2;

		// create a new fraction with the new num and denom, and reduce that fraction
		Fraction fraction2 = new Fraction(new_num,new_denom);
		fraction2.reduceToLowestForm();

		return fraction2;
	}

	/**
	 * Subtracts the given otherFraction from the current fraction.
	 * @param otherFraction to be subtracted from current fraction.
	 * @return Returns a new Fraction that is the difference of the two Fractions.
	 */
	public Fraction subtract(Fraction otherFraction) {

		// set the new denominator as a common denominator of both fractions
		int new_denom = otherFraction.denominator*this.denominator;

		// multiply the numerators so that the fractions are now unreduced,
		// but with the above denominator 
		int num1 = otherFraction.numerator*this.denominator;
		int num2 = this.numerator*otherFraction.denominator;

		// subtract the numerators
		int new_num = num2 - num1;

		// create a new fraction with the new num and denom, and reduce that fraction
		Fraction fraction2 = new Fraction(new_num,new_denom);
		fraction2.reduceToLowestForm();

		return fraction2;
	}

	/**
	 * Multiplies the current fraction by the given otherFraction.
	 * @param otherFraction to multiply with the current fraction.
	 * @return Returns a new Fraction that is the product of this fraction and the otherFraction.
	 */
	public Fraction mul(Fraction otherFraction) {

		// multiply the numerators and denominators together
		int new_num = otherFraction.numerator*this.numerator;
		int new_denom = otherFraction.denominator*this.denominator;

		// create a new fraction with the new num and denom and reduce that fraction
		Fraction fraction2 = new Fraction(new_num,new_denom);
		fraction2.reduceToLowestForm();

		return fraction2;
	}

	/**
	 * Divides the current fraction by the given otherFraction.
	 * @param otherFraction to divide current fraction by
	 * @return Returns a new Fraction that is the quotient of this fraction and the otherFraction.
	 */
	public Fraction div(Fraction otherFraction) {

		// flip the numerator and denominator of the other fraction
		int num1 = otherFraction.denominator;
		int denom1 = otherFraction.numerator;

		// multiply through the numerator and denominator 
		int new_num = num1*this.numerator;
		int new_denom = denom1*this.denominator;

		// create a new fraction with the new num and denom and reduce it
		Fraction fraction2 = new Fraction(new_num,new_denom);
		fraction2.reduceToLowestForm();

		return fraction2;
	}

	/**
	 * Converts the fraction into a decimal.
	 * @return Returns this fraction in decimal form.
	 */
	public double decimal() {

		// set variables for the numerator and denominator of the current fraction
		double num = this.numerator;
		double denom = this.denominator;

		// create a decimal double of the fraction
		double dec = num/denom;

		return dec;
	}

	/**
	 * Square the current fraction.
	 */
	public void sqr() {

		// create a new fraction with the current fractions numerator and denominator
		Fraction fraction1 = new Fraction(this.numerator,this.denominator);

		// reduce that fraction
		fraction1.reduceToLowestForm();

		// square the numerator and denominator and set the current fractions
		// num and denom to that value
		this.numerator = fraction1.numerator*fraction1.numerator;
		this.denominator = fraction1.denominator*fraction1.denominator;

	}

	/**
	 * Averages the current fraction with the given otherFraction.
	 * @param otherFraction to average with current fraction
	 * @return Returns a new Fraction that is the average of this fraction and the otherFraction.
	 */
	public Fraction average(Fraction otherFraction) {

		// create a new fraction as the sum of the current and other fractions
		Fraction fraction1 = this.add(otherFraction);

		// multiply the denominator x2 to complete the average (2 terms)
		int denominator1 = fraction1.denominator;
		int denominator2 = denominator1*2;

		// create a new fraction with the summed numerator and new denominator and reduce it
		Fraction fraction2 = new Fraction(fraction1.numerator,denominator2);
		fraction2.reduceToLowestForm();

		return fraction2;
	}

	/**
	 * Averages all of the fractions in the given array.
	 * Do not include the current fraction in the average.
	 * If the array is empty, return a new Fraction that equals 0.
	 * @param fractions - array of fractions
	 * @return Returns the average of the array.
	 */
	public static Fraction average(Fraction[] fractions) {

		// if the fraction list is empty, the average will return a fraction of 0/1
		if (fractions.length == 0) {
			Fraction fraction1 = new Fraction(0,1);
			return fraction1;
		}

		// otherwise initialize the sum as the first fraction in the array list
		Fraction fractionSum = fractions[0];

		// iterate over the array and sum the fractions
		for (int i = 1; i < fractions.length; i++) {
			fractionSum = fractionSum.add(fractions[i]);
		}

		// create a new fraction which is 1 divided by the length of the list
		Fraction fraction1 = new Fraction(1,fractions.length);

		// divide the fraction sum by the number of terms to get the average
		Fraction fractionAvg = fractionSum.mul(fraction1);

		return fractionAvg;
	}


	/**
	 * Average all the integers in the given array.
	 * Do not include the current fraction in the average.
	 * If the array is empty, return a new Fraction that equals 0.
	 * @param ints - array of integers
	 * @return Returns the average of the array as a new Fraction.
	 */
	public static Fraction average(int[] ints) {

		// if the int list is empty return a fraction of 0/1
		if (ints.length == 0) {
			Fraction fraction1 = new Fraction(0,1);
			return fraction1;
		}

		// otherwise initialize the int sum to 0
		int intsSum = 0;

		// iterate over the ints list and sum them
		for (int i = 0; i < ints.length; i++) {
			intsSum += ints[i];
		}

		// set a new numerator to the sum and denominator to the length of the array list
		int numerator1 = intsSum;
		int denominator1 = ints.length;

		// create a fraction with the new num and denom representing the average 
		// of the list and reduce that fraction
		Fraction fraction2 = new Fraction (numerator1,denominator1);
		fraction2.reduceToLowestForm();

		return fraction2;
	}

	/**
	 * Static function to return the greatest common factor between two numbers.
	 * @param n1 number 1
	 * @param n2 number 2
	 * @return Returns greatest common factor between n1 and n2.
	 */
	public int gcd(int n1, int n2) {

		// initiate the gcd to 1
		int gcd = 1;

		// loop until value for the gcd is equal to the absolute value of the smaller number
		for (int i = 1; i <= Math.abs(n1) && i <= Math.abs(n2); ++i) {

			// checks if i is factor of both integers
			// sets the gcd as the highest number that returns a remainder of 0 between both numbers
			if (n1 % i == 0 && n2 % i == 0)
				gcd = i;
		}
		return gcd;
	}

	/**
	 * Overridden method to compare the given object (as a fraction) to the current fraction, for equality.
	 * Two fractions are considered equal if they have the same numerator and
	 * same denominator, after eliminating common factors.
	 */
	@Override
	public boolean equals(Object object) {

		// creates a new fraction with the current fractions num and denom
		Fraction fraction1 = new Fraction(this.numerator,this.denominator);

		// cast the other object as a second fraction
		Fraction fraction2 = (Fraction) object;

		// reduce both fractions
		fraction1.reduceToLowestForm();
		fraction2.reduceToLowestForm();

		// if both the numerator and denominator of the current and other fraction are equal
		// then return true
		if (fraction1.numerator == fraction2.numerator && fraction1.denominator == fraction2.denominator) {
			return true;
		}

		// otherwise return false
		else {
			return false;
		}
	}

	/**
	 * Overridden method to return a string representation of the current fraction.
	 */
	@Override
	public String toString() {

		// initialize variables for the current fractions numerator and denominator
		int numerator1 = this.numerator;
		int denominator1 = this.denominator;

		// create a string representing the fraction as "num/denom" for printing
		String frac = numerator1 + "/" + denominator1;

		return frac;
	}
}

