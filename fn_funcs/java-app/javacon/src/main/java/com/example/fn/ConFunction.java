package com.example.fn;

public class ConFunction {

    public static class Input {
        public String str1;
        public String str2;
    }

    public static class Result {
        public String f_str;
        public int length;
        
    }

    public Result handleRequest(Input input) {
        Result result = new Result();
        
        if (input.str1 == null || input.str1.isEmpty()) {
             result.f_str = "Enter String1 please.";
            
        }
        
        else if (input.str2 == null || input.str2.isEmpty()) {
            result.f_str = "Enter String2 please.";
            
        }

        else {
            final String fstr1 = input.str1;
            final String output_str = fstr1 + input.str2;

            final String prep = "Concatanated string is " + output_str;
            result.f_str = prep ;
            result.length = output_str.length();
            
        }
        
        return result;
    }

}