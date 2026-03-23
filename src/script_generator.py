from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

def generate_script(topic, style="educational"):
    hook = f"Did you know that {topic} can completely change your life?"
    problem = "Most people struggle with this because they don't know where to start."
    points = [
        f"Step 1 - Understanding the basics of {topic}",
        f"Step 2 - Building your strategy around {topic}",
        f"Step 3 - Taking action and seeing results"
    ]
    cta = "If this helped you, smash that subscribe button!"

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

def main():
    console.print("[bold]Welcome to Creator AI Pipeline[/] 🎬\n")
    topic = input("Enter your video topic: ")
    style = input("Enter style (educational / entertaining / motivational): ")
    
    console.print("\n[bold]Generating your script...[/]\n")
    script = generate_script(topic, style)
    display_script(script)

if __name__ == "__main__":
    main()