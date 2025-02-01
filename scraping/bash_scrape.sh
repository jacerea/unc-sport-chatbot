#!/bin/bash

# Ensure xmllint is installed
if ! command -v xmllint &> /dev/null; then
    echo "xmllint is not installed. Please install it (e.g., sudo apt install libxml2-utils)."
    exit 1
fi

# URL of the Boston Celtics page on ESPN
URL="https://www.espn.com/nba/team/_/name/bos/boston-celtics"

# File to save the output
OUTPUT_FILE="celtics_wins_losses.txt"

# Fetch the webpage content
html_content=$(curl -s "$URL")

# Extract wins and losses using xmllint (XPath queries)Schedule__Record h8 fr
wins=$(echo "$html_content" | xmllint --html --xpath "string(//div[contains(@class, 'Schedule__Header overflow-hidden bb db brdr-clr-gray-09 bg-clr-white')]//span[@class='Schedule__Record h8 fr'])" 2>/dev/null)
losses=$(echo "$html_content" | xmllint --html --xpath "string(//div[contains(@class, 'Schedule__Header overflow-hidden bb db brdr-clr-gray-09 bg-clr-white')]//span[@class='Schedule__Record h8 fr'])" 2>/dev/null)
# wins=$(echo "$html_content" | xmllint --html --xpath "string(//div[contains(@class, 'Record')]//span[@class='wins'])" 2>/dev/null)
# losses=$(echo "$html_content" | xmllint --html --xpath "string(//div[contains(@class, 'Record')]//span[@class='losses'])" 2>/dev/null)

# Check if data was extracted
if [ -z "$wins" ] || [ -z "$losses" ]; then
    echo "Failed to scrape wins and losses. Check the webpage structure or XPath queries."
    exit 1
fi

# Save the results to the file
echo "Boston Celtics Wins: $wins" > "$OUTPUT_FILE"
echo "Boston Celtics Losses: $losses" >> "$OUTPUT_FILE"

echo "Wins and losses saved to $OUTPUT_FILE"
