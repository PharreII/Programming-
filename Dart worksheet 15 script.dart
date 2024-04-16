import 'dart:io';
import 'dart:math';

void main() {
  sayName();
  studentDetails();
  print('20 euros in pounds: ${eurosToPounds(20)}');
  print('68°F in Celsius: ${fahrenheitToCelsius(68)}');

  // Call to functions asking for user input and displaying area and circumference.
  double radius = getRadius();
  circleInfo(radius);

  displayBurgerOrder(3, 5.89);
}

void sayName() {
  print('My name is Pharrell Owens');
}

void studentDetails() {
  print('My name is Pharrell Owens');
  print('My student number is 2124515');
  print('My email address is: up2124515@myport.ac.uk');
}

double eurosToPounds(double euros) {
  return euros * 0.86;
}

double fahrenheitToCelsius(double fahrenheit) {
  return (fahrenheit - 32) * 5 / 9;
}

double getRadius() {
  print('Enter the radius of the circle:');
  return double.parse(stdin.readLineSync()!);
}

double areaOfCircle2(double radius) {
  return pi * pow(radius, 2);
}

double circumferenceOfCircle2(double radius) {
  return 2 * pi * radius;
}

void circleInfo(double radius) {
  print('For a circle with radius $radius:');
  print('Area: ${areaOfCircle2(radius).toStringAsFixed(2)}');
  print('Circumference: ${circumferenceOfCircle2(radius).toStringAsFixed(2)}');
}

void displayBurgerOrder(int count, double price) {
  String burgerEmoji = "\u{1F354}";  // Unicode for burger emoji
  double total = count * price;
  print('Your order: ${burgerEmoji.repeat(count)}');
  print('Total: £${total.toStringAsFixed(2)}');
}
