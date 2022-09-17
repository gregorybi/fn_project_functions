package com.example.fn;

import com.fnproject.fn.testing.*;
import org.junit.*;

import static org.junit.Assert.*;

public class List_FunctionTest {

    @Rule
    public final FnTestingRule testing = FnTestingRule.createDefault();

    @Test
    public void shouldReturnGreeting(){
        testing.givenEvent().withBody("{\"list\":[2, 1]}").enqueue();
        testing.thenRun(List_Function.class,"handleRequest");

        FnResult result = testing.getOnlyResult();
        assertEquals("{\"f_str\":\"Sorted List is: \",\"sorted\":[1,2]}", result.getBodyAsString());
    }
}