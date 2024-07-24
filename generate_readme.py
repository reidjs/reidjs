from datetime import datetime
import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why do Java developers wear glasses? Because they don't C#.",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "Why don't programmers like nature? It has too many bugs.",
    "How do you comfort a JavaScript bug? You console it.",
    "What's a programmer's favorite type of music? Algo-rhythm.",
    "Why was the programmer poor? Because he didn't get arrays.",
    "What's a computer's favorite snack? Microchips.",
    "Why was the computer cold? It left its Windows open.",
    "How do you know if a computer is hungry? It takes a lot of bytes.",
    "Why did the database administrator break up with the SQL server? She found it too controlling.",
]

# Generate the content for the README
content = f"""## Today's Joke
{random.choice(jokes)}

*Updated {datetime.now().strftime('%B %d, %Y')} (UTC)*
"""

with open("README.md", "w") as f:
    f.write(content)
