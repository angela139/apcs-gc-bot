Starfield (with an Oddball)
=========================
For this assignment you will make a animation of fireworks. This common animation is called a "starfield" since it can also be used to simulate movement through a field of stars. You may find slides 35 - 52 on <a href="https://docs.google.com/presentation/d/1Eldw10Y6tP7Ru6pjaCcZPhm5vxjnKjVrWLB8qT5IiF0/edit?usp=sharing">OOP--Inheritance & Encapsulation</a> presentation helpful.
 
Program requirements:
---------------------
Your program must use at least two classes to model the particles. A `Particle` super class and an `Oddball` sub class. All the particles must be stored in a single array of the super class type. Make sure you do not unnunnecessarily duplicate inherited variables and functions in the `Oddball` sub class. Your `Oddball` sub class need only contain a constructor and `void move()` and/or `void show()` so that the `Oddball` moves and/or looks different.


Suggested steps to completing this assignment
-----------------------------------
1. Fork [this repository](https://github.com/APCSLowell/Starfield)  
2. First, finish the `Particle` class. It will need the following members:
  * 5 member variables: X and Y positions, Color, Angle and Speed. (Hint: use doubles for X, Y, Speed and Angle)
  * `Particle()`, the class constructor
  * `void move()`, Takes the cos of the angle times the speed and adds it to the X coordinate. Does the same to Y with the sin of the angle.
  * `void show()`, draws the particle in the correct color
3. Now finish the program's `setup()` and `draw()`
4. Add one `Particle` variable, and make sure you can see it move
5. Add an array of type `Particle` and loop through it to move and show all the Particles.
9. Create an OddballParticle class that `extends` the Particle class.
12. Change the first element in the array to a `OddballParticle` instead of a `Particle`
13. Run your program. Make sure you can see the Oddball.
15. Submit the url of your working GitHub webpage to google classroom
Extensions: Have a fun and be creative. If you have extra time you may want to modify your program and add extra features and other types and arrangements of particles. Look at student work from the links below for other variations.

Samples of Student Work
-----------------------


[Buddy](https://angela139.github.io/Starfield/)   
[Code](https://angela139.github.io/AsteroidsGame/)   