import json
import os
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()

FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")

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

        content = result.markdown

        # Clean markdown content
        content = content.replace("#", "")
        content = content.replace("*", "")
        content = content.replace("\n\n", "\n")

        knowledge.append({
            "id": website["id"],
            "name": website["name"],
            "url": website["url"],
            "category": website["category"],
            "content": content[:3000]
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
