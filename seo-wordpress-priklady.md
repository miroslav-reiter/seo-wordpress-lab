# 🧪 Praktické príklady SEO a WordPress

Zbierka pracovných postupov pre WordPress, WooCommerce, Yoast SEO (Free/Premium), SEO konzultantov, marketérov a webových vývojárov. Na trénovanie používame **testovací WordPress alebo pripravené ukážkové údaje**, nie produkčný web.

## 🧠 Ako pracovať s príkladmi

Každý príklad obsahuje cieľ, postup, očakávaný výsledok a vysvetlenie. Položky menu môžu byť lokalizované alebo sa líšiť podľa verzie pluginu. Po každom cvičení vieme vyhodnotiť, či sa zmenila iba metadátová konfigurácia, alebo aj HTML verejnej stránky.

| Výraz | Význam |
|---|---|
| SEO title | názov zobrazovaný ako titulok vo výsledkoch vyhľadávania, ak ho Google použije |
| Meta description | navrhnutý úryvok výsledku; Google môže zobraziť iný text |
| Focus keyphrase | pomôcka na obsahovú analýzu v Yoast; nie je to priamy signál odoslaný Googlu |
| Slug | koncová časť URL, napríklad `online-kurz-linux` |
| Canonical | preferovaná URL pri viacerých podobných adresách |
| Indexables | interné databázové záznamy Yoastu na optimalizáciu práce s SEO dátami |
| Anchor text | viditeľný text odkazu |
| Cornerstone | dôležitá nosná stránka obsahu |
| Orphaned content | obsah bez dostatočných prichádzajúcich odkazov podľa metodiky nástroja |

## 📝 On-page SEO a obsah

### **1. Nastavenie SEO title a meta description**

**Cieľ:** Optimalizovať zobrazenie článku vo výsledkoch vyhľadávania.

**Postup:** V testovacom WordPresse otvoríme článok → panel Yoast SEO → ukážka vo výsledkoch vyhľadávania / SEO title / Meta description. Zadáme vlastný výstižný názov a opis.

**Vzor:**

- SEO title: `WordPress SEO: Interné odkazy a prelinkovanie | VITA`
- Meta description: `Naučte sa vytvárať interné odkazy vo WordPresse, pracovať s Yoast SEO a kontrolovať ich v SEO crawleri.`

**Čo to robí:** Poskytuje Googlu kandidátov na titulok a úryvok. Nie je zaručené, že Google použije presne tieto texty.

**Overenie:** Otvoríme zdrojový HTML kód a vyhľadáme `<title>` a `<meta name="description">`.

### **2. Nastavenie hlavnej kľúčovej frázy vo Yoaste**

**Cieľ:** Pracovať s kontrolným zoznamom SEO analýzy.

**Postup:** V Yoaste zadáme `interné odkazy wordpress` ako hlavnú kľúčovú frázu, prečítame odporúčania a upravíme obsah tam, kde to má význam.

**Čo to robí:** Yoast vyhodnocuje text, nie skutočné pozície vo vyhľadávaní.

**Vysvetlenie:** Zelené hodnotenie nezaručuje dobré umiestnenie v Google. Optimalizujeme pre používateľský zámer a faktickú správnosť.

### **3. Správna štruktúra H1–H3**

**Cieľ:** Vytvoriť logickú štruktúru článku.

**Príklad:**

~~~html
<h1>SEO a interné prelinkovanie</h1>
<h2>Čo je interný odkaz</h2>
<h3>Anchor text a cieľová URL</h3>
<h2>Praktický postup vo WordPresse</h2>
~~~

**Čo to robí:** Pomáha organizovať obsah a navigáciu.

**Overenie:** V editore WordPress použijeme bloky Nadpis a následne skontrolujeme skutočné HTML.

### **4. Obrázky: Alt text, názov a veľkosť**

**Cieľ:** Zlepšiť prístupnosť a opis obrazového obsahu.

**Postup:** V Knižnici médií pridáme výstižný alternatívny text a zvolíme vhodnú veľkosť obrázka.

