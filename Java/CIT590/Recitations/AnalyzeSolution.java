package rec11;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
/**
 * Sentiment analysis can be used to determine the general attitude of a given 
 * piece of text. For instance, we would like to have a program that could look at 
 * the text 'I love CIT590' and realize that it was a positive statement 
 * while 'I feel uncomfortable' is negative.
 * 
 * The reviews.txt contains many sentences, each sentence takes a line
 * and starts with a number which is the sentiment score of that sentence,
 * sentences with higher score are more positive.
 * 
 * Your job is to determine the average sentiment score of each word and
 * use it to calculate the sentiment score of any other given text.
 * 
 * To determine the overall sentiment of the each word, we take the average of the sentences
 * in which it appears. For example:
 * 		2 I love CIT 590 !
 * 		1 It is fun to learn Java
 * 		-2 I do not like final exam
 * Given the above three sentences, we know the score of some words:
 * 		I: (2-2)/2 = 0 because 'I' appears in two different sentences, and the scores of those sentences are 2 and -2
 * 		love: 2/1 = 2 because 'love' appears in once sentence, and the score of that sentence is 2
 * 		fun: 1/1 = 1
 *		exam: -2/1 = -1 
 * These are only part of words, remember you need to calculate the score of all words.
 * 
 * Now for a new sentence: I love fun exam blabla
 * The score of this sentence = (0(I) + 2(love) + 1(fun) - 2(exam))/4 = 0.25
 * Note, 'blabla' is ignored because it doesn't appear in any of the example sentences above.
 * 
 * @author Chuanrui Zhu, Huize Huang
 *
 */
public class AnalyzeSolution {
	/**
	 * Name of file to open and read.
	 */
	private String filename;
	/**
	 * Map that stores score of each word
	 */
	private HashMap<String, Double> wordScore;

	/**
	 * Creates instance of Analyze with given filename to open and read.
	 * @param filename to open and read
	 */
	public AnalyzeSolution(String filename) {
		this.filename = filename;
		this.wordScore = new HashMap<String, Double>();
	}
	
	/**
	 * Opens and reads the data in filename, 
	 * stores each line as an element into a list,
	 * do not need to worry about format now.
	 * Remember to catch some exceptions when reading files and close file.
	 * @return a list of lines.
	 */
	public ArrayList<String> getContent() {
		ArrayList<String> lines = new ArrayList<String>();
		BufferedReader file = null;
		try {
			file = new BufferedReader(new FileReader(new File(this.filename)));
			String line = file.readLine();
			while (line != null) {
				if (!line.isEmpty()) {
					lines.add(line);
				}
				line = file.readLine();
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			try {
				file.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return lines;
	}
	/**
	 * Calculates the score of each word in the given lines.
	 * 
	 * Step 1: To extract words of each sentence, first we need to iterate over
	 * 		the given lines and split each line by these characters:
	 * 		. , ? ! : ; ' " and single space
	 * 		Then iterate over each word in the split line, and store each word and the score for that line (at the beginning of the line). 
	 * 		Note, you can use a helper HashMap with the key being each unique word and the value being
	 * 		a list of all scores for that word.
	 * Step 2: Since we now have each word's total score and its frequency/number of scores (occurrences),
	 * 		we can iterate over each word and calculate the final score for it with the
	 * 		equation: score = total score / count of scores (appearances)
	 * 		Store the result in this.wordScore.
	 * @param lines in the file
	 */
	public void calculateScore(ArrayList<String> lines) {
		HashMap<String, ArrayList<Integer>> wordScoreListMap = new HashMap<String, ArrayList<Integer>>();
		
		// Iterate over each line in lines
		for(String line: lines) {
			String[] words = line.split("[.,!?:;'\"\\s]+");
			int score = Integer.valueOf(words[0]);
			
			// Iterate over each word in line
			for(int i = 1; i < words.length; i++) {
				String word = words[i];
				if(!wordScoreListMap.containsKey(word)) {
					wordScoreListMap.put(word, new ArrayList<Integer>());
				}
				wordScoreListMap.get(word).add(score);
			}
		}

		// Iterate over the map to get the list of score and calculate the average value
		for(String word: wordScoreListMap.keySet()) {
			ArrayList<Integer> scoreList = wordScoreListMap.get(word);
			double sum = 0;
			for(int i:scoreList) {
				sum+=i;
			}
			this.wordScore.put(word, sum/scoreList.size());
		}
	}
	
	/**
	 * Step 1: For a given sentence, split it again (the same as above).
	 * Step 2: Iterate over each word in the sentence, calculate the total score
	 * 		and number of words, ignore words that did not appear in review.txt,
	 * 		see above example for detailed info.
	 * Step 3: Then calculates average score of this sentence through the equation:
	 * 		score = total score/number of words
	 * @param s: given string to be calculated
	 * @return num: an integer indicates the score of given string s
	 */
	public double determineSentiment(String s) {
		String[] words = s.split("[.,!?:;'\"\\s]+");
		double sum = 0;
		int num = 0;
		
		// Iterate over words in given string and calculate the average value
		for(String word: words) {
			if(this.wordScore.containsKey(word)) {
				sum+=this.wordScore.get(word);
				num++;
			}
		}
		
		// Return the average score of the string
		return num == 0 ? 0 : sum/num;
	}
}
