"""
Infographic Prompt Generator
---------------------------
This script generates a set of prompts for creating daily infographics for a given week, following the EML project visual and stylistic guidelines.

Usage:
- Run this script in Visual Studio Code.
- Enter the start and end date for the week (YYYY-MM-DD).
- Enter a summary of the week's learning or documentation focus.
- The script will output a prompt for each day in the range, ready to use for image generation.
"""

import datetime

def get_date_range(start_date, end_date):
    start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    delta = (end - start).days + 1
    return [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(delta)]

PROMPT_TEMPLATE = '''\
Generate an infographic on the following text for {date}.
Use the following specifications:
Generate a spectacular infographic with a realistic sketch style. The component parts and whole infographic must draw the observer into the picture: with dynamic camera angles. These combinations of perspectives are cleverly used to draw the observer into the links, combinations and graphical representations. The perspective should be structured and system oriented building understanding on the text that follows. Ensure that all images are drawn with black fine-line pen. The text must be written in black. Images must be in black with felt tip pen, with minor touches of dark red pen. Hatch with various colors using a felt tip pen using carefully chosen tones, that enhance the work and draw the observer’s attention into exploring the art work. Two images should be hatched with deep red or blue fine line pen. All Images are drawn in strong black line, using various guages and tones of ink pen; on paper using a black or dark brown felt tip or fine-line pen. Second level features should be with a various light or combinations of dark brown or grey pencil. Use the style of filling spaces of images  i.e., hatchings in   colored pencil. Color should be used to display important features, emphasizing similarities in elements and related concepts. Use a realistic, detailed style (artistic refined) with hatching for all art. Ensure that the page brings a new line of sight (camera angle (perspective that fits the content)); an infographic styled in landscape layout. Include dark brown text boxes with black handwritten text that describe the key ideas with commentary and examples to ensure understanding. Ensure that the images are not over dominating the page. The image should have a 16:9 ratio.

Learning focus for this day:\n{learning}\n'''

def main():
    print("EML Infographic Prompt Generator\n-------------------------------")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    learning = input("Enter a summary of the week's learning or documentation focus: ")
    dates = get_date_range(start_date, end_date)
    print("\nGenerated Prompts:\n")
    for date in dates:
        print(PROMPT_TEMPLATE.format(date=date, learning=learning))
        print("-"*80)

if __name__ == "__main__":
    main()
