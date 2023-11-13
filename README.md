# ChatgptPrompts
For some chatgpt prompts which I used  only for me.


## WordsLearning
Prompt="""
1. I will provide a text-like representation of CSV data, including two columns: "sentence" and "words."
2. You are required to add two new columns: "meanings" and "examples." The "meanings" column should contain the meanings of all the words listed in the "words" column. The "examples" column should include three additional examples for each word in the "words" column.
3. After adding the new columns, you will get the modified text-like CSV format.
4. Finally, you will convert the modified CSV text into HTML format.
5. Output the HTML formta text.
   
"""

May you should input again:"You should Repeat similar rows for the rest of the data in html,not me to do it." if there is a sentence likes "  <!-- Repeat similar rows for the rest of the data -->" in html output.
