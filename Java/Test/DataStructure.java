import java.util.Enumeration;
import java.util.Vector;
import java.util.BitSet;
import java.util.Stack;
import java.util.Hashtable;
import java.util.Properties;
import java.util.Iterator;
import java.util.Set;
import java.lang.String;
import java.util.Map;
import java.util.HashMap;
import java.util.EmptyStackException;

public class DataStructure{
	static void showpush(Stack<Integer> st, int a) {
        st.push(new Integer(a));
        System.out.println("push(" + a + ")");
        System.out.println("stack: " + st);
    }
 
    static void showpop(Stack<Integer> st) {
        System.out.print("pop -> ");
        Integer a = (Integer) st.pop();
        System.out.println(a);
        System.out.println("stack: " + st);
    }
	public static void main(String[] args) {
		// Enumeration
		Enumeration<String> days;

		// Vector
		Vector<String> dayNames = new Vector<String>();
		dayNames.add("Sunday");
		dayNames.add("Monday");
		dayNames.add("Tuesday");
		dayNames.add("Wednesday");
		dayNames.add("Thursday");
		dayNames.add("Friday");
		dayNames.add("Saturday");
	    System.out.println(dayNames.size());
	    System.out.println(dayNames.capacity());
	    System.out.println(dayNames.firstElement());
	    System.out.println(dayNames.lastElement());
	    System.out.println();
		days = dayNames.elements();
		while (days.hasMoreElements()){
		 System.out.println(days.nextElement()); 
		}
		System.out.println();

		// BitSet
		BitSet bits1 = new BitSet(16);
		BitSet bits2 = new BitSet(16);
		// set some bits
		for(int i=0; i<16; i++) {
		if((i%2) == 0) bits1.set(i);
		if((i%5) != 0) bits2.set(i);
		}
		System.out.println("Initial pattern in bits1: " + bits1);
		System.out.println("Initial pattern in bits2: " + bits2);
		// AND bits
		bits2.and(bits1);
		System.out.println("bits2 AND bits1: " + bits2);
		// OR bits
		bits2.or(bits1);
		System.out.println("bits2 OR bits1: " + bits2);
		// XOR bits
		bits2.xor(bits1);
		System.out.println("bits2 XOR bits1: " + bits2);
		System.out.println();

		// Stack
		Stack<Integer> st = new Stack<Integer>();
        System.out.println("stack: " + st);
        showpush(st, 42);
        showpush(st, 66);
        showpush(st, 99);
        showpop(st);
        showpop(st);
        showpop(st);
        try {
            showpop(st);
        } catch (EmptyStackException e) {
            System.out.println("empty stack");
        }
        System.out.println();

        // Hashtable
		Hashtable balance = new Hashtable();
		Enumeration names;
		String str;
		double bal;
		balance.put("Zara", new Double(3434.34));
		balance.put("Mahnaz", new Double(123.22));
		balance.put("Ayan", new Double(1378.00));
		balance.put("Daisy", new Double(99.22));
		balance.put("Qadir", new Double(-19.08));
		// Show all balances in hash table.
		names = balance.keys();
		while(names.hasMoreElements()) {
		 str = (String) names.nextElement();
		 System.out.println(str + ": " + balance.get(str));
		}
		// Deposit 1,000 into Zara's account
		bal = ((Double)balance.get("Zara")).doubleValue();
		balance.put("Zara", new Double(bal+1000));
		System.out.println("Zara's new balance: " + balance.get("Zara"));
		System.out.println();

		// Properties
		Properties capitals = new Properties();

		// Set
		Set states;
		String strs;
		capitals.put("Illinois", "Springfield");
		capitals.put("Missouri", "Jefferson City");
		capitals.put("Washington", "Olympia");
		capitals.put("California", "Sacramento");
		capitals.put("Indiana", "Indianapolis");
		// Show all states and capitals in hashtable.
		states = capitals.keySet(); // get set-view of keys
		Iterator itr = states.iterator();
		while(itr.hasNext()) {
			strs = (String) itr.next();
			System.out.println("The capital of " + strs + " is " + capitals.getProperty(strs) + ".");
		}
		// look for state not in list -- specify default
		strs = capitals.getProperty("Florida", "Not Found");
		System.out.println("The capital of Florida is " + strs + ".");
		System.out.println();

		// HashMap
		Map<String, String> m1 = new HashMap<String, String>(); 
		m1.put("Zara", "8");
		m1.put("Mahnaz", "31");
		m1.put("Ayan", "12");
		m1.put("Daisy", "14");
		System.out.println("Map Elements: " + m1);
		System.out.println();
	}
}