
import argparse
import sys
import re

def is_only_links(line):
    """
    Checks if a line consists solely of one or more Markdown links,
    potentially prefixed with Markdown images (used as icons).
    e.g., "[![...](...)Link1](...)" or "[Link1](...) [Link2](...)"
    """
    # Temporarily remove image links to simplify the check for text links
    line_no_images = re.sub(r'!\\\[[^\\]*?\\]\(.*?\\]\)', '', line)
    
    # Remove all valid markdown text links from the line
    line_without_links = re.sub(r'\\[[^\\]+\\]\(.*?\\]\)', '', line_no_images)
    
    # If the line is empty or just whitespace after removing links, it's a link-only line
    return line_without_links.strip() == ''

def clean_markdown(input_file, output_file):
    """
    Reads a markdown file, removes common junk patterns using string matching, 
    and writes the cleaned content to a new file.
    """
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file {input_file}: {e}", file=sys.stderr)
        sys.exit(1)

    cleaned_lines = []
    in_footer_section = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped_line = line.strip()

        # Once we hit the footer's horizontal rule, skip all subsequent lines
        if stripped_line == '* * *':
            in_footer_section = True
        
        if in_footer_section:
            i += 1
            continue

        # List of simple string checks to identify junk lines
        junk_patterns = [
            "[50+ Advanced ChatGPT Prompts. Get It Free!]",
            "[TypingMind Docs]",
        ]

        is_junk = False
        for pattern in junk_patterns:
            if pattern in line:
                is_junk = True
                break
        
        # New, more robust check for breadcrumbs or local ToC lines
        if not is_junk and stripped_line.startswith('[') and is_only_links(stripped_line):
            is_junk = True

        if is_junk:
            # If it's a junk line, also skip the following blank line if it exists
            if i + 1 < len(lines) and lines[i+1].strip() == "":
                i += 2
            else:
                i += 1
            continue

        cleaned_lines.append(line)
        i += 1

    # Join the cleaned lines and remove excessive blank lines
    cleaned_content = "".join(cleaned_lines)
    while "\n\n\n" in cleaned_content:
        cleaned_content = cleaned_content.replace("\n\n\n", "\n\n")

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_content.strip())
        print(f"Successfully cleaned '{input_file}' and saved to '{output_file}'")
    except Exception as e:
        print(f"Error writing to file {output_file}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """
    Main function to parse command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Cleans junk patterns from a markdown file using simple string matching."
    )
    parser.add_argument(
        "input_file",
        metavar="INFILE",
        help="Path to the input markdown file."
    )
    parser.add_argument(
        "-o", "--output",
        dest="output_file",
        required=True,
        help="Path to the output cleaned markdown file."
    )
    args = parser.parse_args()

    clean_markdown(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
