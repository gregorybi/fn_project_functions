package com.example.fn;

import java.util.ArrayList;
import java.util.Collections;

public class List_Function {

    public static class Input {
        public ArrayList<Integer> list;
    }

    public static class Result {
        public String f_str;
        public ArrayList<Integer> sorted;
    }

    public Result handleRequest(Input input) {
        Result result = new Result();
        
        if (input.list == null || input.list.isEmpty()) {
             result.f_str = "Enter List for sorting please.";
        }

        else {
            result.f_str = "Sorted List is: ";
            Collections.sort(input.list);
            result.sorted = input.list;
        }
        
        return result;
    }

}