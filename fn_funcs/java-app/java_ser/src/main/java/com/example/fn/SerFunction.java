package com.example.fn;

public class SerFunction {

    public static class Input {
        public int a1;
        public int n;
        public int d;
    }

    public static class Result {
        public int n;
        public String message;
        public int a_n;
        public int sum_of_n_terms;
    }

    public Result handleRequest(Input input) {
        Result result = new Result();

        if (input.a1 == 0) 
            result.message = "Enter a1 please.";
       
       else if (input.n == 0) 
           result.message = "Enter n please.";
        
        else if (input.d == 0)
            result.message = "Enter d please.";
        
        else {
            result.n = input.n;
            result.message = "Nth term and Sum of n terms are:";
            result.a_n = input.a1 + (input.n - 1) * input.d;
            result.sum_of_n_terms = (input.n * ((2 * input.a1) + ((input.n - 1) * input.d))) / 2;
        }
        
        return result;
    }



}