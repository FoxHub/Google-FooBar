# [Google Foobar Challenge](https://github.com/FoxHub/Google-Foobar)

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](http://opensource.org/licenses/MIT)

(c) 2017 Sage Callon.

In this repository I'll post my solutions to Google Foobar from level 2
and onwards. I found out after completing level 1 that there's no way
to access my code for that submission, so that won't be on this repository.

## What's Google Foobar?

Google Foobar is a timed coding challenge you can receive from Google
if you're caught looking up programming terms using their search engine! I
got my invitation while looking up documentation for the Python standard
library, and used it as an opportunity to sharpen my Python skills.

You get given a time limit for each challenge, ranging from a day to
a few weeks, and your code is run against hidden test cases — including
how fast and memory-efficient it is!

I completed this challenge, and have no work left to do on it unless
Google sends me more.

## Disclaimer

The code on this repository is for educational purposes. If __you__ are
taking the Google Foobar Challenge and on this repository, I encourage
you take my test cases and look into the algorithms I list in each
subsection below.

_You are doing yourself a great disservice if you just copy/paste my
solutions, and I have intentionally left a few files that do not work
on this repository._

## The Challenges



__Level 1__

This level had a problem about counting duplicate occurrences of
characters in a string.

__Level 2__

In this level, I was confronted with the __Knight's Shortest Path__
Algorithm, and __Array Multiplication__ with a lot of conditional cases to
account for.

* Don't Get Volunteered
* Power Hungry

__Level 3__

On this level, the challenges began to become more complicated. I encountered
__Breadth-First Search__ with conditional passthrough, __Euler's Distinct
Partitions__, and a __Lucky Triplets__ problem.

* Prepare the Bunnies' Escape
    * My first attempt at this problem tried to re-use code from level 2
      where I performed a depth-first search, but that was too slow.
    * For my second attempt, I employed breadth-first search and sacrificed
      some memory for performance.
* The Grandest Staircase Of Them All
* Find the Access Codes
    * My first algorithm for tackling this problem was O(n<sup>3</sup>).
    * The second one was much better optimized, running in O(n<sup>2</sup>).

__Level 4__

On this level, I dealt with a __Combinations__ problem, and an instance of
the __Traveling Salesman Problem__.

* Free the Bunny Prisoners
* Running With Bunnies

__Level 5__

This level was the hardest by far, and took me to the whiteboard. I dealt
with __Cellular Automata Pre-imaging__, and had to go read some academic
papers to solve this one.

* Expanding Nebula
    * For my first attempt, I used an algorithm that produced every possible
      pre-image. This was horribly slow, and so I had to try again.
    * My second attempt was the fastest algorithm, but failed because
      the memory consumption when using a cache was too high.
    * My third attempt, and final submission, just avoided as many
      unnecessary computations as possible.

__Secret Follow-up Challenge__

While not a formal level of the coding challenge, I encountered a fun
__Cryptography__ challenge at the end. If you get this far... you should know
what to do!

* For Your Eyes Only

__My Whiteboard__

Can you guess what challenge this was?

![Whiteboard](https://user-images.githubusercontent.com/5873865/29346666-b3b8fb68-81fb-11e7-87de-269c5fae0e4d.jpg)