using Function;
using NUnit.Framework;

namespace Function.Tests {
  public class GreeterTest {
    [Test]
    public void TestGreetEmpty() {
      Greeter greeter = new Greeter();
      Input input = new Input();
      Output output = greeter.greet(input);
      Assert.AreEqual("Hello World!", output.message);
    }

    [Test]
    public void TestGreetValid() {
      Greeter greeter = new Greeter();
      Input input = new Input();
      input.name = "Dotnet";
      Output output = greeter.greet(input);
      Assert.AreEqual("Hello Dotnet!", output.message);
    }
  }
}
