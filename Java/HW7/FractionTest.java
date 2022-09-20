package hw7;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class FractionTest {

	@Test
	void testFraction() {

		Fraction fraction1 = new Fraction(3,-4);
		int denominator = fraction1.denominator;
		int numerator = fraction1.numerator;

		assertTrue(denominator > 0, "denominator should be positive");
		assertFalse(numerator >= 0, "numerator should not be positive");
	}

	@Test
	void testReduceToLowestForm() {

		Fraction fraction1 = new Fraction(0,4);

		fraction1.reduceToLowestForm();

		assertTrue(fraction1.denominator == 1);

		Fraction fraction2 = new Fraction(6,-8);
		Fraction fraction3 = new Fraction(-3,4);	

		fraction2.reduceToLowestForm();

		assertEquals(fraction2,fraction3);

		Fraction fraction4 = new Fraction(30,3);
		Fraction fraction5 = new Fraction(10,1);

		assertEquals(fraction4,fraction5);
	}

	@Test
	void testAdd() {

		Fraction fraction1 = new Fraction(3,-4);

		Fraction fraction2 = new Fraction(1,8);
		Fraction fraction3 = fraction1.add(fraction2);

		assertTrue(fraction3.numerator == -5);
		assertEquals(fraction3.denominator,8);

		Fraction fraction4 = new Fraction(0,67);
		Fraction fraction5 = fraction1.add(fraction4);

		assertTrue(fraction5.numerator == fraction1.numerator);
		assertEquals(fraction5.denominator,fraction1.denominator);
	}

	@Test
	void testSubtract() {

		Fraction fraction1 = new Fraction(3,-4);

		Fraction fraction2 = new Fraction(1,8);
		Fraction fraction3 = fraction1.subtract(fraction2);

		assertTrue(fraction3.numerator == -7);
		assertEquals(fraction3.denominator,8);

		Fraction fraction4 = new Fraction(0,1);
		Fraction fraction5 = fraction1.subtract(fraction4);

		assertTrue(fraction5.numerator == fraction1.numerator);
		assertEquals(fraction5.denominator,fraction1.denominator);
	}

	@Test
	void testMul() {
		Fraction fraction1 = new Fraction(3,-4);

		Fraction fraction2 = new Fraction(1,-8);
		Fraction fraction3 = fraction1.mul(fraction2);
		Fraction fraction3b = new Fraction(3,32);

		assertEquals(fraction3,fraction3b);

		Fraction fraction4 = new Fraction(3,8);
		Fraction fraction5 = fraction1.mul(fraction4);

		assertTrue(fraction5.numerator == -9);
		assertEquals(fraction5.denominator,fraction3.denominator);

		Fraction fraction6 = new Fraction(0,4);
		Fraction fraction7 = fraction1.mul(fraction6);
		Fraction fraction8 = new Fraction(0,1);

		assertEquals(fraction7,fraction8);
	}

	@Test
	void testDiv() {
		Fraction fraction1 = new Fraction(3,-4);

		Fraction fraction2 = new Fraction(1,-8);
		Fraction fraction3 = fraction1.div(fraction2);
		Fraction fraction3b = new Fraction(6,1);

		assertEquals(fraction3,fraction3b);

		Fraction fraction4 = new Fraction(3,8);
		Fraction fraction5 = fraction1.div(fraction4);

		assertTrue(fraction5.numerator == -2);
		assertEquals(fraction5.denominator,fraction3.denominator);

		Fraction fraction6 = new Fraction(0,1);
		Fraction fraction7 = fraction6.div(fraction1);
		Fraction fraction8 = new Fraction(0,1);

		assertEquals(fraction7,fraction8);
	}

	@Test
	void testDecimal() {
		Fraction fraction1 = new Fraction(3,-4);
		double dec1 = fraction1.decimal();

		assertEquals(dec1,-0.75);

		Fraction fraction2 = new Fraction(0,1);
		double dec2 = fraction2.decimal();

		assertEquals(dec2,0);

		Fraction fraction3 = new Fraction(5,7);
		double dec3 = fraction3.div(fraction1).decimal();

		assertTrue(dec3 == -0.9523809523809523);
	}

	@Test
	void testSqr() {

		Fraction fraction1 = new Fraction(3,-4);
		fraction1.sqr();

		assertEquals(fraction1.numerator,9);
		assertTrue(fraction1.denominator == 16);


		Fraction fraction2 = new Fraction(0,6);
		fraction2.sqr();

		Fraction fraction3 = new Fraction(0,1);
		assertEquals(fraction2,fraction3);

		Fraction fraction4 = new Fraction(4,1);
		fraction4.sqr();

		Fraction fraction5 = new Fraction(16,1);

		assertEquals(fraction4,fraction5);
	}

	@Test
	void testAverageFraction() {

		Fraction fraction1 = new Fraction(3,4);
		Fraction fraction2 = new Fraction(1,-2);

		Fraction fraction3 = fraction1.average(fraction2);
		Fraction fraction4 = new Fraction(1,8);

		assertEquals(fraction3,fraction4);

		Fraction fraction5 = new Fraction(0,3);
		Fraction fraction6 = fraction1.average(fraction5);
		Fraction fraction7 = new Fraction(3,8);

		assertEquals(fraction6,fraction7);

		Fraction fraction9 = fraction4.average(fraction4);

		assertEquals(fraction9,fraction4);
	}

	@Test
	void testAverageFractionArray() {

		Fraction fraction1 = new Fraction(3,4);
		Fraction fraction2 = new Fraction(1,-2);
		Fraction fraction3 = new Fraction(0,4);
		Fraction fraction4 = new Fraction(1,8);

		Fraction[] fractions1 = {fraction1,fraction2,fraction3,fraction4};
		Fraction avg1 = Fraction.average(fractions1);

		Fraction fraction5 = new Fraction(3,32);

		assertEquals(fraction5,avg1);

		Fraction[] fractions2 = {};
		Fraction avgEmpty = Fraction.average(fractions2);

		fraction3.reduceToLowestForm();

		assertEquals(fraction3,avgEmpty);

		Fraction[] fractions3 = {fraction1,fraction1,fraction1,fraction1};
		Fraction avg2 = Fraction.average(fractions3);

		assertEquals(fraction1,avg2);
	}

	@Test
	void testAverageIntArray() {

		int[] ints1 = {0,1,2,3,4,5,6};
		Fraction avg = Fraction.average(ints1);
		Fraction fraction1 = new Fraction(3,1);

		assertEquals(fraction1,avg);

		int[] ints2 = {};
		Fraction avg2 = Fraction.average(ints2);
		Fraction fraction2 = new Fraction(0,1);

		assertEquals(fraction2,avg2);

		int[] ints3 = {2,2,2,2,2,2,2};
		Fraction avg3 = Fraction.average(ints3);
		Fraction fraction3 = new Fraction(2,1);

		assertEquals(fraction3,avg3);
	}

	@Test
	void testEqualsObject() {

		Fraction fraction1 = new Fraction(3,1);
		Fraction fraction2 = new Fraction(6,2);

		fraction2.reduceToLowestForm();

		assertEquals(fraction1,fraction1);

		Fraction fraction3 = new Fraction(0,1);
		Fraction fraction4 = new Fraction(0,2);

		fraction4.reduceToLowestForm();

		assertEquals(fraction3,fraction4);

		Fraction fraction5 = new Fraction(-3,1);
		Fraction fraction6 = new Fraction(3,-1);

		assertEquals(fraction5,fraction6);
	}

	@Test
	void testToString() {

		Fraction fraction1 = new Fraction(3,1);
		String frac = fraction1.toString();

		assertEquals(frac,"3/1");

		Fraction fraction2 = new Fraction(2,3);
		Fraction fraction3 = fraction1.mul(fraction2);
		String frac2 = fraction3.toString();

		assertEquals(frac2,"2/1");

		Fraction fraction4 = new Fraction(0,3);
		fraction4.reduceToLowestForm();
		String frac3 = fraction4.toString();

		assertEquals(frac3,"0/1");
	}
}
