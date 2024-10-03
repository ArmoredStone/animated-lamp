import pyfiglet
import random

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

if __name__ == "__main__":
    # Welcome message
    print("Welcome to the ASCII Banner Generator!")
    
    # List of possible fonts
    possible_fonts = pyfiglet.FigletFont.getFonts()
    random_fonts = random.sample(possible_fonts, 30)
    print("Here are some possible fonts you can use:")
    print(", ".join(random_fonts))  # Display first 30 random fonts from the list of possible    
    # Example usage
    text = input("Enter the text for the ASCII banner: ")
    font = input("Enter the font for the ASCII banner (default is 'standard'): ") or "standard"
    print(create_ascii_banner(text, font))
