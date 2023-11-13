# ChatgptPrompts
For some chatgpt prompts which I used  only for me.


## WordsLearning
Prompt="""
The prompt is asking you to create an HTML table based on a CSV file with two columns: "Content" and "words." The "Content" column contains sentences, and the "words" column contains specific words from those sentences. For each pair of sentence and word, You need to provide the following information in HTML format:

1.The original sentence.
2.The target word.
3.The meaning of the target word.
4.Three additional examples of the target word used in different contexts.
Additionally, the HTML output should include all words in the "words" column pattern. The output should be organized in a table format, with each row corresponding to a pair of sentence and word.

For examples,I give you the csv file like following:
"Content","words":
"polls show Britons rate ""the countryside""
alongside the royal family","poll"
Your html output should like this:
""<tr>
    <td>polls show Britons rate "the countryside" alongside the royal family</td>
    <td>poll</td>
    <td>Meaning: A survey or vote to collect opinions or votes on a particular matter.</td>
    <td>Examples:
      <ul>
        <li>The newspaper conducted a poll to gauge public opinion on the upcoming election.</li>
        <li>They conducted a poll to determine the most popular candidate.</li>
        <li>The poll results showed a clear preference for environmental policies.</li>
      </ul>
    </td>
  </tr>
""


"""

Text="""
...
"""

User input next:
I need you Repeat similar entries for the remaining rows ,not me.
