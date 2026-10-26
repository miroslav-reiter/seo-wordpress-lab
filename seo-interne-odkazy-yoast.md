# 🔗 SEO interné odkazy a prelinkovanie vo WordPress a Yoast SEO

Praktický návod pre SEO konzultantov, správcov webu, WordPress používateľov, WooCommerce administrátorov a vývojárov.

## 📌 Základné pojmy

Interný odkaz prepája URL v rámci jedného webu. Interné prelinkovanie je stratégia, ktorou vytvárame prehľadné cesty medzi dôležitými stránkami, kategóriami, článkami a produktmi. Podporuje objavovanie obsahu, používateľskú navigáciu a tematické súvislosti, ale **nezaručuje indexáciu ani nárast pozícií**.

~~~html
<a href="/online-kurzy-linux-unix/">Online kurzy Linux a Unix</a>
~~~

| Prvok | Význam |
|---|---|
| `<a>` | HTML element odkazu |
| `href` | cieľová URL |
| Anchor text | viditeľný text odkazu |
| Inlink | odkaz smerujúci **na** vybranú URL |
| Outlink | odkaz vedúci **z** vybranej URL |
| Unique inlinks | odkazy počítané po jedinečných zdrojových stránkach |
| Crawl depth | minimálny počet kliknutí/prechodov potrebný na dosiahnutie URL z počiatočnej stránky pri danom crawle |

## 🧭 Typy interných odkazov

| Typ | Príklad | Funkcia |
|---|---|---|
| Navigačný | hlavné menu → kurzy | základná orientácia |
| Kontextový | článok Linux → kurz Linux | obsahová súvislosť |
| Hierarchický | kategória → podkategória | štruktúra |
| Breadcrumb | domov → kategória → produkt | navigácia späť |
| Súvisiaci obsah | článok → ďalší odborný návod | pokračovanie témy |
| Produktový | kategória → produkt | nákupná cesta |
| Pätička | dôležité stránky webu | globálna dostupnosť |

## 🧩 Stratégia: Topic Cluster a Cornerstone

Pri tematickom prelinkovaní vyberieme nosnú stránku a niekoľko kvalitných podporných článkov. Odkazy vytvárame podľa kontextu, nie podľa pevne stanoveného počtu.

**Príklad tematického klastra (navrhovaná štruktúra):**

~~~text
VITA.sk
├── Kategória: Online kurzy Linux
│   ├── Kurz Linux/Unix I. Začiatočník
│   └── Kurz Linux Administrátor
└── Blog: Linux príkazy pre administráciu
    ├── Kontextový odkaz → Linux/Unix I.
    └── Kontextový odkaz → Linux Administrátor
~~~

Rozlišujeme stránky, ktoré sú nosnou témou (cornerstone), od článkov, ktoré ich vysvetľujú alebo rozširujú. Nič nemusíme meniť v produkcii, aby sme tento návrh vedeli učiť na tabuľke odkazov v `data/links.csv`.

## 🎬 Yoast SEO Premium – presný praktický postup

### **1. Otvorenie odporúčaní interných odkazov**

1. V administrácii WordPress otvoríme konkrétny článok alebo stránku.
2. Otvoríme panel **Yoast SEO Premium → Internal linking suggestions**.
3. Pozrieme sa na odporúčané stránky, články a prípadne kategórie či značky.
4. Tematicky relevantný odkaz skopírujeme ikonou pri názve.
5. V texte vyberieme výstižný anchor text a doplníme URL.
6. Uložíme a overíme fungovanie odkazu na verejnej stránke.

**Čo to robí:** Yoast poskytuje výber súvisiaceho obsahu, odkazy nevkladá automaticky podľa relevancie bez našej kontroly.

### **2. Zapnutie funkcie odporúčaní**

V novších verziách spravidla: **Yoast SEO → Settings → Site features → Site structure → Internal linking suggestions**. Dostupnosť závisí od Premium licencie, aktivácie a verzie.

### **3. Text Link Counter**

**Yoast SEO → Settings → Site features → Site structure → Text link counter**, následne **Články → Všetky články**. Overíme stĺpce pre odkazy smerujúce z článku a na článok.

