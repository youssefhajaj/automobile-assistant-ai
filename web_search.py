# web_search.py - Internet Search Module for Kounhany AI
# Uses DuckDuckGo for free web search (no API key required)

import urllib.request
import urllib.parse
import json
import re
from typing import Optional, List, Dict
from datetime import datetime

# Import analytics for caching
try:
    from analytics import cache_search_results, get_cached_search
    ANALYTICS_AVAILABLE = True
except ImportError:
    ANALYTICS_AVAILABLE = False

def search_duckduckgo(query: str, num_results: int = 5) -> List[Dict]:
    """
    Search DuckDuckGo and return results.
    Free, no API key required.
    Uses both Instant Answer API and HTML scraping as fallback.
    """
    # Check cache first
    if ANALYTICS_AVAILABLE:
        cached = get_cached_search(query)
        if cached:
            try:
                return json.loads(cached)
            except:
                pass

    results = []

    # Method 1: DuckDuckGo Instant Answer API
    try:
        encoded_query = urllib.parse.quote(query)
        url = f"https://api.duckduckgo.com/?q={encoded_query}&format=json&no_html=1&skip_disambig=1"

        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))

        # Abstract (main result)
        if data.get('Abstract'):
            results.append({
                'title': data.get('Heading', 'Résultat'),
                'snippet': data.get('Abstract'),
                'url': data.get('AbstractURL', ''),
                'source': data.get('AbstractSource', 'DuckDuckGo')
            })

        # Related topics
        for topic in data.get('RelatedTopics', [])[:num_results]:
            if isinstance(topic, dict) and topic.get('Text'):
                results.append({
                    'title': topic.get('Text', '')[:100],
                    'snippet': topic.get('Text', ''),
                    'url': topic.get('FirstURL', ''),
                    'source': 'DuckDuckGo'
                })

    except Exception as e:
        print(f"DuckDuckGo API error: {e}")

    # Method 2: If no results, try HTML scraping
    if not results:
        try:
            encoded_query = urllib.parse.quote(query)
            url = f"https://html.duckduckgo.com/html/?q={encoded_query}"

            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            })

            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8')

            # Simple regex extraction of results
            # Look for result snippets
            snippet_pattern = r'<a class="result__snippet"[^>]*>([^<]+)</a>'
            title_pattern = r'<a class="result__a"[^>]*>([^<]+)</a>'

            snippets = re.findall(snippet_pattern, html)
            titles = re.findall(title_pattern, html)

            for i, (title, snippet) in enumerate(zip(titles[:num_results], snippets[:num_results])):
                # Clean HTML entities
                title = title.replace('&amp;', '&').replace('&quot;', '"').replace('&#x27;', "'")
                snippet = snippet.replace('&amp;', '&').replace('&quot;', '"').replace('&#x27;', "'")

                results.append({
                    'title': title[:100],
                    'snippet': snippet,
                    'url': '',
                    'source': 'Web'
                })

        except Exception as e:
            print(f"DuckDuckGo HTML scraping error: {e}")

    # Cache results
    if ANALYTICS_AVAILABLE and results:
        cache_search_results(query, json.dumps(results))

    return results[:num_results]

def search_car_info(query: str) -> Dict:
    """
    Search for car-related information.
    Optimized for automotive queries.
    """
    # Add automotive context to query
    automotive_query = f"{query} voiture automobile"

    results = search_duckduckgo(automotive_query, num_results=3)

    if results:
        return {
            'success': True,
            'query': query,
            'results': results,
            'timestamp': datetime.now().isoformat()
        }
    else:
        return {
            'success': False,
            'query': query,
            'results': [],
            'message': 'Aucun résultat trouvé',
            'timestamp': datetime.now().isoformat()
        }

def search_car_price(brand: str, model: str, year: str = None) -> Dict:
    """
    Search for car price information.
    """
    query = f"prix {brand} {model}"
    if year:
        query += f" {year}"
    query += " Maroc"

    results = search_duckduckgo(query, num_results=3)

    return {
        'success': len(results) > 0,
        'brand': brand,
        'model': model,
        'year': year,
        'results': results,
        'disclaimer': "Les prix sont indicatifs. Contactez un concessionnaire pour le prix exact."
    }

