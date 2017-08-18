import com.google.gson.JsonArray;
import com.google.gson.JsonObject;

public class CreatJSON {
	public static void main(String[] args) {
		JsonObject object=new JsonObject();
		object.addProperty("cat", "it");
		
		JsonArray array=new JsonArray();
		JsonObject lan1=new JsonObject();
		lan1.addProperty("id", 1);
		lan1.addProperty("name", "Java");
		lan1.addProperty("ide", "Eclipse");
		array.add(lan1);
		
		JsonObject lan2=new JsonObject();
		lan1.addProperty("id", 2);
		lan1.addProperty("name", "C#");
		lan1.addProperty("ide", "Visual Studio");
		array.add(lan2);
		
		JsonObject lan3=new JsonObject();
		lan1.addProperty("id", 3);
		lan1.addProperty("name", "Swift");
		lan1.addProperty("ide", "Xcode");
		array.add(lan3);
		
		object.add("languages", array);
		object.addProperty("pop", "true");
		
		System.out.println(object.toString());
	}
}
