# <a name="top">Advent of Code 2023!</a>

[Day 1](#Day1)  
[Day 2](#Day2)  
[Day 3](#Day3)  
[Day 4](#Day4)  
[Day 5](#Day5)  
[Day 6](#Day6)  

Things that are different for me for Year 3 (will add as I go):

- I'm not ashamed that I'm not going to come up with the most optimized solutions. I'm going to come up with the simplest solution that I am able to do that gets it done. I have the rest of my career to get better at best practices and believe me, I want to. However after a year+ on the job I have learned there is a high premium on quick, thorough solutions. I don't have to solve for every future conceivable edge case, but if I happen to stumble on that, cool. I have to solve for the edge cases that exist in front of me. My philosophy now is keep it simple and learn as I go.
- Last year I was new to Python. The year before that I was new to JavaScript. This year I'm not new to the language. I'm using it to get better at a need-to-know for what I do, but I don't get to practice daily. 
- Judging by the first two days, I'm somehow not making as many frustrating little mistakes as I've made in past years. I had to google the syntax for some Python methods but I haven't had to rewrite multiple times because I was erroring out so much. It's been pretty smooth going from the pseudo-code in my head to the implementation. I remember being very frustrated the last two years by my mistakes that I felt like I should not have made. This year I'm surprised by the mistakes I'm *not* making. Professional experience + LeetCode. I don't care what people say, LeetCode does in fact make you a better programmer and I will die on that hill. Just like students who are new to reading need to read a lot to get better at it, the act of interacting with code makes you a better programmer. 
- I did not wait this year to buy merch. Last year I had some kind of mentality that I had to "earn" it (holdover from my running days?? You don't wear the shirt till you've run the race or something?). This year, nope, I hit that [Advent of Code shop link](https://advent-of-code.creator-spring.com/?) so fast. I truly need another hoodie anyway, my only go-to hoodie is from [Saint Frank Coffee (and it's beautiful)](https://www.saintfrankcoffee.com/collections/merchandise/products/sister-moon-hoodie). Swag is the best. And I told myself having a ridiculous part 2 on Day 1 justified it. :D 
- I am seriously contemplating creating a Reddit account just to interact with the [AoC after-party](https://www.reddit.com/r/adventofcode/). It's my tradition to solve first and then go laugh at memes. I have never in my life before contemplated creating a reddit account. But the memes are so much fun. And I've looped my whole family into this now. My kids will gather around the computer as I explain the puzzle and then we laugh--sometimes until we cry--over the visualizations and memes on reddit. The AoC community is one of the best. 
- I'm not going to stress myself out over this. It will be great to get farther than the last 2 years, but I have a lot of responsibilities on me at the moment. This is what I am doing for fun and self-care (as odd as that may sound). So I'm letting go of pressure and expectations for this year and just enjoying it. Whether I make it 2 days or 20, I'm grateful for the experience and the joy it brings.

[Back to top](#top)

## <a name="Day1">Day 1</a>

I just have to start this one off with: After I solved I got my family around and we read the story. My husband and kids were cackling. I have missed the absolute silliness of AoC. 

Part 1 was super straightforward. Get the digit with the lowest index, the digit with the highest index, concatenate, cast as int, add. 

Part 2? Lol. I mean it really wasn't that bad but for day 1?? Yeah. 

So I was one of the people that just stumbled into a good solution out of sheer luck. [I have not posted in this thread](https://www.reddit.com/r/adventofcode/comments/188bu8v/2023_day_01_part_2_how_many_people_were/), but yeah, this was me. My first thought was to just iterate through each index, and since we are only talking about 9 digits with only three possible substring lengths, it seemed like a no-brainer to just hard code values and check for substring matches. I loaded any match into a dictionary and converted it on load to a digit if needed, checked for the lowest and highest indeces, then concatened and added. Hacky? Sure. Did it work? Beautifully. One benefit was I did not alter the original strings. Any conversion was done when adding to the dictionary. This puzzle definitely makes a case for not changing the original state. :) 

My major stumbling block is I still think with JavaScript brain (don't train on JS if you can help it) and have to account for the stronger typing in Python. I'll get there eventually. Once I got out of my own way it worked like a charm and I managed it before my work hours started. 

Overall not a bad way to start day one. [But the memes?](https://www.reddit.com/r/adventofcode/comments/1885c33/2023_day_01_did_not_expect_this_on_day_1/) Worth it. 

[Back to top](#top)

## <a name="Day2">Day 2</a>

Y'all I woke up at 5:30 on a Saturday morning with no alarm because I was so excited for this. I thought about staying up to solve last night but we have a full weekend of activities ahead of us and I really don't want to be grumpy. Also there's something fun about gulping down coffee while solving code so there's that too. 

Like many AoC activities, a lot of this is about parsing the input. Ironically practice with that has actually helped me on the job (data engineering things). 

The big trick for today's solve that made both parts easier was not getting too caught up in which set is what within the game id as a whole. For part one, any one individual color pull that is greater than the supply knocks the whole game id out of the running. So I just started with a true flag and any impossible color in that line sets it to false. If the flag is still true at the end, then it gets added to the total.

Part two was surprisingly smooth today. All I had to do was modify the existing code to check for any color count that was greater than what was in the current set and then replace if so. I multiplied the piece counts at the end and then added it to the sum. Done. :) 

Now I just have to decide if I'm staying up late tonight to solve Day 3 or waking up stupid early again tomorrow. :D :D 

Edited to Add: [Accurate](https://www.reddit.com/r/adventofcode/comments/1893ua2/2023_day_2_parsing_was_a_chore_but_man/)

[Back to top](#top)

## <a name="Day3">Day 3</a>

Seeing how easy Day 2 was (a return to "normal," I was hoping), I rested well last night and woke up about 6, got my coffee and sat down to start working...

[Only to get slammed with a 2D matrix with diagonals](https://www.reddit.com/r/adventofcode/comments/189p6qt/2023_day_3_part_2_what_really_grinds_my_gears/). 

OK, no big deal, I had a pretty decent idea of how to get the data I needed. It's just matrices are tedious. 

The first issue I ran into is I am still used to JavaScript scoping and have not yet gotten a good understanding of Python scoping within functions. I learned about global scope, but still had an issue bringing in one variable that kept getting converted to local scope. I decided instead to just convert that to a list which helped with debugging later. But, I made progress on understanding how global and local scope are handled in Python, so that counts as a win for today.

The second problem I encountered was a bug in my parsing. I used the character after a number to determine if I was finished building that number, but that doesn't work for end of line numbers. I got lucky in that I was testing to see if '\n' was considered a symbol and when I included that my answer was too high. So I had a definite range to work with and got a pretty good idea that somehow I wasn't including end of line numbers. I went back over my code and found if I just add a condition that checks for if it is the end of the line then I got the correct answer.

Because I had part 1 set up well, part 2 didn't take long and I got it right on the first try. I set up a dictionary to store star coordinates as a flattened string. Any number adjacent to that particular star coordinate got added to the value list for that star. At the end I gathered the star coordinates with 2 numbers, multiplied and totaled.

Here's to hoping Day 4 is more like Day 2 in difficulty, I'd like to get at least a week accomplished this year... :)

[Back to top](#top)

## <a name="Day4">Day 4</a>

I knocked out part 1 pretty easily before work, and then for part 2 I needed a little more time to think than my morning commute would allow. So I left that for after work & family activities. 

My first thought was an enqueue/dequeue system, which, when I ran it, caused my VS Code editor to shut down. I knew some minutes before that happened that I needed to optimize it. An hour later, my very tired brain figured out the math pattern needed for a one-pass go. It should have been simple but my brain was not thinking in that direction today. 

A win is a win, though, and I will take this one!!

[Back to top](#top)

## <a name="Day5">Day 5</a>

I got off to a slower start for this one for a couple of reasons. I had to hard code the sample input to start in order to understand the pattern. After I did that I was able to change it to dynamic inputs, although I know I can even optimize that further if I wanted.

Part 2 the code change wasn't much, it was the brute forcing that created an issue. As far as I'm concerned though, I put in hours every day coding and sometimes on one problem. So can my computer. We'll call it an equal partnership. 

I will go back and watch an AoC YouTuber explain how to optimize this, but for day 5, I have two more stars. ⭐ ⭐

[Back to top](#top)

## <a name="Day6">Day 6</a>

This is my fastest solve for AoC 2023 yet... Pretty straightforward, just a lot of parsing and a little math. ⭐ ⭐

[Back to top](#top)

## <a name="Day7">Day 7</a>

Python deepcopy and sort are the real MVP today. ⭐ ⭐

[Back to top](#top)