~~~html
<img src="wordpress-seo.webp"
     alt="Panel Yoast SEO pri úprave interného odkazu"
     width="960" height="540">
~~~

**Vysvetlenie:** Alt text opisuje význam obrázka, nie zoznam kľúčových slov. Dekoratívne obrázky môžu mať prázdne alt.

### **5. Interný odkaz s opisným anchor textom**

**Cieľ:** Prepojiť súvisiaci článok a produkt alebo návod.

~~~html
<a href="/online-kurz-linux-unix-i-zaciatocnik/">
  Online kurz Linux/Unix I. Začiatočník
</a>
~~~

**Postup:** Označíme text v editore, vložíme existujúcu URL a skontrolujeme fungovanie odkazu. Pri verejných príkladoch na VITA.sk URL najprv overíme.

**Vysvetlenie:** Odkaz má mať skutočný atribút `href`. Nevytvárame odkazy iba JavaScriptovým `onclick`.

### **6. Rozlíšenie interného a externého odkazu**

~~~html
<a href="/blog/seo/">Interný článok o SEO</a>
<a href="https://developers.google.com/search">Dokumentácia Google</a>
~~~

**Čo to robí:** Prvý odkaz smeruje v rámci tej istej webovej domény, druhý na externý zdroj. Ani jeden nepotrebuje automaticky `rel="nofollow"`.

### **7. Úprava a kontrola URL slug**

**Postup:** V testovacom článku skontrolujeme permalink a vyberieme krátky stabilný slug bez zbytočných parametrov.

**Pozor:** Na produkčnom webe zmena existujúcej URL môže vytvoriť chybu 404. Ak zmenu skutočne vykonáme, potrebujeme skontrolovať interné odkazy, canonical a vhodné presmerovanie.

## 🔗 Interné prelinkovanie a Yoast

### **8. Yoast Premium – Internal linking suggestions**

**Postup:** WordPress → článok alebo stránka → panel Yoast SEO → Internal linking suggestions. Prečítame návrhy, vyberieme tematicky vhodnú URL, skopírujeme ju ikonou a doplníme kontextový odkaz.

**Čo to robí:** Pomáha identifikovať obsahovo príbuzné stránky. Odporúčanie nie je automatický príkaz vložiť všetky ponúkané odkazy.

**Overenie:** Uložíme stránku a preklikneme sa na cieľovú adresu.

### **9. Yoast Text Link Counter**

**Postup:** WordPress → Články → Všetky články; zobrazíme stĺpce odkazov Yoast SEO. Ak nie sú dostupné, preveríme Yoast SEO → Nastavenia → Funkcie webu → Štruktúra webu → Text link counter.

**Čo to robí:** Počíta interné odkazy v podporovanom obsahu podľa pravidiel pluginu.

**Vysvetlenie:** Výsledok nemusí byť totožný s externým crawlerom, ktorý môže započítavať aj navigáciu, pätičku a ďalšie odkazy.

### **10. Cornerstone Content**

**Cieľ:** Označiť prioritný odborný článok alebo stránku.

**Postup:** V editore označíme nosný článok ako Cornerstone Content a prepojíme ho s relevantnými podpornými článkami.

**Čo to robí:** Pomáha riadiť obsahovú stratégiu a identifikovať dôležité stránky.

### **11. Orphaned Content Workout**

**Postup:** Yoast SEO Premium → Workouts → Orphaned Content. Identifikujeme články s nedostatočnou podporou a vyberieme tie, ktoré chceme zachovať a doplniť odkazy.

**Pozor:** Možnosti odstránenia a `Hide from search engines` môžu mať trvalý vplyv na dostupnosť a indexáciu. Na videu ich iba vysvetľujeme; bez rozhodnutia ich nepoužívame.

### **12. SEO Data Optimization a indexables**

**Postup:** Yoast SEO → Tools → SEO data optimization. Vysvetlíme význam indexables, sledovanie priebehu a chybové hlásenia.

**Vysvetlenie:** Ide o databázové operácie, nie o automatické pridávanie interných odkazov do článkov. Na veľkom produkčnom webe môže proces zaťažiť server; nespúšťame ho iba kvôli ukážke.

