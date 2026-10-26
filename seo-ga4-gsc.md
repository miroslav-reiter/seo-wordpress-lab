# 📊 Meranie SEO: Google Analytics 4 a Google Search Console

Tento dokument presne odlišuje **návštevy**, **zobrazenia stránok**, **kliknutia z vyhľadávania**, **zobrazenia vo vyhľadávaní**, **zapojenie** a **kliknutia na interné odkazy**. Pre interné prelinkovanie potrebujeme vedieť, čo každý údaj skutočne meria.

## 🧭 Kde nájdeme metriky v GA4

| Potrebujeme | Cesta v rozhraní GA4 | Metrika |
|---|---|---|
| návštevy podľa zdroja | Reports → Acquisition → Traffic acquisition | `Sessions` |
| zapojené návštevy | Reports → Acquisition → Traffic acquisition | `Engaged sessions` |
| miera zapojenia | Reports → Acquisition → Traffic acquisition | `Engagement rate` |
| návštevnosť konkrétnych stránok | Reports → Engagement → Pages and screens | `Views` |
| zapojenie na konkrétnych stránkach | Reports → Engagement → Pages and screens | `Average engagement time per active user` |
| prvé stránky v relácii | Reports → Engagement → Landing page | výkon vstupných stránok |
| cesta medzi stránkami | Explore → Path exploration | následnosť udalostí alebo návštev stránok |

**Dôležité:** `Views` nie sú `Sessions`. Jedna relácia môže obsahovať viac zobrazení stránky. `Engagement overview` nemusí zobrazovať celkový počet návštev v hlavnej karte. Viditeľnosť reportov závisí aj od konfigurácie navigácie property.

### **1. GA4 – počet návštev z organického vyhľadávania**

1. Otvoríme **Reports → Acquisition → Traffic acquisition**.
2. Nastavíme obdobie a dimenziu, napríklad **Session source / medium**.
3. Zobrazíme `google / organic` alebo kanál `Organic Search`.
4. Vyhodnotíme `Sessions` a `Engaged sessions`.

**Čo to robí:** Ukazuje relácie podľa zdroja návštevnosti. Nerozlišuje automaticky kliknutia na konkrétne interné odkazy.

### **2. GA4 – návštevnosť vybranej URL**

1. Otvoríme **Reports → Engagement → Pages and screens**.
2. Zvolíme vhodnú dimenziu stránky, ideálne cestu URL podľa dostupných možností.
3. Vyhľadáme konkrétnu URL alebo slug.
4. Skontrolujeme `Views`, `Active users` a `Average engagement time`.

**Pozor:** Ide o výkon stránky, nie o presný počet kliknutí z iného článku.

### **3. GA4 – prechod používateľov medzi stránkami**

**Explore → Path exploration** umožní zistiť, aké stránky alebo udalosti nasledovali po vybranej stránke. **Nie je dôkazom konkrétneho kliknutia na odkaz**; môže ísť aj o iný typ navigácie.

Na presné meranie kliknutí na interné odkazy potrebujeme definovať a implementovať vlastnú udalosť (napr. cez Google Tag Manager), s parametrami ako `source_path`, `link_url` a `link_text`. V produkcii zavedenie merania koordinujeme s pravidlami súhlasu, ochranou údajov a testovaním duplicít.

## 🔍 Kde nájdeme organické kliknutia a zobrazenia v GSC

**Google Search Console → Výkonnosť → Výsledky vyhľadávania → Úplný prehľad**

| Metrika | Význam |
|---|---|
| Celkový počet kliknutí | kliknutia z výsledkov Vyhľadávania Google |
| Celkový počet zobrazení | koľkokrát sa výsledok zobrazil podľa metodiky Google |
| Priemerná miera preklikov / CTR | kliknutia ÷ zobrazenia |
| Priemerná pozícia | priemerná pozícia vo výsledkoch Google |

### **4. GSC – výkon konkrétnej stránky**

1. Otvoríme **Výsledky vyhľadávania**.
2. Zapneme kliknutia a zobrazenia.
3. Pod grafom vyberieme kartu **Stránky**.
4. Klikneme na konkrétnu URL alebo pridáme filter stránky.
5. Nastavíme časové obdobie a prípadne **Porovnať**.

**Čo to robí:** Sledujeme vývoj organickej viditeľnosti URL a potenciálne zmeny po doplnení interných odkazov. Neznamená to však automaticky príčinný účinok prelinkovania.

### **5. GSC – čo nie je k dispozícii**

Google Search Console neukazuje počet kliknutí na interný odkaz **v rámci webu**. GSC zobrazuje výkon vo Vyhľadávaní Google. Na kliknutia v obsahu potrebujeme iné meranie.

## 📈 Pred/po audit interného prelinkovania

| Krok | Výsledok |
|---|---|
| 1. Vyberieme URL | cieľová produktová alebo článková stránka |
| 2. Zaznamenáme pôvodný stav | počet a zdroje inlinks, crawl depth, meta, indexability |
| 3. Zapíšeme dátum zásahu | napr. pridanie 3 kontextových odkazov |
| 4. Nastavíme porovnateľné obdobia | napr. 28 dní pred a 28 dní po |
| 5. GSC | kliknutia, zobrazenia, CTR, priemerná pozícia |
| 6. GA4 | sessions podľa zdroja, views a engagement cieľových stránok |
| 7. Interpretácia | sezónnosť, ďalšie zmeny, indexácia, časové oneskorenia |

### **6. Praktická ukážka hodnotenia**

V testovacom príklade predpokladáme, že článok A novo odkazuje na produkt B. Po zásahu zistíme viac views produktu B, no zároveň prebiehala reklama. **Nemôžeme tvrdiť, že rast spôsobilo iba interné prelinkovanie.**

Ideálne:
- Použijeme porovnateľné obdobie a rovnaké filtre.
- Zaznamenáme všetky súbežné zmeny.
- Zohľadníme, že zdroje GA4 a GSC používajú odlišné metódy merania.
- Pri hodnotení konkrétnych odkazov využijeme vlastné interné klikacie udalosti.

## 🧾 Cheat Sheet metrík

| Metrika | Zdroj | Čo neznamená |
|---|---|---|
| Sessions | GA4 | nie je to počet zobrazení stránky |
| Views | GA4 | nie je to počet relácií |
| Engaged sessions | GA4 | nie sú všetky relácie |
| Clicks | GSC | nie sú interné kliknutia |
| Impressions | GSC | nie sú zobrazenia stránok na webe |
| CTR | GSC | nie je miera konverzie |
| Crawl Depth | crawler | nie je priemerná pozícia v Google |
| Inlinks | crawler / Yoast | nie je zaručený SEO prínos |

## 📚 Zdroje

- https://support.google.com/analytics/answer/12926732
- https://support.google.com/webmasters/answer/17010961
- https://support.google.com/webmasters/answer/17011165
- https://support.google.com/webmasters/answer/7042828
