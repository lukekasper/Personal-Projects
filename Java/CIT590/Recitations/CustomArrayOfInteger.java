package rec8;

import java.util.ArrayList;
import java.util.Arrays;
/**
 * We want to build a fancy ArrayList that support some other operations
 * which are not included in Java built-in methods
 * Implement the methods with TODO
 * @author Chuanrui Zhu, Huize Huang
 *
 */
public class CustomArrayOfInteger {
	
	//instance variables
	
	/**
	 * Internal ArrayList.
	 */
	private ArrayList<Integer> arr;
	
	//constructors
	/**
	 * Creates an empty CustomArrayList
	 */
	public CustomArrayOfInteger() {
		this.arr = new ArrayList<Integer>();
	}
	
	/**
	 * Creates a new CustomArrayList containing all elements in the internal ArrayList arr.
	 * We need to make sure if we change current ArrayList, the argument "arr" won't change.
	 * @param arr to use for internal ArrayList.
	 */
	public CustomArrayOfInteger(ArrayList<Integer> arr) {
		this.arr = new ArrayList<Integer>(arr);
	}
	
	/**
	 * Returns the element at the specified index in the internal ArrayList arr.
	 * @param index of item to get
	 * @return element at specified index
	 */
	public int get(int index) {
		return this.arr.get(index);
	}
	
	/**
	 * Gets the internal ArrayList arr.
	 * @return Internal ArrayList arr
	 */
	public ArrayList<Integer> getArray() {
		return this.arr;
	}
	
	/**
	 * Appends the given element to the end of the internal ArrayList arr.
	 * @param element to append
	 */
	public void add(int element) {
		this.arr.add(element);
	}
	
	/**
	 * Inserts the given element at the specified index.
	 * The built-in .add() in ArrayList raises an exception when an index is out of range,
	 * but we want this method to return false if the given index is out of range.
	 * @param index at which to insert the given element
	 * @param element to insert
	 * @return return false if the given index is out of range, otherwise return true
	 */
	public boolean add(int index, int element) {
		if (index > this.arr.size() - 1) {
			return false;
	}
		this.arr.add(index,element);
		return true;
	}
	
	/**
	 * Remove element at the specified index.
	 * @param index at which to remove element
	 * @return the removed element
	 */
	public int remove(int index) {
		return this.arr.remove(index);
	}
	
	/**
	 * Removes the first specified number (num) of elements in the internal ArrayList arr.
	 * if num <= 0, do nothing.
	 * if num is too large, remove all the specified elements in the list.
	 * e.g. [1,2,1,2,1].remove(2, 1)=>[2,2,1]
	 * @param num number of instances of element to remove
	 * @param element to remove
	 */
	public void remove(int num, int element) {
		if (num <= 0) {
			return;
		}
		int count = 0;
		ArrayList<Integer> arr2 = (ArrayList<Integer>) this.arr;
		arr2.toArray();
		for (int i = 0; i < this.arr.size()-1; i++) {
			
			
			if ( = element) {
				
			}
		}
	}
	
	/**
	 * Removes the first specified number (num) of elements in the internal ArrayList arr, starting at the given index.
	 * e.g.[1,2,3,4,5].splice(1,2)=>[1,4,5]
	 * @param index to start on
	 * @param num of items
	 * @return ArrayList removed elements, return an empty ArrayList if index out of range
	 */
	public ArrayList<Integer> splice(int index, int num){
		//TODO
		return null;
	}
	
	/**
	 * Removes the specified number of elements (num), starting with the given index,
	 * and inserts the elements in the given array at the given index.
	 * e.g.[1,2,3,4,5].splice(1,2,[6,7])=>[1,6,7,4,5]
	 * @param index at which to remove and add elements
	 * @param num of elements to remove
	 * @param otherArray with elements to add to internal ArrayList arr
	 * @return the removed elements
	 */
	public ArrayList<Integer> splice(int index, int num, int[] otherArray){
		//TODO
		return null;
	}
	
	
	public static void main(String args[]) {
		CustomArrayOfInteger sol = new CustomArrayOfInteger();
		sol.add(2);					
		System.out.println(sol.getArray());	//[2]
		
		sol.add(0, 5);				
		System.out.println(sol.getArray());	//[5,2]
		
		sol.remove(2, 2);
		System.out.println(sol.getArray());	//[5]
		
		sol.add(6);
		sol.add(2);
		sol.add(7); 						//[5,6,2,7]
		sol.splice(0, 2);
		System.out.println(sol.getArray());	//[2,7]
		
		sol.splice(0, 1, new int[] {4,5});
		System.out.println(sol.getArray());	//[4,5,7]
	}
}