# 🐸 SEO audit a interné odkazy v Screaming Frog SEO Spider

Praktická príručka na **Crawl Depth, Inlinks, Outlinks, anchor texty, indexovateľnosť, presmerovania a osirelé stránky**. Postupy sa vzťahujú na bežné rozhranie SEO Spider, názvy kariet sa môžu podľa verzie meniť.

## 📌 Čo je SEO crawler

SEO crawler systematicky prechádza web podobne ako robot vyhľadávača, zbiera URL a ich technické vlastnosti. Výsledky sú **stavom konkrétneho skenu**, nie absolútnou pravdou o všetkých stránkach webu.

### Základné prvky rozhrania

| Miesto | Čo tam nájdeme |
|---|---|
| Adresný riadok hore | štartovaciu URL, napr. `https://www.vita.sk/` |
| Tlačidlo Start | spustenie crawlera |
| Internal | interné URL s technickými metrikami |
| Filter HTML | iba HTML dokumenty (bez obrázkov, JS a CSS) |
| Hlavná tabuľka | adresy, status, indexovateľnosť a ďalšie stĺpce |
| Spodný panel Inlinks | odkazy smerujúce na vybranú URL |
| Spodný panel Outlinks | odkazy vedúce z vybranej URL |
| Pravá záložka Site Structure | distribúcia štruktúry a hĺbky preklikov |
| Crawl Analysis | doplnkové výpočty a filtre podľa verzie |

## 🧭 Hĺbka preklikov: Crawl Depth

`Crawl Depth` udáva minimálny počet odkazových prechodov od štartovacieho bodu crawlera k URL v rámci jeho modelu. Presmerovania sa môžu počítať ako ďalší krok. Je to hodnota citlivá na nastavenie crawlera, začiatok skenu a rozsah povolených URL.

| Crawl Depth | Význam v typickom skene z homepage |
|---|---|
| 0 | štartovacia URL |
| 1 | stránka dostupná jedným prechodom |
| 2 | dva prechody |
| 3 | tri prechody |
| 4 a viac | hlbšie umiestnený obsah, ktorý preveríme |

### **1. Kde hĺbku nájdeme**

1. Spustíme crawl vlastnej alebo testovacej lokality.
2. Otvoríme záložku **Internal** alebo **Links**.
3. V hlavnej tabuľke nájdeme stĺpec **Crawl Depth** (môže byť ďalej vpravo).
4. Zoradíme zostupne a vyberieme hlboké dôležité stránky.
5. Vpravo **Site Structure** zobrazíme rozdelenie hĺbky.

**Odporúčanie:** Pre dôležité stránky sa často usilujeme o nízku hĺbku (napríklad 1–3), no nejde o striktné pravidlo Googlu.

### **2. Filter Pages With High Crawl Depth**

Ak ho daná verzia ponúka, zapneme **Crawl Analysis → Configure → Links**, následne **Crawl Analysis → Start**. Potom v **Links** vyberieme **Pages With High Crawl Depth**. Bez doplnkovej analýzy môže byť tento filter prázdny.

## 🔗 Počítanie interných odkazov

| Stĺpec | Význam |
|---|---|
| Inlinks | všetky odkazy smerujúce na vybranú URL, aj viacero z jednej stránky |
| Unique Inlinks | počet odlišných zdrojových URL, ktoré na vybranú URL odkazujú |
| Outlinks | odkazy smerujúce z vybranej URL |
| Unique Outlinks | počet jedinečných cieľových URL |
| Indexability | informácia, či je URL podľa crawlera indexovateľná |
| Status Code | HTTP odpoveď (200, 301, 404 atď.) |
| Crawl Depth | hĺbka od počiatočnej stránky |

### **3. Kde konkrétne nájdeme odkazy na URL**

1. **Internal → HTML**.
2. Klikneme na analyzovanú URL.
3. V **spodnom paneli Inlinks** sledujeme zdroje odkazov.
4. Skontrolujeme `From`, `To`, `Anchor Text`, prípadne `Follow`.
5. V **Outlinks** vidíme odkazy smerujúce z tejto stránky.

### **4. Čo znamená relevantnosť**

Crawler nám poskytuje dáta, napríklad názvy zdrojových stránok a anchor texty. **Tematickú vhodnosť** posudzujeme aj manuálne:
- Má zdrojová stránka rovnakú alebo doplňujúcu tému?
- Odpovedá anchor text cieľovému obsahu?
- Je odkaz vhodne umiestnený v kontexte?
- Je cieľ používateľsky hodnotný, dostupný a aktuálny?

**Počet odkazov ≠ automaticky SEO kvalita.**

## 🚦 Kontrola odpovedí a indexovateľnosti

| HTTP kód / stav | Čo overíme |
|---|---|
| 200 | stránka je dostupná; ďalej overíme indexovateľnosť |
| 301/308 | trvalé presmerovanie, kontrola koncového cieľa |
| 302/307 | dočasné presmerovanie a jeho vhodnosť |
| 404 | neexistujúca URL; opravíme odkazy alebo zvolíme vhodný zásah |
| 410 | úmyselné odstránenie |
| 5xx | serverové chyby |
| Noindex | overíme, či je zámerné |
| Canonical na inú URL | overíme, či zodpovedá obsahu a stratégii |

## 🕸️ Osirelé stránky

Crawler štartujúci iba z domovskej stránky nemusí vôbec objaviť osirelé URL. Na vyhodnotenie potrebujeme porovnať aj externé zoznamy URL, napríklad XML sitemap alebo exporty GSC/GA4 (podľa dostupných možností a licencie).

**Nezamieňame:** „0 Inlinks v neúplnom crawle“ nemusí znamenať „skutočne osirelá stránka“.

## 💡 Ukážková analýza webu VITA.sk

Pri výučbe môžeme zadať `https://www.vita.sk/` a demonštrovať rozhranie, ale nechávame dbať na limity. **Bezplatná verzia Screaming Frog má limit 500 URL**, takže výsledok nemusí reprezentovať celý rozsiahly web.

Ak crawler nájde 500 URL, analýzu považujeme za **čiastkovú**. Najmä pri stovkách produktov, článkov a médií nemožno automaticky vyhlasovať, ktoré dôležité stránky nemajú interné odkazy.

Pre úplne reprodukovateľné cvičenie použijeme `data/pages.csv`, `data/links.csv` a skript `scripts/internal_link_audit.py`.

## 🧪 Praktický checklist auditu

- [ ] Overili sme správnu štartovaciu URL a protokol HTTPS
- [ ] Nepomýlili sme HTML s obrázkami a JS/CSS
- [ ] Vieme, či crawl dosiahol limit 500 URL
- [ ] Skontrolovali sme `Crawl Depth` dôležitých stránok
- [ ] Pozreli sme `Unique Inlinks` a nie iba celkový počet
- [ ] Skontrolovali sme anchor text a typy odkazov v spodnej záložke
- [ ] Identifikovali sme nefunkčné a presmerované cieľové URL
- [ ] Overili sme Indexability, noindex a canonical
- [ ] Zaznamenali sme odporúčania a mieru istoty nálezov

## 📚 Zdroje

- https://www.screamingfrog.co.uk/seo-spider/tutorials/internal-linking-audit-with-the-seo-spider/
- https://www.screamingfrog.co.uk/seo-spider/
- https://developers.google.com/search/docs/crawling-indexing/links-crawlable
