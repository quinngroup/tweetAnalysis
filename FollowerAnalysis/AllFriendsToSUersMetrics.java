import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class AllFriendsToSUersMetrics {
	public static void main(String[] args) {
		Map<String, List<String>> mapOfUserToFriend = new HashMap<String, List<String>>();
		List<String> justTheUserList = new ArrayList<String>();
                //String fileName = "/home/manish/ResearchWork/RA/Tweet_Friends/Friends/resultOutputImportedFromAws/experiment.txt";
		String fileName = "/home/manish/ResearchWork/RA/Tweet_Friends/Friends/resultOutputImportedFromAws/FinalUserToFriend_exp.txt";
		try{
			FileReader inputFile = new FileReader(fileName);
			BufferedReader bufferReader = new BufferedReader(inputFile);
			String line;
			String userName="";
			String[] arrayOfFriends;
			List<String> tempFriendList = new ArrayList<String>();
			while ((line = bufferReader.readLine()) != null)   {
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

		//printTheLists(mapOfUserToFriend,justTheUserList);
		
		//MapUserToUserFriendShip(mapOfUserToFriend,justTheUserList);

                GephiInputFormatPrepare(mapOfUserToFriend,justTheUserList);
	}

        /**
         * This method will take the input as ywo maps and try to create a input format which 
         * gephi software expects to be able to do network analysis
         *
         */
        private static void GephiInputFormatPrepare(Map<String, List<String>> mapOfUserToFriend, List<String> justTheUserList){
           for(Map.Entry<String,List<String>> entry: mapOfUserToFriend.entrySet()){
                String user = entry.getKey();
                System.out.print(user);
                List<String> listOfFriends =  new ArrayList<String>();
                listOfFriends =  mapOfUserToFriend.get(user);
                for(String frn: listOfFriends){
                    System.out.print(";"+frn);
                }
                System.out.println();
           } 
        
        }
            

	/**
	 * This method has the userNames and the friendList as map as input
	 * end goal is to come up with ametrics like 
	 * userName -- x,y,z  based on if they are friend among each other
         * because this output can be consumed by gephi directly
	 * @param mapOfUserToFriend
	 * @param justTheUserList
	 */
	private static void MapUserToUserFriendShip(Map<String, List<String>> mapOfUserToFriend, List<String> justTheUserList) {
		 Set<String> setOfAllFriends = new HashSet<String>();
                 for(Map.Entry<String, List<String>> entry: mapOfUserToFriend.entrySet()){
                    for(String str: entry.getValue()){
                        setOfAllFriends.add(str);
                  }
                } 
		Collections.sort(justTheUserList);
		List<String> listOfFriends =  new ArrayList<String>();
		for(String rowstr:justTheUserList){
		        listOfFriends =  mapOfUserToFriend.get(rowstr);
                        System.out.print(rowstr+"-->");
			for(String colsr:setOfAllFriends){
				if(listOfFriends.indexOf(colsr)==-1){
				}
				else{
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
		System.out.println("here just once??");
		Set<String> setOfAllFriends = new HashSet<String>();
		for(Map.Entry<String, List<String>> entry: mapOfUserToFriend.entrySet()){
			//System.out.println(entry.getKey()+":"+entry.getValue());
			for(String str: entry.getValue()){
				setOfAllFriends.add(str);
			}
		}

		for(String str: setOfAllFriends){
			System.out.print(str + ",");
		}
//		for(String str: justTheUserList){
//			System.out.print(str+",");
//		}
		System.out.println();
	}

}
