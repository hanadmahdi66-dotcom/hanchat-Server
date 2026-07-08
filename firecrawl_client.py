import json
import os
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("fc-fd621a6845f6420c9153090a4b1eb417")

firecrawl = FirecrawlApp(api_key=FIRECRAWL_API_KEY)


# Akhri websites.json
with open("websites.json", "r", encoding="utf-8") as file:
    websites = json.load(file)


knowledge = []


# Mid mid u crawl garee websites-ka
for website in websites:
    print(f"Crawling: {website['name']}")

    try:
        result = firecrawl.scrape(
            website["url"],
            formats=["markdown"]
        )

        knowledge.append({
            "id": website["id"],
            "name": website["name"],
            "url": website["url"],
            "category": website["category"],
            "content": result.markdown
        })

        print("✅ Done")

    except Exception as e:
        print(f"❌ Error {website['name']}: {e}")


# Ku keydi knowledge.json
with open("knowledge.json", "w", encoding="utf-8") as file:
    json.dump(
        {
            "knowledge": knowledge
        },
        file,
        indent=2,
        ensure_ascii=False
    )


print("🎉 All websites saved to knowledge.json")