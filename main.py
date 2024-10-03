import pyfiglet
import random
import argparse

def create_ascii_banner(text: str, font: str = "standard") -> str:
    """
    Generates an ASCII banner from the provided text using the specified font.
    
    Parameters:
    text (str): The text to convert into an ASCII banner.
    font (str): The font to use for the ASCII banner. Default is "standard".
    
    Returns:
    str: The generated ASCII banner.
    """
    # Create a Figlet object with the specified font
    figlet = pyfiglet.Figlet(font=font)
    
    # Generate ASCII banner
    ascii_banner = figlet.renderText(text)
    
    return ascii_banner

def list_random_fonts(num_fonts: int) -> None:
    """
    A function to list a given number of random fonts from the list of possible fonts.
    """
    possible_fonts = pyfiglet.FigletFont.getFonts()
    random_fonts = random.sample(possible_fonts, num_fonts)
    print("Here are some possible fonts you can use:")
    print(", ".join(random_fonts))  # Display first 30 random fonts from the list of possible
    
    

def main():    # Welcome message
    # Argument parser setup
    parser = argparse.ArgumentParser(description="ASCII Banner Generator with multiple modes.")

    # Common arguments for all modes
    parser.add_argument("text", type=str, help="Text to generate the ASCII banner.")

    parser.add_argument(
    "--mode", 
    type=str, 
    choices=["list-fonts", "generate", "random-font"],
    default="random-font",
    help="Mode of operation: list-fonts, generate, or random-font"
    )
    
    # Optional font argument for the 'generate' mode
    parser.add_argument(
        "--font", 
        type=str, 
        default="standard", 
        help="Font to use for the ASCII banner (default is 'standard') to use in 'generate' mode."
    )

    # Argument for the number of fonts to list in 'list-fonts' mode
    parser.add_argument(
        "--num-fonts", 
        type=int, 
        default=30, 
        help="Number of random fonts to list in 'list-fonts' mode."
    )
    
    
    # Parse the arguments
    args = parser.parse_args()
    
    
    # Mode handling
    if args.mode == "list-fonts":
        # List random fonts mode
        list_random_fonts(args.num_fonts)
        font = input("Enter the font for the ASCII banner (default is 'standard'): ") 
        print(create_ascii_banner(args.text, font))

    elif args.mode == "random-font":
        # Random font selection mode
        possible_fonts = pyfiglet.FigletFont.getFonts()
        random_font = random.choice(possible_fonts)
        print(create_ascii_banner(args.text, random_font))

    else:
        # Default 'generate' mode
        print(create_ascii_banner(args.text, args.font))


if __name__ == "__main__":
    main()

