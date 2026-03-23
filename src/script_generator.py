from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import json
import os
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

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

def generate_ai_script(topic, style="educational"):
    from openai import OpenAI
    
    client = OpenAI(
        base_url="https://router.huggingface.co/v1",
        api_key=os.getenv("HUGGINGFACE_API_TOKEN")
    )
    
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional YouTube script writer."
                },
                {
    "role": "user",
    "content": f"""Write a detailed YouTube script about '{topic}' in a {style} style.

The script should be 3-5 minutes long when read aloud.

Use this exact structure:

HOOK (30 seconds): A powerful opening line that grabs attention immediately

PROBLEM (1 minute): Explain the core problem or question this video answers

MAIN POINT 1 (1 minute): First key insight with explanation and example

MAIN POINT 2 (1 minute): Second key insight with explanation and example

MAIN POINT 3 (1 minute): Third key insight with explanation and example

CONCLUSION (30 seconds): Wrap up the key takeaways

CTA (15 seconds): Call to action to subscribe, like and comment

Write in a conversational tone like you are talking directly to the viewer."""
}
            ],
            max_tokens=1000
        )
        
        generated_text = completion.choices[0].message.content
        
        return {
            "topic": topic,
            "style": style,
            "generated_text": generated_text,
            "source": "llama-3.1-8b"
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "detail": repr(e)
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
    console.print("\n[bold]Generating AI script...[/]\n")
    ai_script = generate_ai_script(topic, style)

    if "error" in ai_script:
        console.print(f"[bold red]Error:[/] {ai_script['error']}")
        console.print(f"[bold red]Detail:[/] {ai_script.get('detail', 'no detail')}")
    else:
      console.print(Panel(ai_script["generated_text"], title="AI Generated Script"))

if __name__ == "__main__":
    main()