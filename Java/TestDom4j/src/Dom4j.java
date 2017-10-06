import org.dom4j.Document;
import org.dom4j.DocumentHelper;

public class Dom4j {
	public static void main(String[] args) {
		try {
			String xmlString="<root><people>lizhens</people></root>";
			Document document=DocumentHelper.parseText(xmlString);
			System.out.println(document.asXML());
		} catch (Exception e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}
