package rec11;

import java.util.ArrayList;

/**
 * Controller class.
 * @author Chuanrui Zhu, Huize Huang
 *
 */
public class MainSolution {

	public static void main(String[] args) {
		
		//create file reader and load given file
		AnalyzeSolution analyze = new AnalyzeSolution("reviews.txt");
			
		//return lines
		ArrayList<String> lines = analyze.getContent();
		
		//calculate score of each word
		analyze.calculateScore(lines);
		//example:
		System.out.println(analyze.determineSentiment("great!,:'great"));	// ~ 0.4
		System.out.println(analyze.determineSentiment("No!,  :'no")); 		// ~ -0.5
		
	}
}