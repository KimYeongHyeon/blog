#!/usr/bin/env python3
"""
Google Scholar 프로필에서 논문 정보를 가져와 publications.md를 업데이트하는 스크립트
"""

import re
from scholarly import scholarly
from datetime import datetime

# Google Scholar 사용자 ID
SCHOLAR_ID = "cLAlajcAAAAJ"

def get_scholar_data():
    """Google Scholar에서 데이터 가져오기"""
    try:
        author = scholarly.search_author_id(SCHOLAR_ID)
        author = scholarly.fill(author)
        return author
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def format_publication(pub):
    """논문 정보를 마크다운 형식으로 변환"""
    title = pub.get('bib', {}).get('title', 'Unknown Title')
    authors = pub.get('bib', {}).get('author', 'Unknown Authors')
    venue = pub.get('bib', {}).get('venue', 'Unknown Venue')
    year = pub.get('bib', {}).get('pub_year', 'Unknown Year')
    citations = pub.get('num_citations', 0)
    url = pub.get('pub_url', '')
    
    # 저자 이름에서 YeongHyeon Kim, YH Kim, KY Hyeon을 볼드 처리
    authors = re.sub(r'\b(YeongHyeon Kim|YH Kim|KY Hyeon)\b', r'**\1**', authors)
    
    md = f"**{title}**  \n"
    md += f"{authors}  \n"
    md += f"*{venue}*  \n"
    
    if url:
        md += f"[[Paper]]({url})"
    
    if citations > 0:
        md += f" • {citations} citations"
    
    md += "\n\n"
    
    return md, year

def update_publications_file(author):
    """publications.md 파일 업데이트"""
    
    publications_by_year = {}
    
    # 논문들을 연도별로 분류
    for pub in author.get('publications', []):
        pub_data = scholarly.fill(pub)
        md_text, year = format_publication(pub_data)
        
        if year not in publications_by_year:
            publications_by_year[year] = []
        publications_by_year[year].append(md_text)
    
    # Markdown 파일 생성
    content = f"""---
title: "Publications"
layout: "publications"
url: "/publications/"
summary: "Research Publications"
---

## Journal Articles

"""
    
    # 연도별로 정렬하여 출력 (최신순)
    for year in sorted(publications_by_year.keys(), reverse=True):
        content += f"### {year}\n\n"
        for pub_md in publications_by_year[year]:
            content += pub_md
            content += "---\n\n"
    
    # Citation Statistics
    total_citations = author.get('citedby', 0)
    h_index = author.get('hindex', 0)
    i10_index = author.get('i10index', 0)
    
    content += f"""## Citation Statistics

- **Total Citations:** {total_citations}
- **h-index:** {h_index}
- **i10-index:** {i10_index}
- [Google Scholar Profile](https://scholar.google.co.kr/citations?user={SCHOLAR_ID}&hl=ko)

---

## Research Areas

- Artificial Intelligence
- Computer Vision
- Machine Learning
- Data Analysis
- Active Learning
- Object Detection

---

*Last updated: {datetime.now().strftime("%B %Y")}*
"""
    
    # 파일 저장
    with open('content/publications.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Publications updated successfully!")
    print(f"   Total Citations: {total_citations}")
    print(f"   h-index: {h_index}")
    print(f"   i10-index: {i10_index}")

if __name__ == "__main__":
    print("🔄 Fetching data from Google Scholar...")
    author = get_scholar_data()
    
    if author:
        print("📝 Updating publications.md...")
        update_publications_file(author)
    else:
        print("❌ Failed to fetch data from Google Scholar")
        exit(1)

