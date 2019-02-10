Title: A FiveThirtyEight Riddler Attempt
Date: 2016-12-15
Category: Economics
Tags: background, economics, game theory
Slug: a-fivethirtyeight-riddler-attempt
Summary: An introduction to Game Theory by way of FiveThirtyEight and The Riddler...

While reading a [FiveThirtyEight riddler post,](http://fivethirtyeight.com/features/how-much-gold-would-push-you-into-a-war/) I saw that the classic riddle had to do with game theory. As I've recently been reading about game theory, I thought it would be interesting to work through the problem and see what I come up with.

The rules of the game are as follows: there are two countries with a military strength that is a random uniform number[^1] between 0 and 1. Each country only knows their strength, and these two countries can choose to either declare war or peace. If either country chooses war, the two countries enter into war with the higher strength country obtaining the wealth of the two countries. If both countries choose peace, then they remain with their wealth. Each country starts with a wealth of 1 trillion dollars. The question now is to solve the game. What is the best move for each country?

## Getting Nashty

The first instance of the game is where the moves are made simultaneously[^2]. In order to find the "answer" to the game, I often pick a strategy and play out the game with that strategy to see what happens[^3]. So assume that Country A chooses to declare war whenever it's strength is above .5 [^4]. Because each country is playing the same game, this means that they both follow this rule initially. However, it makes sense for Country B to lower the threshold to .25 (half of the original value). Now you're probably wondering how this makes sense. If A's strength is above .5, it will always declare war and Country B has to fight no matter what. On the other hand, say A's strength is below the .5 threshold. With Country B lowering the threshold necessary to declare war, it will win half of the time and lose half of the time, making a net gain[^5]. 

But! Say Country A also employs an economist well versed in game theory and this economist predicts what Country B will do. Country A will then lower their threshold to .125 (half of .25) for the exact same reason! This arms race will continue until the threshold for each country is at zero, and each country declares war. Thus, the best move[^6] is to have each country always declare war. 

If the game shifts to a version where Country A acts first, and then Country B acts, not a lot changes. If Country A declares peace, Country B knows that is a sign of weakness and will therefore declare war[^7]. If the payout of winning the war is increased, all it means is that war will be more valuable and thus will be declared more often as well. Thus, war will always be declared no matter what. 


[^1]:	In human speak, there's a equally random chance it'll be any decimal. If the decimals make it tough to understand, just make it any number between 0 and 10.

[^2]:	Meaning that if I'm Country A, I don't know Country B's move

[^3]:	My optimal strategy for solving game theory, if you will.

[^4]:	The expected utility of declaring war says that it makes sense to declare war whenever the strength of a country is above .5. In other words, the country will declare war when it expects to earn more money from war than from peace. With a strength of .5, the country will be indifferent between war and peace. It earns 1 trillion if peace holds, and it expects to win the war 50% of the time. .5 multiplied by 2 trillion plus .5 multiplied by zero is 1 trillion. 

[^5]:	Remember, we call indifference a win. Makes the math easier.

[^6]:	The Nash Equilibrium! 

[^7]:	If Country A declares war, it doesn't matter what Country B does regardless.