def search_car_recall(brand: str, model: str = None) -> Dict:
    """
    Search for car recall information.
    """
    query = f"rappel {brand}"
    if model:
        query += f" {model}"
    query += " sécurité"

    results = search_duckduckgo(query, num_results=3)

    return {
        'success': len(results) > 0,
        'brand': brand,
        'model': model,
        'results': results
    }

def search_technical_info(topic: str) -> Dict:
    """
    Search for technical automotive information.
    """
    query = f"{topic} automobile technique"

    results = search_duckduckgo(query, num_results=3)

    return {
        'success': len(results) > 0,
        'topic': topic,
        'results': results
    }

def format_search_results(results: List[Dict], max_length: int = 500) -> str:
    """
    Format search results into a readable French response.
    """
    if not results:
        return "Je n'ai pas trouvé d'informations pertinentes sur internet."

    response_parts = ["🔍 **Voici ce que j'ai trouvé:**\n"]

    for i, result in enumerate(results[:3], 1):
        title = result.get('title', 'Sans titre')[:80]
        snippet = result.get('snippet', '')[:200]
        source = result.get('source', '')

        if snippet:
            response_parts.append(f"**{i}.** {snippet}")
            if source:
                response_parts.append(f"   _(Source: {source})_\n")

    response_parts.append("\n⚠️ *Ces informations proviennent d'internet et peuvent ne pas être à jour.*")

    return '\n'.join(response_parts)[:max_length]

def detect_search_intent(message: str) -> Optional[Dict]:
    """
    Detect if a message requires an internet search.
    Returns search parameters if search is needed.
    """
    message_lower = message.lower()

    # Price queries
    price_patterns = [
        r'prix\s+(?:de\s+)?(?:la\s+)?(\w+)\s+(\w+)',
        r'combien\s+(?:coûte|coute)\s+(?:une?\s+)?(\w+)\s+(\w+)',
        r'(\w+)\s+(\w+)\s+(?:prix|coût|cout)',
    ]

    for pattern in price_patterns:
        match = re.search(pattern, message_lower)
        if match:
            return {
                'type': 'price',
                'brand': match.group(1),
                'model': match.group(2) if len(match.groups()) > 1 else None
            }

    # Recall queries
    if any(word in message_lower for word in ['rappel', 'recall', 'défaut', 'problème connu']):
        # Try to extract brand
        brands = ['renault', 'peugeot', 'citroen', 'dacia', 'bmw', 'mercedes', 'audi',
                  'volkswagen', 'toyota', 'ford', 'fiat', 'opel', 'seat', 'skoda']
        for brand in brands:
            if brand in message_lower:
                return {
                    'type': 'recall',
                    'brand': brand
                }

    # General search for "what is", "how to" type queries
    search_triggers = ['c\'est quoi', 'qu\'est-ce que', 'comment fonctionne',
                       'différence entre', 'avantages', 'inconvénients',
                       'meilleur', 'comparaison', 'avis sur']

    if any(trigger in message_lower for trigger in search_triggers):
        return {
            'type': 'general',
            'query': message
        }

    return None

def perform_search(intent: Dict) -> str:
    """
    Perform the appropriate search based on detected intent.
    """
    search_type = intent.get('type', 'general')

    if search_type == 'price':
        result = search_car_price(
            intent.get('brand', ''),
            intent.get('model', ''),
            intent.get('year')
        )
        if result['success']:
            return format_search_results(result['results']) + f"\n\n{result['disclaimer']}"
        else:
            return "Je n'ai pas trouvé d'informations de prix. Pour un prix précis, contactez un concessionnaire."

    elif search_type == 'recall':
        result = search_car_recall(
            intent.get('brand', ''),
            intent.get('model')
        )
        if result['success']:
            return format_search_results(result['results'])
        else:
            return "Je n'ai pas trouvé d'informations de rappel pour ce véhicule."

    else:  # general search
        result = search_car_info(intent.get('query', ''))
        if result['success']:
            return format_search_results(result['results'])
        else:
            return "Je n'ai pas trouvé d'informations pertinentes."

# Test function
def test_search():
    """Test the search functionality."""
    print("Testing DuckDuckGo search...")

    # Test general search
    results = search_duckduckgo("vidange huile moteur", 3)
    print(f"Found {len(results)} results")

    for r in results:
        print(f"- {r.get('title', 'N/A')[:50]}...")

    # Test formatted output
    print("\nFormatted output:")
    print(format_search_results(results))

if __name__ == "__main__":
    test_search()