**Pozor:** Počty Yoastu sa môžu líšiť od externého crawlera, keďže nástroje môžu uplatňovať odlišnú metodiku.

### **4. Cornerstone Content**

V editore označíme kľúčovú stránku ako **Cornerstone content**, následne na ňu vedome prepojíme obsah, ktorý ju tematicky podporuje.

### **5. Orphaned Content Workout**

**Yoast SEO Premium → Workouts → Orphaned content**. Vyhodnotíme, ktoré stránky potrebujeme aktualizovať a prepojiť. Tento postup môže vyžadovať predchádzajúcu optimalizáciu SEO dát.

**Pozor na Remove / Hide from search engines:** Odstránenie alebo noindex nie sú „optimalizácia odkazov“. V tréningu pracujeme iba na kópii alebo používame bezpečný režim čítania.

### **6. SEO Data Optimization – Indexables**

**Yoast SEO → Tools → SEO data optimization** spracúva interné SEO dáta (indexables). Môže aktualizovať záznamy v databáze; jeho primárnym účelom nie je prepísať články či automaticky doplniť odkazy.

Na rozsiahlejšom produkčnom WordPresse môžu databázové procesy zaťažiť server. Na školení vysvetlíme túto funkciu bez opakovaného spúšťania na produkcii.

### **7. Taxonomy sync problem a neúspešný prepočet**

Hlásenie samo o sebe neurčuje presnú príčinu. Overíme:
- podrobný text chyby a HTTP kód,
- dostupnosť a autentifikáciu WordPress REST API,
- pravidlá WAF a cache,
- serverové chyby a časové limity,
- kompatibilitu Yoast SEO, WordPressu a ďalších pluginov.

**401/403** môže znamenať blokovanie požiadaviek, **301/302** nechcené presmerovanie API a **5xx** chybu alebo timeout servera.

## 🧪 Príklady relevancie

| Zdrojový článok | Odporúčaný cieľ | Hodnotenie |
|---|---|---|
| Linux administrácia | kurz Linux Administrátor | spravidla relevantné |
| Linux administrácia | FAQ – vrátenie peňazí | zvyčajne nerelevantné |
| SMTP server | odborný článok o SMTP | relevantné |
| Predplatné VITA | FAQ – prihlásenie k predplatnému | relevantné |
| WordPress SEO | návod na Yoast a interné odkazy | relevantné |
| WordPress SEO | nesúvisiaci kurz grafiky | bez jasného kontextu nevhodné |

**Päť návrhov Yoastu neznamená päť povinných odkazov.**

## 🧾 Anchor text – dobré a slabé príklady

| Slabý anchor text | Lepší anchor text |
|---|---|
| Kliknite sem | Online kurz Linux Administrátor |
| Viac informácií | Návod na WordPress SEO |
| Naša ponuka | Online kurzy administrácie Linuxu |
| Pozrite si tento článok | Práca s Google Search Console |
| Čítať viac | Ako používať Yoast SEO Premium |

Anchor text má byť výstižný, primerane krátky a prirodzený. Nepotrebujeme ho napĺňať identickou kľúčovou frázou v každom odkaze.

## 🔍 Čo skontrolujeme po vložení odkazu

| Kontrola | Očakávaný výsledok |
|---|---|
| Cieľová URL | zmysluplná, aktuálna, dostupná |
| HTTP stav | spravidla 200 alebo odôvodnené presmerovanie |
| Anchor text | odpovedá obsahu |
| Kontext | odkaz dopĺňa okolný text |
| HTML | `<a href="...">`, nie iba `onclick` |
| Indexácia cieľa | cieľ nemá neúmyselné noindex |
| Duplicity | nepridávame zbytočné opakovania |
| Meranie | zaznamenáme dátum zásahu a cieľovú URL |

## 📚 Oficiálne zdroje

- https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- https://yoast.com/help/how-to-use-the-yoast-seo-internal-linking-tool/
- https://yoast.com/help/how-to-use-the-yoast-seo-premium-orphaned-content-workout/
- https://yoast.com/help/yoast-seo-settings-site-features/
- https://yoast.com/help/we-couldnt-complete-the-optimization-of-your-seo-data/
