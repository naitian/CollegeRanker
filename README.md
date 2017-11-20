# College Ranker

One of the difficulties of choosing which colleges to apply to is its subjective nature.

The student needs to rank colleges based on a large number of factors. They are presented with a couple of options on how to proceed:

1. Rank the colleges holistically without any quantitative measurement.
2. Assign scores to colleges holistically or based on features such as location and prestige.

The problem with the second solution is that these scores are entirely arbitrary. The scale is never strictly defined, and as such, also frequently changes.

The solution is to compare just two schools. This is less arbitrary than assigning scores, and, with the Elo rating method, more quantitative than just ranking them.

I initially compared schools holistically, but this biased the choices towards prestige, even though the school may have been a worse fit with other features. For example, if I was looking for a small school with good academics, and I was presented with Harvey Mudd or Harvard, I would probably still choose Harvard, because, if I got in to both, Harvard would be a more desirable school. The prestige and difficulty of acceptance biases the results.

As a result, I separated the comparisons to the following features:

- Culture
- Location
- Prestige
- Major
- Affordability
- Gut

The "Gut" factor is a more holistic feature. Generally, if a decision can't be made on this feature in a second, it is probably a tie, since the "Gut" factor should be quick reaction.

Of course, these comparisons are as arbitrary as you make them. However, I do think it's easier to compare based on specific aspects as opposed to trying to make a holistic decision by yourself.

## Usage

When running the script, the colleges to consider are in an array in the script. For best results, I recommend 20 colleges or so. Any more would raise the risk of having to make too many comparisons.

This is what a prompt looks like:

```
Choose a University based on Location
1: Yale
    Score: 1500
2: UT Austin
    Score: 1500
Choose Yale (1) or UT Austin (2):
```

Entering `1` chooses Yale, `2` chooses UT Austin, `D` marks it as a draw, and `L` skips the question and lists the current ranked universities instead.

Entering `Q` quits, lists the ranked universities, and saves the data to a CSV file.

The scores are initialized to 1500, but you shouldn't read _too_ far into them.
