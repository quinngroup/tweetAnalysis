import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;
import java.util.Set;



public class SortByValueWordCount {
	public static void main(String[] args) {
		Map<String, Integer> unsortMap = new HashMap<String, Integer>();
		Set<String> mostCommonWords = new HashSet<String>();
		String fileName = "/home/manish/ResearchWork/RA/DrunkTweetAnalysis/word_cloud-master/examples/wordCount.txt";
		String fileCommon = "/home/manish/ResearchWork/src/1000mostCommon.txt";
		try{

			//Create object of FileReader
			FileReader inputFileCommon = new FileReader(fileCommon);

			//Instantiate the BufferedReader Class
			BufferedReader bufferReaderCommon = new BufferedReader(inputFileCommon);

			//Variable to hold the one line data
			String word;
			while ((word = bufferReaderCommon.readLine()) != null)   {
				mostCommonWords.add(word.toUpperCase());
			}
			
			FileReader inputFile = new FileReader(fileName);

			//Instantiate the BufferedReader Class
			BufferedReader bufferReader = new BufferedReader(inputFile);
			String line;
			// Read file line by line and print on the console
			while ((line = bufferReader.readLine()) != null)   {
				//System.out.println(line);
				line = line.toUpperCase();
				String[] temp = line.split(" ");
				if(!(mostCommonWords.contains(temp[0])) && temp[0].charAt(0) !='@')  // to get rid of mentions
				unsortMap.put(temp[0], Integer.parseInt(temp[1]));
			}
			bufferReader.close();
		}
		catch(Exception e){
			System.out.println("Error while reading file line by line:" + e.getMessage());
		}
//		System.out.println("Unsort Map......");
//		printMap(unsortMap);

		System.out.println("\nSorted Map......");
		Map<String, Integer> sortedMap = sortByComparator(unsortMap);
		printMap(sortedMap);
	}
	/**
	 * 
	 * @param unsortMap
	 * @return
	 */
	private static Map<String, Integer> sortByComparator(Map<String, Integer> unsortMap) {

		// Convert Map to List
		List<Map.Entry<String, Integer>> list = 
			new LinkedList<Map.Entry<String, Integer>>(unsortMap.entrySet());

		// Sort list with comparator, to compare the Map values
		Collections.sort(list, new Comparator<Map.Entry<String, Integer>>() {
			public int compare(Map.Entry<String, Integer> o1,
                                           Map.Entry<String, Integer> o2) {
				return (o1.getValue()).compareTo(o2.getValue());
			}
		});

		// Convert sorted map back to a Map
		Map<String, Integer> sortedMap = new LinkedHashMap<String, Integer>();
		for (Iterator<Map.Entry<String, Integer>> it = list.iterator(); it.hasNext();) {
			Map.Entry<String, Integer> entry = it.next();
			sortedMap.put(entry.getKey(), entry.getValue());
		}
		return sortedMap;
	}	
	/**
	 * 
	 * @param map
	 */
	public static void printMap(Map<String, Integer> map) {
		for (Map.Entry<String, Integer> entry : map.entrySet()) {
			System.out.println(entry.getKey() 
                                      + ":" +entry.getValue());
		}
	}
	
}