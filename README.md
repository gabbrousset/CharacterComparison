# CharacterComparison
comp370 final project


## Project Structure
- data/
  - raw/            # raw downloaded data
  - processed/      # clean after prep_data.py script is run
  - characters/     # one file of extracted dialogue per character
  - annotations/
    - nonbanter/    # annotated dialogue per character with banter column
      - filtered/   # only 300 meaningful lines per character
  - analysis        # TD-IDF
- scripts/
  - prep_data.py
  - analyze_script.py
  - extract_character.py
  - shuffle_csv.py
  - filter_col.py


## Plan
### Data Collection / Cleaning
- Choose show/movie(s)
- Find script
- Count lines per character
- Pick 3-5 side characters with more than 300 lines
- Collect dialogue from scripts
- Extract 300+ meaningful lines per character
  - unbiased (random?)
  - not reactions / banter

### Open Coding
- Sample 100 lines per character
- Annotate lines with ONE topic
- Refine topics (pick only 3-8 topics in total)

### Manual Annotation (Full Dataset)
- Assign one of 3-8 topics to every line (900 lines)

### Analysis
- Compute 10 words in each category with the highest tf-idf scores
- LLM Summary of each category
