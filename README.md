# ai201-project3-takemeter

```
.
├── .gitignore
├── confusion_matrix.png
├── evaluation_results.json
├── planning.md
├── README.md
└── data/
    ├── Artist Comparison - data.csv      # Labeled dataset
    ├── extract.py                        # Script: Parses JSON threads into tabular CSVs
    ├── extracted_reddit-thread-1c717tj.csv
    ├── extracted_reddit-thread-1svl3ll.csv
    ├── extracted_reddit-thread-gkyd36.csv
    ├── extracted_reddit-thread-ixp2s8.csv
    ├── reddit-thread-1c717tj.json
    ├── reddit-thread-1svl3ll.json
    ├── reddit-thread-gkyd36.json
    └── reddit-thread-ixp2s8.json
```

[Google Collab link](https://colab.research.google.com/drive/1AqvGZLhQfxzh8NMZ9AbzbmI10yDXLuhM?usp=sharing)

## Community

I chose the art-commerce community because I love creating art in my free time and have personally contemplated selling my work, considering financial trade-offs. There is an interesting debate over whether creators should underprice their work to remain accessible to everyday buyers, or if low pricing structurally devalues human labor by ignoring the time, effort, and material overhead required to produce art. The wide range of opinions spans from detailed economic breakdowns to blunt personal opinions, as well as vents from artists and buyers about the experiences they have encountered.

## Label Taxonomy

### `analysis`

**Definition**
An argument or case study based on economic metrics—such as overhead, hourly rates, and market data—to logically evaluate the systemic impact of art pricing, including first-person accounts where a creator uses their own transactional data or calculated labor costs to illustrate a broader business reality.

**Key Indicators**

- Mention of specific numbers, pricing data, or monetary values ($150, £100, 20%).
- Logical breakdowns of product margins, supply/demand mechanics, or volume sales vs. originals.
- Concrete math evaluating time spent, material overhead, or labor value.

**Examples**

- "We have to look at the basic math here. If a piece takes 10 hours to paint, using a $15/hour federal minimum wage standard means the baseline labor cost is $150. When you factor in a 15% self-employment tax and the cost of canvas and physical acrylics, selling that piece for anything less than $200 means the artist is literally operating at a financial loss."
- "The issue with underpricing is how it shifts consumer expectations across the broader digital market. When platforms like Fiverr normalize $10 logos, it skews the perceived value of creative assets, forcing professional freelancers to compete against unsustainable pricing structures that don't align with local cost-of-living metrics."

---

### `hot-take`

**Definition**
An assertion or generalization about how the art industry "should" work, stated confidently as a fact but missing supporting data or evidence, which includes general business advice presented without metrics and short conversational commentary passing judgment on industry behavior.

**Key Indicators**

- Absolute language or moral imperatives like _should_, _always_, _never_, _must_, or _it's unethical_.
- Sweeping generalizations about what "consumers," "the public," or "artists" want or do.
- Business advice (e.g., "sell prints," "tier your pricing") stated as a universal rule without specific financial metrics.

**Examples**

- "If you are a hobbyist selling full digital illustrations for $5, you are single-handedly destroying the freelance art industry. People who do this lack any self-respect and should be banned from posting in public commission spaces altogether."
- "Real art should be accessible to everyday working-class people, not just rich elites. If an artist refuses to lower their prices for someone who genuinely loves their work but is broke, they care way more about greed than the actual spirit of creativity."

---

### `reaction`

**Definition**
A subjective expression of a specific user's personal emotions, anxieties, or lived experiences typically framed in the first person, covering localized conversational expressions such as peer-to-peer encouragement, direct practical advice, or the sharing of specific external links.

**Key Indicators**

- First-person framing focused on immediate emotions, anxieties, personal dreams, or validation.
- Supportive, empathetic peer communication or highly localized advice (e.g., "try a local pet festival").
- Sharing concrete references, tool directories, or links as a helpful peer rather than a structural critique.

**Examples**

- "Ugh, I honestly want to cry right now. I just spent three whole days on a custom commission and the client asked if I could drop the price from $40 to $15 because it's 'just a hobby' for me. It feels so insulting and makes me want to just lock my tablet away and never post my art online again."
- "I feel so awkward right now because I really want to commission this illustrator whose work I adore, but I'm just a student and can't afford their standard rates. I want to ask if they offer simpler, cheaper options like quick sketches, but I’m terrified of offending them or looking like a choosing beggar."

## Data Collection & Labeling

Data was collected in JSON format from four Reddit posts within the r/ArtistLounge community using the web-scraping tool, reddinbox. I then developed a Python script (extract.py) to parse this raw data into structured CSV files. These four CSV files were combined into a single Google Sheet, where I utilized Gemini alongside my label taxonomy to pre-assign initial labels to each post.

Following the automated labeling, I manually reviewed each entry to determine if the assigned label aligned with the established definitions or if it presented an edge case requiring minor adjustments to the taxonomy. Distinguishing between categories proved challenging at times; here are three notable examples of this review process:

Example 1: "I also live in a non-tipping country, jsyk. The thought behind the tip in this case is because you, as the client, felt like you received excellent service and achieved a good output that you want to commend the artist and pay them more to show appreciation.

In this situation, the artist has set a price that they feel is worth their work and so a tip is not included. You might want to consider leaving a tip though if you feel like they didn't charge enough or even if you just appreciate the work a lot.

You don't include tip in the pricing because a tip is a show of appreciation from the client. The client is not obligated to tip at all."

Explanation: Originally labeled by the LLM as a reaction, I re-labeled this entry to a hot-take. The user does not describe a personal experience, but rather offers suggestions and generalized opinions regarding tipping culture.

Example 2:
"I used to be in the medical marijuana business from 2015-2021. When advertising my products, I would sometimes run into broke college kids (I live near a very prestigious & wealthy university), and they could only afford maybe $20. I would take the $20 for something that is normally $25-35. Why? Because money is money. I could either make a $5-10 profit off them or deny their $20 and make no profit. This would also increase my chance of a returning customer.

Now I do the same thing with my art. Broke people want art too."

Explanation: The LLM originally labeled this as a reaction, but I adjusted it to analysis. The user provides a comparative business case backed by specific dollar amounts to demonstrate why lower pricing can optimize marginal profit and could improve customer retention.

Example 3:
"Wow some people don't understand the concept of labour"

Explanation: The LLM classified this statement as a reaction, but I relabeled it as a hot-take. It avoids personal experiences and instead functions as a generalized statement on how knowledgeable other people are.

```
======================================================
Label Class     | Count            | Distribution
======================================================
reaction        | 82               | 0.3849765258
analysis        | 56               | 0.2629107981
hot-take        | 75               | 0.3521126761
------------------------------------------------------
Total           | 213
======================================================
```

## Fine-Tuning

To optimize the distilbert-base-uncased base model, I initially used a 3-epoch setup with a learning rate of 2e-5 and a batch size of 16, but increasing to 5 epochs caused the model to quickly overfit as validation loss increased. To combat this, I dropped the batch size to 4, which increased total weight updates to prevent the model from falling into majority-class guessing—particularly for the underrepresented analysis label. Finally, I increased the learning rate slightly to 3e-5, allowing the network to adjust its attention weights to better map out distinct class boundaries. Overall, I concluded that more labeled posts need to be added to help the model refine these decision boundaries further.

## Baseline

To capture a zero-shot baseline, I used the llama-3.3-70b-versatile model with this system prompt:
"""
You are classifying posts from the art-commerce community focusing on if underpricing work is harmful or beneficial.
Assign each post to exactly one of the following categories.

analysis: An argument or case study based on economic metrics—such as overhead, hourly rates, and market data—to logically evaluate the systemic impact of art pricing, including first-person accounts where a creator uses their own transactional data or calculated labor costs to illustrate a broader business reality.
Example: "The issue with underpricing is how it shifts consumer expectations across the broader digital market. When platforms like Fiverr normalize $10 logos, it skews the perceived value of creative assets, forcing professional freelancers to compete against unsustainable pricing structures that don't align with local cost-of-living metrics."

hot-take: An assertion or generalization about how the art industry "should" work, stated confidently as a fact but missing supporting data or evidence, which includes general business advice presented without metrics and short conversational commentary passing judgment on industry behavior.
Example: "Real art should be accessible to everyday working-class people, not just rich elites. If an artist refuses to lower their prices for someone who genuinely loves their work but is broke, they care way more about greed than the actual spirit of creativity."

reaction: A subjective expression of a specific user's personal emotions, anxieties, or lived experiences typically framed in the first person, covering localized conversational expressions such as peer-to-peer encouragement, direct practical advice, or the sharing of specific external links.
Example: "Ugh, I honestly want to cry right now. I just spent three whole days on a custom commission and the client asked if I could drop the price from $40 to $15 because it's 'just a hobby' for me. It feels so insulting and makes me want to just lock my tablet away and never post my art online again."

Respond with ONLY the label name.
Do not explain your reasoning.

Valid labels:
analysis
hot-take
reaction
"""
The model was able to parse all 32 data points and collected the overall accuracy and per-class metrics of precision, recall, and f1-score.

## Evaluation Report

### Metrics

```
==================================================
RESULTS COMPARISON
==================================================
Model                               Accuracy
---------------------------------------------
Zero-shot baseline (Groq)              0.500
Fine-tuned DistilBERT                  0.625
---------------------------------------------
Fine-tuning improvement: 0.125

Per-class metrics (baseline):
              precision    recall  f1-score   support

    analysis       0.67      0.44      0.53         9
    hot-take       0.50      0.36      0.42        11
    reaction       0.44      0.67      0.53        12

    accuracy                           0.50        32
   macro avg       0.54      0.49      0.50        32
weighted avg       0.53      0.50      0.49        32

Per-class metrics (fine-tuned model):
              precision    recall  f1-score   support

    analysis       1.00      0.11      0.20         9
    hot-take       0.58      1.00      0.73        11
    reaction       0.67      0.67      0.67        12

    accuracy                           0.62        32
   macro avg       0.75      0.59      0.53        32
weighted avg       0.73      0.62      0.56        32

Confusion Matrix:
======================================================
True Label  | Predicted: analysis | hot-take | reaction
======================================================
analysis    | 1                   | 4        | 4
hot-take    | 0                   | 11       | 0
reaction    | 0                   | 4        | 8
======================================================
```

### Sample Classifications

```
======================================================================================================================
ID  | Post Text                                                                        | Predicted | Conf | Actual
======================================================================================================================
#1  | As an artist, I think it’s ok. I am a mid career artist. I am underpriced        | reaction  | 0.72 | reaction
    | because the economy in my city couldn’t bear what I think I’m worth.             |           |      |
    | I appreciate my patrons who have taken a risk on me when I was unknown.          |           |      |
    | If more people bought art at unethical prices from emerging artists,             |           |      |
    | then they could raise their prices faster.                                       |           |      |
----------------------------------------------------------------------------------------------------------------------
#2  | No, everyone sets the price they want, and customers have nothing to do with it. | hot-take  | 0.56 | hot-take
    | The market moves on its own.                                                     |           |      |
----------------------------------------------------------------------------------------------------------------------
#3  | Honestly, I think the answer is to charge even more. Completely scare away       | hot-take  | 0.38 | reaction
    | the people who think they can get art for cheap. That whole audience-            |           |      |
    | people who try to find the lowest cost portrait- is not worth dealing with.      |           |      |
    | Your work is gorgeous and is worth a higher price point. I sell a lot of         |           |      |
    | originals, and I get fewer complaints the higher I go. It is a luxury item       |           |      |
    | and it's ok to price it as such.                                                 |           |      |
----------------------------------------------------------------------------------------------------------------------
#4  | Was it for commercial use? if they are going to use the art for a cd or book     | hot-take  | 0.53 | analysis
    | or ad then it expected that they pay 100+, they will just recover the money      |           |      |
    | they paid you with the sells.                                                    |           |      |
----------------------------------------------------------------------------------------------------------------------
#5  | If you charge what you're worth from the start you'll find less people will      | reaction  | 0.53 | analysis
    | bother trying to take advantage. Stop doing free portraits (unless it's gifts    |           |      |
    | for people you love). Say no. Just no. You are skilled. You will wind up         |           |      |
    | overworking yourself for nothing. I charge $280 for my smallest pastel           |           |      |
    | portraits. And I only bother with clients within my country. I get 50% non       |           |      |
    | refundable before starting with the balance on completion. I don't get any       |           |      |
    | complaints or people trying to scam. I assume because I'm very clear in my       |           |      |
    | terms and don't stand for any shit. People aren't doing me a favour by hiring    |           |      |
    | me. *I'm* doing them a favour by taking their commission. Yeah I still get       |           |      |
    | nft requests and the "draw my daughters dog for $300" scammers but I don't       |           |      |
    | give them any time. Immediately report and block. You have to stand up for       |           |      |
    | yourself and your art or you'll keep getting treated like crap.                  |           |      |
======================================================================================================================
```

### Wrong Classifications

For example #3, the model labeled the post as a hot-take despite it being a reaction. This post starts off with a strong opinion from the user but transitions into their personal experience. While the opening structure of the post signals a hot-take, it should actually be a reaction due to the heavy focus on personal anecdotes in the second half. This aligns with a directional trend highlighted in the confusion matrix, where true reaction posts are only misclassified as hot-takes, while the model was able to classify all true hot-takes correctly. To address this, I should include more examples in the dataset that structurally use phrasing that partially signals one label, but overall are more representative of another.

For example #4, the model labeled the post as a hot-take despite it being an analysis. This post uses more assertive, opinionated language that likely signaled a hot-take to the model, causing it to focus on the tone rather than the underlying economic logic. To address this, I should refine my definition for analysis to focus less on an academic tone, as these real-world examples on Reddit demonstrate that both analysis and hot-take posts often share a similar tone.

For example #5, the model labeled the post as a reaction despite it being an analysis. This post incorporates a heavier use of the first-person perspective and personal experiences from the artist, which the model likely relied on as a signal to classify it as a reaction. However, this shortcut led the model astray, causing it to overlook how those personal examples were actually being used as evidence to explain macro market dynamics. To address this, I should provide more analysis examples in the dataset that incorporate first-person experiences as evidence to explain market points, and I should also refine both my reaction and analysis definitions to make this distinction clearer.

### Correct Classification

For example #1, the model labeled the post correctly as a reaction with a higher confidence of 0.72. The model caught on that this user is taking about their personal experiences being an artist and heavy use of first-person.

For example #2, the model labeled the post correctly as a hot-take. The model evaluated that this user was providing a generalization about the art market and was not basing this on economic data or personal experiences.

## Reflection

<!--what your model captured vs. what you intended it to capture. This is distinct from listing wrong predictions — it's a higher-level observation about the gap between your label definitions and what the model's decision boundary actually captures. What did the model overfit to? What did it miss?-->

The model relied on shortcuts, mapping first-person words to reaction and assertive language straight to hot-take. This caused it to miss the bigger picture, failing to see when personal stories were used as economic evidence or to evaluate the post as a whole. The model overfit to hot-takes—its boundary became aggressive, hitting a perfect 1.00 recall but resulting in false positives due to tone similarities. It completely missed on analysis because it failed to recognize logic whenever it lacked an academic tone. Ultimately, adding more mixed-signal examples is needed to help the model learn more nuanced decision boundaries.

## Spec Reflection

<!-- describe one way the spec helped guide your implementation and one way your implementation diverged from it and why.-->

The label stress testing helped me refine the definitions to make sure more cases were being covered. This also helped me create clearer distinctions between posts when I was going through and reviewing labels to double-check their validity. I revised my plan because I originally mentioned I would hand-label each post. Due to the sheer number of posts to review, I ended up using Gemini to pre-label them; I then hand-reviewed each label and its reasoning, double checking them against my definitions to see if I agreed, and changed the labels or refined my definitions accordingly.

## AI Usage

<!-- Describe at least 2 specific instances: what you directed the AI tool to do, what it produced, and what you changed or overrode. If you used any AI assistance during annotation (e.g., asking an LLM to pre-label examples you then reviewed), disclose it here.-->

**Instance 1**

- What I gave the AI: I gave Gemini my posts data and label definitions specified in planning.md.
- What it produced: A table with each post, label classificaiton, and reasoning.
- What I changed or overrode: I changed labels accordingly if they did not match the definitions and if the reasoning did not justify that particular label. I also used Gemini to help refine my definitions after reviewing the labels and using these re-labeled examples to help capture those nuances better.

**Instance 2**

- What I gave the AI: I gave Gemini my hyperparameters, the confusion matrix, and per-class metrics.
- What it produced: Some suggestions on combinations of hyperparameters to experiment with.
- What I changed or overrode: I re-prompted the AI based on the new metric results until I felt confident that the model was learning and capturing nuances in the data rather than overfitting. I reviewed the validation and testing loss to see how different hyperparameters affected these numbers, and I asked the AI based on my observations if my thinking was reasonable for making those hyperparameter changes.
