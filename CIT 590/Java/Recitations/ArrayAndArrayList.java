package recitation;
import java.util.ArrayList;


public class ArrayAndArrayList {

	int array[] = new int[10];
	int element;

	/** 
	 * This method counts the number of occurrences of 
	 * the requested element in the given array. 
	 * @param array integer array to search 
	 * @param element integer element to search for 
	 * @return number of times element is in array 
	 */
	public int howMany(int[] array, int element) {
		int count = 0;

		for (int i= 0; i< array.length; i++) {
			if (array[i] == element) {
				count++;
			}
		}
		return count;
	}

	/** 
	 * This method finds the max number in the given array. 
	 * If the array is empty, returns -1. 
	 * @param array integer array to search 
	 * @return max number in array 
	 */
	public int findMax(int[] array) {
		int max = 0;
		int count = 0;

		for (int i = 0; i < array.length; i++) {
			if (array[i] == 0) {
				count++;
			}
		}

		if (count == array.length) {
			return -1;

		}
		else {
			for (int i = 0; i < array.length; i++) {
				if (array[i] > max) {
					max = array[i];
				}
			}
			return max;
		}
	}

	/**
	 * This method keeps track of the occurrences of the 
	 * max number in the given array. 
	 * Returns an ArrayList with the occurrences. 
	 * If the array is empty, returns null. 
	 * @param array integer array to search 
	 * @return ArrayList with every instance of the max 
	 */
	public ArrayList<Integer> maxArray(int[] array) {
		int max = findMax(array);

		if (max == -1) {
			return null;
		}
		else {
			int count = howMany(array, max);
			ArrayList<Integer> maxArray = new ArrayList<Integer>();
			for (int i = 0; i < count; i++) {
				maxArray.add(max);
			}
			return maxArray;
		}
	}
	/**
	 * This method puts all of the zeros in the given array, at the end of the given array. 
	 * Updates the array itself. 
	 * @param integer array containing all zeros at the end 
	 */
	public void swapZero(int[] array) {
		
		ArrayList<Integer> tempArray = new ArrayList<Integer>();
		int count = 0;
		
		for (int i = 0; i < array.length; i++) {
			if (array[i] == 0) {
				count++;
			}
			else {
				tempArray.add(array[i]);
			}
		}
}
