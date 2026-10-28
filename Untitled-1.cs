string projectName = "ACME";
string englishLocation = $@"c:\Exercise\{projectName}\data.txt";
Console.WriteLine($"View English output:\n\t{englishLocation}\n");

string russianMessage = "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u0432\u044b\u0432\u043e\u0434";
string russianLocation = $@"c:\Exercise\{projectName}\ru-RU\data.txt";
Console.WriteLine($"{russianMessage}:\n\t{russianLocation}\n");

// Collect the bill amount and tip percentage
 Console.WriteLine("Enter your bill details:\n");
 Console.Write("Bill amount:    ");
 decimal billAmount = Convert.ToDecimal(Console.ReadLine());
 Console.Write("Tip percentage: ");
 decimal tipPercentage = Convert.ToDecimal(Console.ReadLine());

 // Display the entered values
 Console.WriteLine("\nBill details:");
 Console.WriteLine($"  Bill amount:    ${billAmount}");
 Console.WriteLine($"  Tip percentage: {tipPercentage}%");

 // Calculate the tip and total
 decimal tipAmount = billAmount * (tipPercentage / 100);
 decimal totalAmount = billAmount + tipAmount;

 // Display the results
 Console.WriteLine($"\nTip amount:   ${tipAmount}");
 Console.WriteLine($"Total amount: ${totalAmount}");