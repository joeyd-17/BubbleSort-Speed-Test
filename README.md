# Speed Test

Joey Donohue, Ollie Cloutier
Same installations as Speed-Test: Starter Code made by Lisa Dion
Using Python, C++, Java, Ocaml, C, Rust
I completed the Python, C++, and Java Sections

--Summary--
  For our open ended project we were curious about how other languages would test in Speed-Test,
so we expanded the number of languages. We added 4 other languages (Java, C, Rust, Ocaml), to 
be tested. Each program has it's own BubbleSort code and is tested in increments of 1000 from
1000 to 10000. After each time is found, they are compared against each other on a graph. 

--How Languages are connected--
  Python is used as the driver for this project, first testing it's own BubbleSort program and then
running the other program's versions of BubbleSort. The times are compiled in Python and then graphed
in Python using matplot. 

--Why we chose our languages to work in--
  Python was a good choice for running this program as it has a good graphing 
capabilities with matplotlib. The other programs offer different pros and cons and we were looking for 
how these differences in languages would impact their respective bubble sorting speeds.

--Bugs--
The bars in the bar graph are overlapping a bit, and the graph labels don't make for a very presentable graphs

--Future Expansion--
  There are many ways we could expand the project given more time. We could opt to find even more languages,
which would increase our knowledge in sorting algorithms in different languages and in how different langauges
interact with CLI. It would lead to more understanding of what languages sort most efficiently.

  We could also create more graphs for different sorting algorithms. This would be interesting, as it would 
reveal similar patterns to the CS2240 project, but we could see how each languages efficiency changes with different
sorting algorithms. It would be intriguing to analyze how the differences in efficiency change between different algorithms

  We briefly discussed changing the graph type to be a line graph, which would be more effective in conveying lots of langauges
  simultaneously. Making a more presentable graph (with better labels) would be a focus, regardless of the type of project expansion

--Sources--
Lisa Dion- SpeedTest Module 3 Guided Project starter code


