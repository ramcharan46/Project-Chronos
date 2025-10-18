import os
import sys
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

def reconstruct(text):
    prompt = f'Reconstruct this internet text by decoding all slang, abbreviations, and references into plain English. Original: "{text}". Provide ONLY the reconstructed text, nothing else.'
    return client.models.generate_content(model="gemini-2.0-flash-exp", contents=prompt).text.strip()

def extract_terms(text):
    prompt = f'From this text: "{text}", extract ONLY the slang terms, abbreviations, and cultural references (like "smh", "g2g", "top 8", etc.). Return them as a comma-separated list, nothing else.'
    return client.models.generate_content(model="gemini-2.0-flash-exp", contents=prompt).text.strip()

def search_term(term):
    search_url = "https://api.duckduckgo.com/"
    params = {'q': f"{term} meaning slang abbreviation", 'format': 'json', 'no_html': 1}
    
    try:
        response = requests.get(search_url, params=params, timeout=10)
        data = response.json()
        
        results = []
        if data.get('AbstractURL') and data['AbstractURL']:
            results.append({'url': data['AbstractURL'], 'desc': f"Explaining '{term}'"})
        
        if data.get('RelatedTopics'):
            for topic in data['RelatedTopics'][:2]:
                if isinstance(topic, dict) and 'FirstURL' in topic:
                    results.append({'url': topic['FirstURL'], 'desc': f"About '{term}'"})
        
        if results:
            return results
        
        #  we fallback to known common slang dictionaries if no results found
        
        term_clean = term.lower().strip()
        fallback_urls = {
            'smh': 'https://www.dictionary.com/e/slang/smh/',
            'lol': 'https://www.dictionary.com/e/slang/lol/',
            'g2g': 'https://www.internetslang.com/G2G-meaning-definition.asp',
            'ttyl': 'https://www.internetslang.com/TTYL-meaning-definition.asp',
            'brb': 'https://www.internetslang.com/BRB-meaning-definition.asp',
            'gg': 'https://www.dictionary.com/e/slang/gg/',
            'wp': 'https://www.urbandictionary.com/define.php?term=wp',
            'ez': 'https://www.urbandictionary.com/define.php?term=ez',
            'pwned': 'https://www.dictionary.com/e/slang/pwned/',
            'noob': 'https://www.dictionary.com/e/slang/noob/',
            'noobs': 'https://www.dictionary.com/e/slang/noob/',
            'top 8': 'https://en.wikipedia.org/wiki/Myspace#Features',
            'imo': 'https://www.internetslang.com/IMO-meaning-definition.asp',
            'imho': 'https://www.internetslang.com/IMHO-meaning-definition.asp',
            'afk': 'https://www.internetslang.com/AFK-meaning-definition.asp',
            'rofl': 'https://www.dictionary.com/e/slang/rofl/',
            'lmao': 'https://www.dictionary.com/e/slang/lmao/',
            'ftw': 'https://www.dictionary.com/e/slang/ftw/',
            'fml': 'https://www.dictionary.com/e/slang/fml/',
        }
        
        if term_clean in fallback_urls:
            return [{'url': fallback_urls[term_clean], 'desc': f"Definition of '{term}'"}]
        
        return [{'url': f'https://www.urbandictionary.com/define.php?term={term}', 'desc': f"Definition of '{term}'"}]
        
    except:
        return [{'url': f'https://www.urbandictionary.com/define.php?term={term}', 'desc': f"Definition of '{term}'"}]

def search_all_terms(terms_str):
    terms = [t.strip() for t in terms_str.split(',')]
    all_sources = []
    
    for term in terms:
        if term:
            sources = search_term(term)
            all_sources.extend(sources)
    
    return all_sources

def show_report(original, reconstructed, sources):
    report = f'\n{"="*60}\n--- RECONSTRUCTION REPORT ---\n{"="*60}\n\n'
    report += f'[Original Fragment]\n> "{original}"\n\n'
    report += f'[AI-Reconstructed Text]\n> "{reconstructed}"\n\n'
    report += '[Contextual Sources]\n'
    
    for s in sources:
        report += f"* {s['url']}\n"
        if s.get('desc'):
            report += f"  ({s['desc']})\n"
    
    report += f'\n{"="*60}\n'
    print(report)
    
    with open("reconstruction_report.txt", 'a', encoding='utf-8') as f:
        f.write(report)
    print("Report saved to reconstruction_report.txt")

def main():
    print(f'\n{"="*60}\nPROJECT CHRONOS: The AI Archeologist\n{"="*60}\n')
    
    if len(sys.argv) < 2:
        print('Usage: python main.py "your text here"\n')
        return
    
    text = sys.argv[1]
    
    print("Analyzing fragment...")
    reconstructed = reconstruct(text)
    
    print("Extracting slang and abbreviations...")
    terms = extract_terms(text)
    
    print(f"Searching for: {terms}")
    sources = search_all_terms(terms)
    
    print("Generating report...\n")
    show_report(text, reconstructed, sources)

if __name__ == "__main__":
    main()