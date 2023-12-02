# <a name="top">Advent of Code 2023!</a>

[Day 1](#Day1)  
[Day 2](#Day2)


Things that are different for me for Year 3 (will add as I go):

- I'm not ashamed that I'm not going to come up with the most optimized solutions. I'm going to come up with the simplest solution that I am able to do that gets it done. I have the rest of my career to get better at best practices and believe me, I want to. However after a year+ on the job I have learned there is a high premium on quick, thorough solutions. I don't have to solve for every future conceivable edge case, but if I happen to stumble on that, cool. I have to solve for the edge cases that exist in front of me. My philosophy now is keep it simple and learn as I go.
- Last year I was new to Python. The year before that I was new to JavaScript. This year I'm not new to the language. I'm using it to get better at a need-to-know for what I do, but I don't get to practice daily. 
- Judging by the first two days, I'm somehow not making as many frustrating little mistakes as I've made in past years. I had to google the syntax for some Python methods but I haven't had to rewrite multiple times because I was erroring out so much. It's been pretty smooth going from the pseudo-code in my head to the implementation. I remember being very frustrated the last two years by my mistakes that I felt like I should not have made. This year I'm surprised by the mistakes I'm *not* making. Professional experience + LeetCode. I don't care what people say, LeetCode does in fact make you a better programmer and I will die on that hill. Just like students who are new to reading need to read a lot to get better at it, the act of interacting with code makes you a better programmer. 
- I did not wait this year to buy merch. Last year I had some kind of mentality that I had to "earn" it (holdover from my running days?? You don't wear the shirt till you've run the race or something?). This year, nope, I hit that [Advent of Code shop link](https://advent-of-code.creator-spring.com/?) so fast. I truly need another hoodie anyway, my only go-to hoodie is from [Saint Frank Coffee (and it's beautiful)](https://www.saintfrankcoffee.com/collections/merchandise/products/sister-moon-hoodie). Swag is the best. And I told myself having a ridiculous part 2 on Day 1 justified it. :D 
- I am seriously contemplating creating a Reddit account just to interact with the [AoC after-party](https://www.reddit.com/r/adventofcode/). It's my tradition to solve first and then go laugh at memes. I have never in my life before contemplated creating a reddit account. But the memes are so much fun. And I've looped my whole family into this now. My kids will gather around the computer as I explain the puzzle and then we laugh--sometimes until we cry--over the visualizations and memes on reddit. The AoC community is one of the best. 
- I'm not going to stress myself out over this. It will be great to get farther than the last 2 years, but I have a lot of responsibilities on me at the moment. This is what I am doing for fun and self-care (as odd as that may sound). So I'm letting go of pressure and expectations for this year and just enjoying it. Whether I make it 2 days or 20, I'm grateful for the experience and the joy it brings.


## <a name="Day1">Day 1</a>

I just have to start this one off with: After I solved I got my family around and we read the story. My husband and kids were cackling. I have missed the absolute silliness of AoC. 

Part 1 was super straightforward. Get the digit with the lowest index, the digit with the highest index, concatenate, cast as int, add. 

Part 2? Lol. I mean it really wasn't that bad but for day 1?? Yeah. 

So I was one of the people that just stumbled into a good solution out of sheer luck. [I have not posted in this thread](https://www.reddit.com/r/adventofcode/comments/188bu8v/2023_day_01_part_2_how_many_people_were/), but yeah, this was me. My first thought was to just iterate through each index, and since we are only talking about 9 digits with only three possible substring lengths, it seemed like a no-brainer to just hard code values and check for substring matches. I loaded any match into a dictionary and converted it on load to a digit if needed, checked for the lowest and highest indeces, then concatened and added. Hacky? Sure. Did it work? Beautifully. One benefit was I did not alter the original strings. Any conversion was done when adding to the dictionary. This puzzle definitely makes a case for not changing the original state. :) 

My major stumbling block is I still think with JavaScript brain (don't train on JS if you can help it) and have to account for the stronger typing in Python. I'll get there eventually. Once I got out of my own way it worked like a charm and I managed it before my work hours started. 

Overall not a bad way to start day one. [But the memes?](https://www.reddit.com/r/adventofcode/comments/1885c33/2023_day_01_did_not_expect_this_on_day_1/) Worth it. 

## <a name="Day2">Day 2</a>

Y'all I woke up at 5:30 on a Saturday morning with no alarm because I was so excited for this. I thought about staying up to solve last night but we have a full weekend of activities ahead of us and I really don't want to be grumpy. Also there's something fun about gulping down coffee while solving code so there's that too. 

Like many AoC activities, a lot of this is about parsing the input. Ironically practice with that has actually helped me on the job (data engineering things). 

The big trick for today's solve that made both parts easier was not getting too caught up in which set is what within the game id as a whole. For part one, any one individual color pull that is greater than the supply knocks the whole game id out of the running. So I just started with a true flag and any impossible color in that line sets it to false. If the flag is still true at the end, then it gets added to the total.

Part two was surprisingly smooth today. All I had to do was modify the existing code to check for any color count that was greater than what was in the current set and then replace if so. I multiplied the piece counts at the end and then added it to the sum. Done. :) 

Now I just have to decide if I'm staying up late tonight to solve Day 3 or waking up stupid early again tomorrow. :D :D 

Edited to Add: [Accurate](https://www.reddit.com/r/adventofcode/comments/1893ua2/2023_day_2_parsing_was_a_chore_but_man/)

