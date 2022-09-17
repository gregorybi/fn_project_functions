package com.example.fn;

public class HelloFunction {

    public static class Input {
        public String name;
    }

    public static class Result {
        public String salutation;
    }

    public Result handleRequest(Input input) {
        Result result = new Result();
        
        if (input.name == null || input.name.isEmpty()) 
            result.salutation = "Hello World!";
        else {
            final String prep = "Hello " + input.name;
            result.salutation = prep + " !" ;
        }
        
        return result;
    }

}