# 🧾 SEO a WordPress Cheat Sheet

## 🔗 Interné odkazy

| Pojem | Význam | Kontrola |
|---|---|---|
| Inlinks | odkazy na vybranú URL | Screaming Frog → Internal → Inlinks |
| Unique Inlinks | počet rôznych zdrojových URL | Screaming Frog |
| Outlinks | odkazy z vybranej URL | Screaming Frog → Outlinks |
| Crawl Depth | vzdialenosť od štartovacej URL podľa crawlera | Internal / Site Structure |
| Anchor text | text odkazu | Inlinks → Anchor Text |
| Orphaned Content | nedostatočne prelinkovaný obsah | Yoast Premium → Workouts |
| Cornerstone | prioritná nosná stránka | Yoast SEO v editore |
| Text Link Counter | počet interných odkazov | WordPress → Články / Yoast |

## 🛠️ Yoast SEO

| Funkcia | Kde |
|---|---|
| SEO title a Meta description | Editor obsahu → Yoast SEO |
| Focus keyphrase | Editor obsahu → Yoast SEO |
| Internal linking suggestions | Yoast SEO Premium → panel editora |
| Text Link Counter | Yoast Settings → Site features / Štruktúra webu |
| Orphaned content | Yoast SEO Premium → Workouts |
| Cornerstone Content | Editor článku → Yoast SEO |
| SEO data optimization | Yoast SEO → Tools |
| Canonical | Yoast SEO → Advanced |

## 📊 GA4 a Google Search Console

| Čo zisťujeme | Nástroj | Umiestnenie |
|---|---|---|
| Sessions (návštevy) | GA4 | Reports → Acquisition → Traffic acquisition |
| Views (zobrazenia stránok) | GA4 | Reports → Engagement → Pages and screens |
| Zapojenie stránok | GA4 | Engagement → Pages and screens |
| Cesty používateľov | GA4 | Explore → Path exploration |
| Kliknutia z Google | GSC | Výkonnosť → Výsledky vyhľadávania |
| Zobrazenia vo vyhľadávaní | GSC | Výkonnosť → Výsledky vyhľadávania |
| Výkon konkrétnej URL | GSC | Výsledky vyhľadávania → Stránky |
| Kliknutia na konkrétny interný odkaz | vlastná GA4 udalosť | vyžaduje implementáciu merania |

## 🧪 Lokálny audit

```bash
python3 scripts/internal_link_audit.py --pages data/pages.csv --links data/links.csv
```

## 🔒 Bezpečnostné upozornenia

- Nemeňte produkčnú URL alebo canonical bez pochopenia presmerovaní.
- `noindex` nie je to isté ako blokovanie v `robots.txt`.
- Sitemap nezaručuje indexáciu.
- Yoast zelená kontrolka nezaručuje pozície v Google.
- Screaming Frog Free analyzuje maximálne 500 URL, preto výsledky väčšieho webu môžu byť neúplné.
- GA4 Views ≠ Sessions; GSC clicks ≠ interné kliknutia.
- Relevantnosť odkazov nie je len počet odkazov.
