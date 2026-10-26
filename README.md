# 🧪 seo-wordpress-lab

**Testovací a vzdelávací repozitár na praktické precvičovanie SEO, WordPress, WooCommerce, Yoast SEO, interného prelinkovania, technického SEO a analytiky.**

Materiály sú určené SEO konzultantom, SEO špecialistom, správcom webových stránok a internetových obchodov, tvorcom obsahu, WordPress používateľom, webovým vývojárom aj študentom. Repozitár je koncipovaný podobne ako [curl-lab](https://github.com/miroslav-reiter/curl-lab): **README + odborné príklady + cheat sheet + testovacie dáta + spustiteľné skripty**.

> **Bezpečné trénovanie:** CSV dáta sú fiktívne. Skript pracuje lokálne, nemení dáta a neodosiela sieťové požiadavky. Ukážky vo WordPresse odporúčame vykonávať na testovacej inštalácii, nie automaticky na produkčnom webe VITA.sk.

## 📌 Čo je SEO

**SEO (Search Engine Optimization)** je súbor obsahových, technických a analytických postupov, ktorými zlepšujeme dostupnosť, zrozumiteľnosť a použiteľnosť webového obsahu pre vyhľadávače a návštevníkov. SEO nie je iba práca s kľúčovými slovami: riešime tiež informačnú architektúru, interné odkazy, indexovateľnosť, výkon, štruktúrované dáta, interpretáciu výsledkov a používateľské potreby.

**WordPress** je redakčný systém (CMS), **WooCommerce** jeho e-commerce rozšírenie a **Yoast SEO** plugin poskytujúci pomôcky pre SEO analýzu, nastavenia metadát a interné prelinkovanie. **Google Search Console (GSC)** sleduje výkon vo Vyhľadávaní Google a **Google Analytics 4 (GA4)** meria aktivitu na stránkach/aplikáciách. **Screaming Frog SEO Spider** je samostatný SEO crawler na technický audit.

## 🎯 Na čo sa repozitár používa v praxi

- optimalizácia článkov, podstránok a produktov vo WordPresse;
- tvorba relevantných interných odkazov a vhodných anchor textov;
- práca s Yoast SEO Free a Premium vrátane interných odporúčaní;
- Cornerstone Content, Orphaned Content a Text Link Counter;
- diagnostika SEO Data Optimization, Indexables a chybových hlásení;
- audit indexácie, canonical, robots, sitemap a presmerovaní;
- technický audit v Screaming Frog – Inlinks, Outlinks, Crawl Depth;
- správna interpretácia návštev, zapojenia, kliknutí a zobrazení v GA4 a GSC;
- precvičenie počítania interných odkazov a vyhľadávania osirelých URL na testovacích CSV;
- príprava SEO reportov, kontrolných zoznamov a odporúčaní.

## 📁 Štruktúra repozitára

| Súbor / priečinok | Obsah |
|---|---|
| [seo-wordpress-priklady.md](seo-wordpress-priklady.md) | 20 praktických postupov pre on-page SEO, WordPress, WooCommerce a Yoast |
| [seo-interne-odkazy-yoast.md](seo-interne-odkazy-yoast.md) | interné prelinkovanie, anchor texty, link suggestions, Cornerstone, Orphaned |
| [seo-audit-screaming-frog.md](seo-audit-screaming-frog.md) | Crawl Depth, Inlinks, Outlinks, HTTP status, indexovateľnosť |
| [seo-ga4-gsc.md](seo-ga4-gsc.md) | návštevy a zapojenie v GA4, kliknutia/zobrazenia v GSC, meranie výsledkov |
| [seo-cheatsheet.md](seo-cheatsheet.md) | prehľadné tabuľky nástrojov, metrík a najčastejších volieb |
| [data/pages.csv](data/pages.csv) | fiktívne URL testovacieho webu |
| [data/links.csv](data/links.csv) | fiktívne interné odkazy s anchor textmi |
| [data/README.md](data/README.md) | popis dát, úmyselných problémov a cvičení |
| [scripts/internal_link_audit.py](scripts/internal_link_audit.py) | lokálny audit odkazov, jedinečných inlinks, hĺbky a problémov |
| [.gitignore](.gitignore) | bežné výstupy a súkromné konfigurácie, ktoré nepatria do Git repozitára |

## 🧩 Čo si v tomto repozitári vyskúšame

| Oblasť | Úloha | Výsledok |
|---|---|---|
| SEO základy | vysvetliť title, meta description, URL, H1–H3 | správne usporiadaný obsah |
| WordPress | vyplniť SEO nastavenia v editore | náhľad titulku a metadát |
| Yoast Premium | posúdiť interné odporúčania | relevantné kontextové odkazy |
| Interné odkazy | vysvetliť inlinks, outlinks, anchor texty | tabuľka odkazových vzťahov |
| Cornerstone | označiť strategický obsah | návrh tematického klastra |
| Orphaned | nájsť nedostatočne prepojené URL | zoznam na manuálne posúdenie |
| Screaming Frog | skontrolovať Crawl Depth | hlbšie umiestnené stránky |
| GSC | analyzovať kliknutia a impressions | vývoj výkonu URL |
| GA4 | rozlíšiť Sessions a Views | správna interpretácia návštev |
| Lokálny audit | spustiť Python nad CSV | opakovateľný SEO report |

## ⚙️ 1. Spustenie lokálneho tréningu

Potrebujeme **Python 3** bez externých balíkov. Skript používa iba štandardnú knižnicu.

**Windows PowerShell:**

```powershell
git clone https://github.com/miroslav-reiter/seo-wordpress-lab.git
cd seo-wordpress-lab
py -3 scripts/internal_link_audit.py --pages data/pages.csv --links data/links.csv
```

**Ubuntu / Kali Linux:**

```bash
git clone https://github.com/miroslav-reiter/seo-wordpress-lab.git
cd seo-wordpress-lab
python3 scripts/internal_link_audit.py --pages data/pages.csv --links data/links.csv
```

Na počítači bez Git môžeme stiahnuť ZIP cez GitHub → **Code → Download ZIP**, rozbaliť ho a spustiť Python z koreňového adresára.

Skript vypíše:

- počet **Inlinks** a **Unique Inlinks** pre každú URL;
- najkratšiu **Crawl Depth** z domovskej stránky v rámci testovacieho modelu;
- URL bez prichádzajúcich odkazov;
- odkazy na neznáme alebo neindexovateľné ciele;
- nevýstižné anchor texty.

### 🔎 Ako čítať výsledok

| Výstup | Význam |
|---|---|
| `Inlinks = 2` | na URL smerujú dva zaznamenané odkazy |
| `Unique inlinks = 1` | oba odkazy prichádzajú z jednej zdrojovej URL |
| `Crawl depth = 3` | URL je dosiahnuteľná v troch odkazových krokoch |
| `Crawl depth = nezistena` | zo štartovacej URL v našom dátovom modeli nevedie cesta |
| Osirelá URL | v testovacom CSV nemá prichádzajúci odkaz |
| Nevýstižný anchor | napríklad „Kliknite sem“ |

**Upozornenie:** Ide o výučbový model. Skutočný crawler môže počítať odkazy a hĺbku odlišne, pričom výsledky závisia od rozpočtu skenu, JavaScriptu, navigácie, presmerovaní a nastavení.

## 🎬 2. Praktické cvičenia vo videu

**1. Interné odkazy:** Prepojíme odborný článok na tematicky súvisiaci produkt alebo kurz vo WordPresse. Vysvetlíme `<a href="...">` a význam anchor textu.

**2. Yoast SEO Premium:** V editore článku otvoríme Internal linking suggestions, vyberieme jeden relevantný návrh a vložíme odkaz.

**3. Text Link Counter:** V zozname článkov pozrieme počet interných odkazov a vysvetlíme rozdiel oproti crawleru.

**4. Cornerstone / Orphaned:** Označíme prioritnú stránku a identifikujeme obsah, ktorý potrebuje prelinkovanie.

**5. Screaming Frog:** V karte Internal vyberieme HTML URL; v spodnom paneli Inlinks/Outlinks posúdime zdroje, ciele a anchor texty.

**6. Crawl Depth:** V Site Structure / Internal vysvetlíme hĺbku a overíme jej limity pri neúplnom skene.

**7. Google Search Console:** Výkonnosť → Výsledky vyhľadávania → Stránky → konkrétna URL. Sledujeme clicks, impressions, CTR a priemernú pozíciu.

**8. Google Analytics 4:** Reports → Acquisition → Traffic acquisition (Sessions) a Reports → Engagement → Pages and screens (Views a engagement).

**9. Audit CSV:** Spustíme `scripts/internal_link_audit.py`. Pozrieme si osirelé URL, nevýstižné anchor texty a odkazy na neindexovateľné stránky.

**10. Návrh opráv:** Zoznam problémov zoradíme podľa dopadu, závažnosti a náročnosti opravy.

## 🧾 Cheat Sheet – základné rozdiely

| Pojem / metrika | Nástroj | Prečo je dôležitý |
|---|---|---|
| Internal linking suggestions | Yoast Premium | návrhy súvisiacich stránok |
| Text Link Counter | Yoast | evidencia interných odkazov |
| Crawl Depth | Screaming Frog | dostupnosť URL od štartovacieho bodu |
| Unique Inlinks | Screaming Frog | počet zdrojových stránok odkazujúcich na URL |
| Sessions | GA4 | počet návštev / relácií |
| Views | GA4 | počet zobrazení stránok |
| Organic clicks | GSC | kliknutia z výsledkov Vyhľadávania Google |
| Impressions | GSC | zobrazenia vo výsledkoch vyhľadávania |
| Interné kliknutie | vlastná GA4 udalosť | presné meranie kliknutia na odkaz v obsahu |

Viac praktických tabuliek nájdeme v [seo-cheatsheet.md](seo-cheatsheet.md).

## 🔒 Bezpečnostné poznámky

- Pri cvičeniach **nepoužívame živú databázu produkčného WordPressu**.
- Nevykonávame hromadné zmeny URL, redirectov, `noindex`, `robots.txt` a canonical bez samostatného overenia.
- Yoast SEO Data Optimization zapisuje interné SEO údaje do databázy; jeho spustenie nenahrádza zálohu ani diagnostiku.
- Bezplatný Screaming Frog má limit **500 URL**. Neúplný crawl nie je úplný SEO audit.
- Rozlišujeme URL prístupnú pre crawlera, indexovateľnú URL a reálne indexovanú URL v Google.
- Žiadna metrika sama nedokazuje príčinný účinok interného prelinkovania.
- Klientske dáta, autentifikačné tokeny ani exporty obsahujúce osobné údaje necommitujeme do verejného repozitára.

## 📚 Užitočné odkazy a dokumentácia

- Google Search Central: https://developers.google.com/search/docs
- Google – Links best practices: https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- WordPress Developer Resources: https://developer.wordpress.org/
- WooCommerce Documentation: https://woocommerce.com/documentation/
- Yoast SEO: https://yoast.com/wordpress/plugins/seo/
- Yoast – Internal linking tool: https://yoast.com/help/how-to-use-the-yoast-seo-internal-linking-tool/
- Yoast – Orphaned content workout: https://yoast.com/help/how-to-use-the-yoast-seo-premium-orphaned-content-workout/
- Screaming Frog SEO Spider: https://www.screamingfrog.co.uk/seo-spider/
- Google Search Console: https://search.google.com/search-console/about
- Google Analytics: https://analytics.google.com/
- VITA Academy: https://www.vita.sk/

**Účel repozitára:** Praktické osvojenie SEO a WordPress postupov od správneho prelinkovania až po audit a vyhodnotenie výsledkov.