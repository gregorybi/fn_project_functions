using Fnproject.Fn.Fdk;
using System;

using System.Runtime.CompilerServices;
[assembly:InternalsVisibleTo("Function.Tests")] namespace Function {
  class Input {
    public string name {
      get;
      set;
    }
  }

  class Output {
    public string message {
      get;
      set;
    }

    public Output(string message) { this.message = message; }
  }

  class Greeter {
    public Output greet(Input input) {
      return new Output(string.Format(
          "Hello {0}!",
          string.IsNullOrEmpty(input.name) ? "World" : input.name.Trim()));
    }

    static void Main(string[] args) { Fdk.Handle(args[0]); }
  }
}