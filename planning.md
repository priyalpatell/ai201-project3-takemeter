## Community

<!--What community did you choose and why? Why is this community a good fit for a classification task — what makes the discourse varied enough to be interesting?-->

I chose the art-commerce community because I love creating art in my free time and have personally contemplated selling my work, considering financial trade-offs. There is an interesting debate over whether creators should underprice their work to remain accessible to everyday buyers, or if low pricing structurally devalues human labor by ignoring the time, effort, and material overhead required to produce art. The wide range of opinions spans from detailed economic breakdowns to blunt personal opinions, as well as vents from artists and buyers about the experiences they have encountered.

## Labels

<!--What are your 2–4 labels? Define each in a complete sentence. Include 2 example posts per label.-->

### `analysis`

An argument based on economic metrics--such as overhead, hourly rates, and market data--to logically evaluate the systemic impact of art pricing.

**Examples**

"We have to look at the basic math here. If a piece takes 10 hours to paint, using a $15/hour federal minimum wage standard means the baseline labor cost is $150. When you factor in a 15% self-employment tax and the cost of canvas and physical acrylics, selling that piece for anything less than $200 means the artist is literally operating at a financial loss."

"The issue with underpricing is how it shifts consumer expectations across the broader digital market. When platforms like Fiverr normalize $10 logos, it skews the perceived value of creative assets, forcing professional freelancers to compete against unsustainable pricing structures that don't align with local cost-of-living metrics."

### `hot-take`

An assertion or generalization about how the art industry "should" work, stated confidently as a fact but missing any supporting data or evidence.

**Examples**

"If you are a hobbyist selling full digital illustrations for $5, you are single-handedly destroying the freelance art industry. People who do this lack any self-respect and should be banned from posting in public commission spaces altogether."

"Real art should be accessible to everyday working-class people, not just rich elites. If an artist refuses to lower their prices for someone who genuinely loves their work but is broke, they care way more about greed than the actual spirit of creativity."

### `reaction`

A subjective expression of a specific user's personal emotions, anxieties, or lived experiences, typically framed in the first person.

**Examples**

"Ugh, I honestly want to cry right now. I just spent three whole days on a custom commission and the client asked if I could drop the price from $40 to $15 because it's 'just a hobby' for me. It feels so insulting and makes me want to just lock my tablet away and never post my art online again."

"I feel so awkward right now because I really want to commission this illustrator whose work I adore, but I'm just a student and can't afford their standard rates. I want to ask if they offer simpler, cheaper options like quick sketches, but I’m terrified of offending them or looking like a choosing beggar."

## Hard edge cases

<!--What type of post will be genuinely ambiguous between two labels? How will you handle it when you encounter it during annotation?-->

Some posts mention numbers or prices, but will look specifically at how those numbers are actually used. If a post includes dollar amounts but doesn't use them to do any real math or prove a point, I know it is not an analysis. Instead, if the numbers are just part of a personal story about buying or selling something, I will classify it as a reaction. If the numbers are just thrown in to vent about a hypothetical situation or a broad rumor, I will label it a hot-take.

Some posts won't include any numbers at all, which could result in them being incorrectly classified as a hot-take or reaction. However, if the user backs up their point with real-world examples, like history, industry trends, or a clear cause-and-effect argument, then this would be an analysis.

It can be confusing when a user tells a personal story but adds in small generalizations about the art world. When a post blurs the line like this, I look at the main focus of the text. If the core of the post is about the artist’s or buyer’s own real-life experience and feelings, I will keep it classified as a reaction instead of a hot-take.

## Data collection plan

<!--Where will you collect examples? How many per label? What will you do if a label is underrepresented after 200 examples?-->

To gather my data, I will collect examples from various Reddit posts within the r/ArtistLounge community, aiming for an equal split among my three labels. If I notice that a specific label is underrepresented, I will either search for more posts that fit that category or reduce the number of examples in the other categories to keep the dataset balanced. In total, I my sample size will be around 200+ posts.

