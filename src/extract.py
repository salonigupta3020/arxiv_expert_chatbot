import json

input_path = r"C:\Users\Admin\AppData\Local\Temp\f608da24-abfc-41bd-80cf-e21033e7e52c_archive.zip.52c\arxiv-metadata-oai-snapshot.json"
output_path = "../data/arxiv_cs.json"  # Save output to 'data' folder

def filter_cs_papers(input_file, output_file):
    """Extracts computer science papers and saves them to a new JSON file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            paper = json.loads(line)
            if 'cs' in paper.get('categories', ''):
                outfile.write(json.dumps(paper) + '\n')
    print(f"Filtered computer science papers saved to: {output_file}")

if __name__ == "__main__":
    filter_cs_papers(input_path, output_path)

def extract_info(query):
    """Extracts relevant information from the query."""

    return f"Extracted information related to: {query}"