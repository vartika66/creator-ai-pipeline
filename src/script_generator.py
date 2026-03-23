from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json
import os
from datetime import datetime

console = Console()

def generate_script(topic, style="educational"):
    
    if style == "educational":
        hook = f"Today we're going to learn everything about {topic}."
        problem = "Most people get this wrong because they skip the fundamentals."
        points = [
            f"Step 1 - What exactly is {topic} and why it matters",
            f"Step 2 - The most important things to know about {topic}",
            f"Step 3 - How to apply this knowledge today"
        ]
        cta = "Drop your questions in the comments below!"

    elif style == "entertaining":
        hook = f"I tried {topic} for 30 days and this is what happened..."
        problem = "Nobody talks about the real struggles behind this."
        points = [
            f"Day 1 - My first experience with {topic}",
            f"Day 15 - When everything went wrong",
            f"Day 30 - The shocking results"
        ]
        cta = "Like this video if you want part 2!"

    elif style == "motivational":
        hook = f"Your life will never be the same after you understand {topic}."
        problem = "Most people give up before they even start."
        points = [
            f"Truth 1 - Why {topic} is the key to your success",
            f"Truth 2 - What separates winners from quitters",
            f"Truth 3 - The one thing you must do starting today"
        ]
        cta = "Share this with someone who needs to hear it!"

    else:
        hook = f"Everything you need to know about {topic}."
        problem = "This topic is more important than you think."
        points = [
            f"Point 1 about {topic}",
            f"Point 2 about {topic}",
            f"Point 3 about {topic}"
        ]
        cta = "Subscribe for more content!"

    return {
        "topic": topic,
        "style": style,
        "hook": hook,
        "problem": problem,
        "points": points,
        "cta": cta
    }

def display_script(script):
    console.print(Panel(f"[bold yellow]Topic:[/] {script['topic']}", title="Creator AI Pipeline"))
    console.print(f"\n[bold green]HOOK:[/] {script['hook']}")
    console.print(f"\n[bold red]PROBLEM:[/] {script['problem']}")
    console.print("\n[bold blue]MAIN POINTS:[/]")
    for point in script["points"]:
        console.print(f"  • {point}")
    console.print(f"\n[bold magenta]CTA:[/] {script['cta']}")

def save_script(script):
    os.makedirs("data", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"data/script_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(script, f, indent=4)
    
    console.print(f"\n[bold green]Script saved to {filename}[/]")

def main():
    console.print("[bold]Welcome to Creator AI Pipeline[/] 🎬\n")
    topic = input("Enter your video topic: ")
    style = input("Enter style (educational / entertaining / motivational): ")
    
    console.print("\n[bold]Generating your script...[/]\n")
    script = generate_script(topic, style)
    display_script(script)
    save_script(script) 

if __name__ == "__main__":
    main()