Sources:
https://www.reddit.com/r/ArtistLounge/comments/1svl3ll/is_it_unethical_to_buy_from_underpricing_artists/
https://www.reddit.com/r/ArtistLounge/comments/gkyd36/feeling_too_guilty_to_price_up_my_art/
https://www.reddit.com/r/ArtistLounge/comments/ixp2s8/people_always_tell_the_artist_to_price_their_work/
https://www.reddit.com/r/ArtistLounge/comments/1c717tj/im_undercharging_my_work/

All can be found in the /data folder in two format JSON (web-scraped data) and csv (parsed data).

## Evaluation metrics

<!--Which metrics will you use to evaluate your model and why are those the right ones for this specific task? (Accuracy alone is not enough — explain what else you need and why.)-->

To evaluate my model, I will use a combination of overall accuracy, per-class metrics, and a confusion matrix. The overall accuracy will show the total fraction of correct guesses, allowing me to compare my model's performance against the baseline. For the per-class metrics, I will evaluate the precision, recall, and F1 score for each category to understand exactly where the model is succeeding or struggling. Checking for high precision will tell me if the model is carefully applying a label only when it is highly confident, while tracking recall will show if it is successfully catching as many true examples as possible. The F1 score will then serve as a balanced measure to show how well the model is learning these specific class distinctions overall. Finally, I will use the confusion matrix to see exactly which labels are getting mixed up, helping me identify clear patterns and fix any labeling inconsistencies in my data.

## Definition of success

<!--What performance would make this classifier genuinely useful? What would you accept as "good enough" for deployment in a real community tool?-->

There are a few main metrics I’d look at to see if this classifier is actually good enough to deploy as a real community tool. First, I’d want every single class to have an F1-score of at least 0.70, which proves the model is actually learning the differences between the labels well. I’d also look for high precision so users can trust the data claims, and high recall so important posts don't get missed. Finally, I’d check the confusion matrix to make sure the labels aren't getting swapped around and the model isn't just picking one default label whenever it gets confused.

## AI Tool Plan

### Label stress-testing

**Edge Case 1: Looks like Analysis but is a Hot-Take**

Example: "Basic supply and demand dictates that if you charge pennies for your work, you are actively shifting the economic baseline for every single digital creator on the platform."

Explanation: It uses specific terminology like "supply and demand" and "economic baseline", but doesn't have specific metrics to back these claims.

**Edge Case 2: Uses first person but is a Hot-Take**

Example: "I think that any artist who charges less than $50 an hour is completely ruining the market for the rest of us."

Explanation: The core idea isn't about the person's own experience and is focused on an opinion they have about the market.

**Edge Case 3: A historical comparison without metrics is an Analysis**

Example: "The current digital art pricing crisis mirrors the early days of stock photography platforms, where an influx of cheap, crowdsourced assets permanently destroyed the income stability of independent studio photographers by altering what corporate clients expected to pay for usage rights."

Explanation: The person presents a logical argument with a historical parallel to show a cause and effect relationship.

**Edge Case 4: Uses metrics but is a Hot-Take**

Example: "Why is this $100 and not $30?! That's literal highway robbery, artists are so greedy nowadays!"

Explanation: Makes a claim about artists being greedy and does not directly rely on economic affordability metrics to support claim.

**Edge Case 5: Personal story that include strong generalizations is a reaction**

Example: "I used to underprice my work because I wanted to be nice, but after a client completely took advantage of me and demanded a million free changes, I realized it's just not worth it. I felt so burnt out and unappreciated that I decided I'm never catering to cheap budgets again, because it only leads to absolute misery for the artist."

Explanation: At the end the person generalizes, but the overall premise and how the post starts is talking about their experience.

### Annotation assistance

I will use Gemini and give it the label definitions stated above and ask it to match a label and provide an explanation. This way I can see why the model made a certain lable choice and if this reasoning is inconsistent with definitions.

### Failure analysis

To check for labeling mistakes, I will review my labeled data a second time to look for inconsistencies. If I find posts where I hesitated or don't agree with the explanation, I will re-evaluate using my definitions to select the appropriate label. I will then verify the AI's suggestions and adjust my definitions accordingly.
