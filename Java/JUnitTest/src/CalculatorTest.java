import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class CalculatorTest {
    private static Calculator calculator = new Calculator();

    @Before
    public void setUp() throws Exception {
        calculator.clear();
    }

    @Test
    public void testAdd() {
        calculator.add(3);
        calculator.add(4);
        assertEquals(7, calculator.getResult());

    }

    @Test
    public void testSubstract() {
        calculator.add(8);
        calculator.substract(3);
        assertEquals(5, calculator.getResult());

    }

    @Ignore("Multiply() Not yet implemented")
    @Test
    public void testMultiply() {
        fail("Not yet implemented");
    }

    @Test
    public void testDivide() {
        calculator.add(8);
        calculator.divide(2);
        assertEquals(4, calculator.getResult());
    }

}
