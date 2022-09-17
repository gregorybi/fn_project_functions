package com.example.fn;

import com.fnproject.fn.testing.*;
import org.junit.*;

import static org.junit.Assert.*;

public class SerFunctionTest {

    @Rule
    public final FnTestingRule testing = FnTestingRule.createDefault();

    @Test
    public void shouldReturnGreeting(){
        testing.givenEvent().withBody("{\"a1\":1, \"n\":4, \"d\":2}").enqueue();
        testing.thenRun(SerFunction.class,"handleRequest");

        FnResult result = testing.getOnlyResult();
        assertEquals("{\"n\":4,\"message\":\"Nth term and Sum of n terms are:\",\"a_n\":7,\"sum_of_n_terms\":16}", result.getBodyAsString());
    }
}