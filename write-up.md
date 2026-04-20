Daily Reflection Tree — Design Write-up

1. Objective

The goal of this project is to build a simple daily reflection tool that helps employees think about their day in a structured way.

Instead of using AI to generate answers, this system follows a fixed decision tree. That means every user gets a consistent experience, and the same answers will always lead to the same result. This makes the system reliable and easy to trust.

2. Why These Questions Were Chosen

The questions are designed to feel like a natural conversation, not a formal survey.

I focused on keeping them:

* Simple and easy to understand
* Based on real work situations
* Clear enough so users don’t get confused between options



For example:

* “How would you describe your day?” helps the user reflect emotionally
* “When something went wrong, how did you respond?” focuses on behavior
* “What did you contribute today?” shifts thinking toward value
* “Where was your focus today?” helps expand awareness

The idea is to slowly move the user from basic reflection to deeper thinking.

3. Branching Design and Trade-offs

 Branching Logic

The system works using simple decision rules:

* Each answer leads to a fixed next step
* There is no randomness and no AI involved

For example:

* Positive answers move the user toward a more proactive path
* Negative answers lead to reflective or corrective paths

Trade-offs

While designing this, I made a few practical choices:

1. Limited Options (3–4 per question)
   This keeps things simple and avoids confusion, even though it reduces some detail.

2. Controlled Depth
   I avoided making the tree too deep so that it stays readable and easy to follow.

3. Pre-written Reflections
   Instead of generating responses, I wrote all reflections beforehand to keep them consistent.

4. Balanced Complexity
   The tree is detailed enough to feel personalized, but still simple enough to manage.


4. Psychological Foundations

The structure of the tree is based on three main ideas from psychology:

Axis 1: Locus of Control

This checks whether the user takes responsibility or blames external factors.

Axis 2: Contribution vs Entitlement

This looks at whether the user focused on giving value or expecting something in return.

Axis 3: Radius of Concern

This expands thinking from self → team → customer.

I also used ideas from:

* Growth mindset (improving through effort)
* Perspective-taking (understanding others)

These concepts helped make the questions more meaningful and realistic.


5. Reflection Design

The reflections are written in a calm and supportive tone.

They are:

* Not judgmental
* Easy to understand
* Slightly motivating

The goal is not to tell the user they are right or wrong, but to help them notice their own patterns.

For example, instead of blaming the user, the system says:
“Situations were difficult, but there were still choices you could make.”



6. Summary Design

At the end, there is one summary that brings everything together.

It:

* Combines insights from all three sections
* Highlights how the user approached their day
* Encourages them to do better tomorrow

The idea is that the user finishes with a clear takeaway, not confusion.


7. What I Would Improve with More Time

If I had more time, I would:

* Add smarter tracking to make summaries more personalized
* Combine multiple answers for deeper insights
* Build a proper UI instead of a simple interface
* Store past sessions to track progress over time
* Add more branches to cover more real-life situations


8. Conclusion

This project shows how simple psychological ideas can be turned into a structured system.

Instead of acting like a chatbot, the tree acts like a guide that helps users think step by step.

The focus was on making the system clear, consistent, and useful, so that users can reflect better on their daily actions and decisions.
