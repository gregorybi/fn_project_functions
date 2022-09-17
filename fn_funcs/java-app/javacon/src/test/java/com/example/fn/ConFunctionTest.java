package com.example.fn;

import com.fnproject.fn.testing.*;
import org.junit.*;

import static org.junit.Assert.*;

public class ConFunctionTest {

    @Rule
    public final FnTestingRule testing = FnTestingRule.createDefault();

    @Test
    public void shouldReturnGreeting(){
        testing.givenEvent().withBody("{\"str1\":\"Bob\", \"str2\":\"mm\"}").enqueue();
        testing.thenRun(ConFunction.class,"handleRequest");

        FnResult result = testing.getOnlyResult();
        assertEquals("{\"f_str\":\"Concatanated string is Bobmm\",\"length\":5}", result.getBodyAsString());
    }
}