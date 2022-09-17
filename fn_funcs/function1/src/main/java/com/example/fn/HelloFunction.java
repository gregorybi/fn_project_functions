package com.example.fn;

public class HelloFunction {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_YELLOW = "\u001B[33m";

    public String handleRequest(String input) {
        String name = (input == null || input.isEmpty() || input == "{}") ? "world"  : input;

        System.out.println("Inside Java Hello World function"); 
        return ANSI_YELLOW + "Hello, " + name + "!" + ANSI_RESET;
    }

}