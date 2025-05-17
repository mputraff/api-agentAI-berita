from newspaper import Article

def extract_article(url: str) -> str:
    article = Article(url)
    article.download()
    article.parse()
    return article.text