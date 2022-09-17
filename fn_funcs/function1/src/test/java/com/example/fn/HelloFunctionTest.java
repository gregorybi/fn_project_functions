package com.example.fn;

import com.fnproject.fn.testing.*;
import org.junit.*;

import static org.junit.Assert.*;

public class HelloFunctionTest {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_YELLOW = "\u001B[33m";

    @Rule
    public final FnTestingRule testing = FnTestingRule.createDefault();

    @Test
    public void shouldReturnGreeting() {
        testing.givenEvent().enqueue();
        testing.thenRun(HelloFunction.class, "handleRequest");

        FnResult result = testing.getOnlyResult();
        assertEquals(ANSI_YELLOW + "Hello, world!" + ANSI_RESET, result.getBodyAsString());
    }

    @Test
    public void shouldReturnGreetingwithBodyValue() {
        testing.givenEvent().withBody("Java").enqueue();
        testing.thenRun(HelloFunction.class, "handleRequest");
 
        FnResult result = testing.getOnlyResult();
        assertEquals(ANSI_YELLOW + "Hello, Java!" + ANSI_RESET,
                     result.getBodyAsString());
}

}