

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class UserToFriendMap {
	public static void main(String[] args) {
		Map<String, List<String>> mapOfUserToFriend = new HashMap<String, List<String>>();
		List<String> justTheUserList = new ArrayList<String>();
                //String fileName = "/home/manish/ResearchWork/RA/Tweet_Friends/Friends/resultOutputImportedFromAws/experiment.txt";
		String fileName = "/home/manish/ResearchWork/RA/Tweet_Friends/Friends/resultOutputImportedFromAws/FinalUserToFriend_exp.txt";
		try{
			//Create object of FileReader
			FileReader inputFile = new FileReader(fileName);
			//Instantiate the BufferedReader Class
			BufferedReader bufferReader = new BufferedReader(inputFile);
			//Variable to hold the one line data
			String line;
			String userName="";
			String[] arrayOfFriends;
			List<String> tempFriendList = new ArrayList<String>();

			while ((line = bufferReader.readLine()) != null)   {
				//System.out.println(line);
				if (!line.startsWith("$#$")){
					userName = line.trim();
					justTheUserList.add(userName);
				}
				else
				{
					tempFriendList = new ArrayList<String>();
					line = line.substring(3, line.length());
					arrayOfFriends = line.split(",");
					for(String friend:arrayOfFriends){
						if(!friend.contains("$#$")){
							tempFriendList.add(friend);

						}	
						else{
							friend = friend.replace("$","");
							String[] temp = friend.split("#");
							tempFriendList.add(temp[0]);
						}
					}
				}
				mapOfUserToFriend.put(userName, tempFriendList);
			}
			bufferReader.close();
		}
		catch(Exception e){
			System.out.println("Error while reading file line by line:" + e.getMessage());
		}

//		printTheLists(mapOfUserToFriend,justTheUserList);
		MapUserToUserFriendShip(mapOfUserToFriend,justTheUserList);




	}
	/**
	 * This method has the userNames and the friendList as map as input
	 * end goal is to come up with ametrics like 
	 * userName: 1,0,1,1,1,1,0,0,0,0,0  based on if they are friend among each other
	 * @param mapOfUserToFriend
	 * @param justTheUserList
	 */
	private static void MapUserToUserFriendShip(
			Map<String, List<String>> mapOfUserToFriend,
			List<String> justTheUserList) {
		
		Collections.sort(justTheUserList);
		List<String> listOfFriends =  new ArrayList<String>();
		for(String rowstr:justTheUserList){
			listOfFriends =  mapOfUserToFriend.get(rowstr);
                        System.out.print(rowstr+"-->");
			//listOfFriends.add("bgunn11");
			for(String colsr:justTheUserList){
				if(listOfFriends.indexOf(colsr)==-1){
					//System.out.print("0"+",");
				}
				else{
					//System.out.print("1"+","+colsr+",");
					System.out.print(colsr+",");
					
				}
			}
			System.out.println();
		}

	}

	/**
	 * 
	 * @param mapOfUserToFriend
	 * @param justTheUserList
	 */
	private static void printTheLists(
			Map<String, List<String>> mapOfUserToFriend,
			List<String> justTheUserList) {
		for(Map.Entry<String, List<String>> entry: mapOfUserToFriend.entrySet()){
			System.out.println(entry.getKey()+":"+entry.getValue());
		}

		for(String str: justTheUserList){
			System.out.print(str+",");
		}
		System.out.println();
	}

}
