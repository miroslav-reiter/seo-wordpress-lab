#!/usr/bin/env python3
"""Bezpečný lokálny tréningový audit interných odkazov v CSV (bez siete)."""
import argparse
import csv
from collections import Counter, defaultdict, deque
from pathlib import Path

def read_csv(path, required):
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        rd = csv.DictReader(stream)
        if not rd.fieldnames or not required.issubset(set(rd.fieldnames)):
            raise ValueError(f"{path}: chybaju stlpce {sorted(required)}")
        return list(rd)

def audit(pages_path, links_path, root):
    pages = read_csv(pages_path, {"url", "title", "indexable"})
    links = read_csv(links_path, {"source", "target", "anchor", "placement"})
    urls = {p["url"] for p in pages}
    if len(urls) != len(pages):
        raise ValueError("V pages.csv su duplicitne URL")
    if root not in urls:
        raise ValueError(f"Startovacia URL {root} sa nenachadza v pages.csv")
    indegree = Counter()
    unique_from = defaultdict(set)
    graph = defaultdict(set)
    broken = []
    vague = []
    for link in links:
        src, dst = link["source"], link["target"]
        if src not in urls or dst not in urls:
            broken.append(link)
        if src in urls and dst in urls:
            indegree[dst] += 1
            unique_from[dst].add(src)
            graph[src].add(dst)
        if link["anchor"].strip().casefold() in {
            "kliknite sem", "viac informacii", "viac informácií", "tu", "click here"
        }:
            vague.append(link)
    depth = {root: 0}
    queue = deque([root])
    while queue:
        src = queue.popleft()
        for dst in sorted(graph[src]):
            if dst not in depth:
                depth[dst] = depth[src] + 1
                queue.append(dst)
    print("URL | Inlinks | Unique inlinks | Crawl depth | Indexable")
    for p in pages:
        url = p["url"]
        print(f"{url} | {indegree[url]} | {len(unique_from[url])} | {depth.get(url, 'nezistena')} | {p['indexable']}")
    print("\nOSIRELE (podla dostupnych links.csv):")
    for p in pages:
        if p["url"] != root and len(unique_from[p["url"]]) == 0:
            print("-", p["url"])
    print("\nODKAZY NA NEZNAME URL:")
    for e in broken:
        print("-", e["source"], "->", e["target"])
    print("\nODKAZY NA NEINDEXOVATELNE CIELE:")
    indexed = {p["url"]: p["indexable"].lower() in {"yes", "true", "1"} for p in pages}
    for e in links:
        if e["target"] in indexed and not indexed[e["target"]]:
            print("-", e["source"], "->", e["target"])
    print("\nNEVYSTIZNE ANCHOR TEXTY:")
    for e in vague:
        print("-", repr(e["anchor"]), e["source"], "->", e["target"])
    print("\nPoznamka: Ide o modelove CSV, nie crawler ziveho webu.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lokalny SEO audit internych odkazov")
    parser.add_argument("--pages", default="data/pages.csv")
    parser.add_argument("--links", default="data/links.csv")
    parser.add_argument("--root", default="/")
    args = parser.parse_args()
    audit(args.pages, args.links, args.root)