### **13. Diagnostika hlásenia Taxonomy sync problem**

**Postup:** Prečítame podrobnosti chyby; skontrolujeme REST API, HTTP stavové kódy, serverové logy a kompatibilitu pluginov. Dôvod neurčujeme len podľa jedného riadka „Taxonomy sync problem“.

**Vysvetlenie:** Príčiny môžu zahŕňať blokovanie API, 401/403, presmerovanie alebo serverové chyby, no konkrétnu príčinu treba diagnostikovať.

## 🛒 WooCommerce, technické SEO a indexácia

### **14. Interné odkazy medzi kategóriami a produktmi**

**Postup:** Na testovacej kategórii WooCommerce pridáme prehľadný odkaz na podkategóriu a na súvisiaci produkt. Overíme, že anchor text odráža obsah cieľovej stránky.

**Cieľ:** Zlepšiť navigáciu a prístupnosť dôležitých produktov.

### **15. Canonical a duplicitné URL**

**Postup:** Na testovacej stránke skontrolujeme kanonickú URL vytvorenú SEO pluginom.

~~~html
<link rel="canonical" href="https://example.com/kurzy/wordpress-seo/">
~~~

**Vysvetlenie:** Canonical je signál o preferovanej URL, nie náhrada za presmerovanie alebo opravu interných odkazov.

### **16. XML sitemap**

**Postup:** Otvoríme sitemap generovanú WordPressom/Yoastom, overíme dostupnosť a skontrolujeme, či obsahuje dôležité indexovateľné URL.

**Vysvetlenie:** Prítomnosť v sitemap sama osebe nezaručuje indexáciu.

### **17. Kontrola indexovateľnosti a robots.txt**

**Postup:** V testovacej inštalácii porovnáme nastavenia indexovania, `robots.txt` a meta robots.

**Vysvetlenie:** Blokovanie crawl cez robots.txt nie je to isté ako `noindex`. Nepridávame zákaz indexácie na živý web bez overenia dôsledkov.

### **18. Kontrola presmerovaní a HTTP odpovedí**

**Windows PowerShell:**
~~~powershell
curl.exe -I -L https://example.com/
~~~

**Ubuntu a Kali Linux:**
~~~bash
curl -I -L https://example.com/
~~~

**Čo to robí:** Skontrolujeme HTTP hlavičky a presmerovania. `-I` žiada iba hlavičky, `-L` sleduje presmerovania; pri niektorých serveroch sa odpoveď na HEAD môže líšiť od GET.

### **19. Štruktúrované dáta**

**Postup:** Skontrolujeme výsledný JSON-LD a otestujeme URL cez Rich Results Test.

**Vysvetlenie:** Platná schéma ešte nezaručuje zobrazenie rich results. Plugin môže vytvárať viac vzájomne súvisiacich entít.

### **20. Audit a prioritizácia oprav**

**Cieľ:** Vytvoriť zoznam problémov s prioritami.

| Priorita | Nález | Akcia |
|---|---|---|
| P1 | Dôležitá stránka 404 | opraviť interný odkaz alebo vhodne presmerovať |
| P1 | Omylom noindex na prioritnej stránke | preveriť zámer, opraviť nastavenie |
| P2 | Dôležitá stránka bez relevantných inlinks | doplniť kontextové odkazy |
| P2 | Nevýstižný anchor text | zlepšiť text odkazu |
| P3 | Názov a meta opis bez jasnej hodnoty | zlepšiť podľa obsahu a vyhľadávacieho zámeru |

## 📚 Odporúčané zdroje

- [Google – Link best practices](https://developers.google.com/search/docs/crawling-indexing/links-crawlable)
- [Google – Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview)
- [Yoast – Internal linking tool](https://yoast.com/help/how-to-use-the-yoast-seo-internal-linking-tool/)
- [Yoast – Site features](https://yoast.com/help/yoast-seo-settings-site-features/)
- [Yoast – Orphaned content workout](https://yoast.com/help/how-to-use-the-yoast-seo-premium-orphaned-content-workout/)
