# Optimalizácia produktov a kurzov s Yoast SEO a AI

**Praktický sprievodca pre WordPress a WooCommerce**

Optimalizáciu produktov a kurzov s Yoast SEO a AI postavíme na konkrétnom pracovnom postupe: analyzujeme produkt → vyberieme kľúčovú frázu → pripravíme obsah pomocou AI → vyplníme Yoast SEO → overíme výsledok → vyhodnotíme výkon.

## Obsah

- **[1. Cieľ a výsledok optimalizácie](#cast-1)**
- **[2. Komu je návod určený](#cast-2)**
- **[3. Pracovný postup krok za krokom](#cast-3)**
- **[4. Rozdiel medzi jednotlivými nástrojmi](#cast-4)**
- **[5. Podklady pred optimalizáciou](#cast-5)**
- **[6. Praktický postup v administrácii](#cast-6)**
- **[7. Výber kľúčovej frázy a synoným](#cast-7)**
- **[8. Príklady optimalizácie štyroch kurzov VITA](#cast-8)**
- **[9. Ako pracujeme so zeleným hodnotením Yoastu](#cast-9)**
- **[10. Univerzálny AI prompt pre akýkoľvek produkt](#cast-10)**
- **[11. Konkrétne AI prompty pre štyri kurzy](#cast-11)**
- **[12. Opravný prompt podľa skutočných upozornení Yoastu](#cast-12)**
- **[13. Kontrolný prompt pred publikovaním](#cast-13)**
- **[14. Technická časť pre správcov a vývojárov](#cast-14)**
- **[15. Kontrola publikovanej stránky a meranie výsledkov](#cast-15)**
- **[Zdroje a referenčné stránky](#zdroje)**

<a id="cast-1"></a>

## 1. Cieľ a výsledok optimalizácie

Cieľom je pripraviť produktovú stránku, ktorá jasne vysvetľuje ponuku, zodpovedá vyhľadávaciemu zámeru zákazníka a obsahuje správne SEO údaje. Postup zahŕňa výber kľúčovej frázy, úpravu produktového textu, nastavenie SEO názvu a meta popisu, kontrolu obrázkov a vyhodnotenie odporúčaní Yoastu.

Výsledkom je upravená stránka vo WooCommerce, overený obsah a záznam zmien na následné meranie výkonu. AI používame na prípravu návrhov z doložených údajov. Za správnosť informácií a finálne rozhodnutia zodpovedáme my.

<a id="cast-2"></a>

## 2. Komu je návod určený

| Cieľová skupina | Prínos návodu |
|---|---|
| SEO konzultanti | Opakovateľný postup auditu a návrhu úprav produktových stránok |
| Produktoví manažéri | Prepojenie vlastností produktu, potrieb zákazníka a obsahu stránky |
| Produktoví marketéri | Tvorbu hodnotovej ponuky, benefitov a textov pre vyhľadávanie |
| Produktoví špecialisti | Premenu produktových údajov na presné a zrozumiteľné popisy |
| SEO špecialisti | Prácu s kľúčovými frázami, metadátami a odporúčaniami Yoastu |
| Správcovia webu | Kontrolu nastavení, indexovateľnosti a výslednej stránky |
| WordPress používatelia | Praktickú orientáciu v editore produktu a paneli Yoast SEO |
| Správcovia e-shopov | Systematickú optimalizáciu katalógu a kontrolu produktových údajov |
| Weboví vývojári a web developeri | Kontrolu HTML výstupu, štruktúrovaných dát a integrácie šablóny |

<a id="cast-3"></a>

## 3. Pracovný postup krok za krokom

| Krok | Čo urobíme | Výsledok |
|---|---|---|
| 1 | Zaznamenáme pôvodný obsah, SEO polia a dostupné metriky | Východiskový stav na porovnanie |
| 2 | Overíme vlastnosti produktu, cieľovú skupinu a podmienky | Spoľahlivé podklady pre text a AI |
| 3 | Určíme vyhľadávací zámer a vyberieme hlavnú frázu | Tematické zameranie stránky |
| 4 | Pripravíme krátky a hlavný popis pomocou AI promptu | Návrh obsahu na kontrolu |
| 5 | Skontrolujeme fakty, prínosy, synonymá a sľuby | Obsah zodpovedajúci produktu |
| 6 | Vyplníme SEO názov, meta popis a relevantné polia Yoastu | Nastavené SEO údaje |
| 7 | Upravíme obrázky, alt texty, kategórie a značky | Konzistentná produktová stránka |
| 8 | Opravíme konkrétne upozornenia Yoastu | Skontrolovaný obsah v analyzátore |
| 9 | Overíme technický výstup, mobilné zobrazenie a nákup | Funkčná publikovaná stránka |
| 10 | Zaznamenáme dátum zmien a vyhodnotíme dostupné metriky | Podklad na ďalšie úpravy |

<a id="cast-4"></a>

## 4. Rozdiel medzi jednotlivými nástrojmi

| Nástroj | Úloha pri optimalizácii |
|---|---|
| WordPress | Spravuje obsah, médiá a publikovanie |
| WooCommerce | Spravuje produkty, ceny, produktové údaje a objednávky |
| Yoast SEO Free | Poskytuje základnú SEO analýzu a nastavenia SEO názvu či meta popisu |
| Yoast SEO Premium | Rozširuje prácu napríklad o synonymá, súvisiace kľúčové frázy a ďalšie obsahové funkcie |
| Yoast WooCommerce SEO | Pridáva produktovo špecifickú analýzu a rozširuje prepojenie produktových údajov so štruktúrovanými dátami |
| AI asistent | Pripravuje návrhy textov, varianty a kontrolné rozbory podľa dodaných podkladov |

**Yoast SEO Premium a Yoast WooCommerce SEO nie sú totožné rozšírenia.** Pred optimalizáciou skontrolujeme, ktoré sú na webe aktívne. Špecializované produktové kontroly nebudeme automaticky pripisovať základnému Yoastu.

<a id="cast-5"></a>

## 5. Podklady pred optimalizáciou

- Otvoríme vybraný produkt v administrácii a jeho verejnú stránku
- Zaznamenáme pôvodný SEO názov, meta popis a upozornenia Yoastu
- Pripravíme vlastnosti produktu, cieľové skupiny a podmienky použitia. Pri kurze doplníme aktuálnu osnovu a vstupné požiadavky
- Skontrolujeme jazyk webu a verzie aktívnych pluginov
- Pripravíme obrázky, ktoré budeme skutočne používať
- Poznačíme dátum zmien na následné vyhodnotenie

Tvrdenia o akreditácii, certifikácii, licencii alebo záruke overíme podľa aktuálnych podkladov pre konkrétny produkt. Samotný existujúci popis nie je dôkazom správnosti tvrdenia.

<a id="cast-6"></a>

## 6. Praktický postup v administrácii

V bežnom editore WooCommerce začneme cez:
WordPress → Produkty → Všetky produkty → vybraný produkt → Upraviť

Umiestnenie jednotlivých panelov sa líši podľa editora a konfigurácie. Príslušné polia vyhľadáme v používanom editore produktu.

| Pole alebo časť | Čo upravujeme | Čo skontrolujeme |
|---|---|---|
| Názov produktu | Presné pomenovanie produktu a úrovne | SEO názov je samostatné pole |
| Hlavný popis | Obsah, prínosy, použitie a podmienky | Nepíšeme všeobecné frázy bez informácií |
| Krátky popis produktu | Stručné zhrnutie pre rozhodovanie | Nie je to meta popis |
| Údaje o produkte | Cena, SKU, vlastnosti a typ produktu | Marketingový text nenahrádza tieto údaje |
| Obrázok a galéria | Relevantné vizuály a alternatívne texty | Alt opisuje obsah alebo funkciu obrázka |
| Kategórie produktov | Zaradenie do logickej štruktúry | Vyberáme podľa sortimentu |
| Značky produktov | Konzistentné tematické označenia | Nevytvárame zbytočne desiatky podobných značiek |
| Yoast SEO | Kľúčová fráza, SEO názov a meta popis | Návrh následne kontrolujeme v analyzátore |

WooCommerce rozlišuje virtuálny produkt a produkt na stiahnutie. Prístup k online kurzu automaticky neznamená súbor na stiahnutie. Nastavenie musí zodpovedať spôsobu dodania a napojeniu vzdelávacej platformy.

<a id="cast-7"></a>

## 7. Výber kľúčovej frázy a synoným

Pri výbere výrazov rozlišujeme hlavnú frázu, jej významové varianty, súvisiace témy a produktové značky:

| Pojem | Príklad pre PHP | Použitie |
|---|---|---|
| Hlavná kľúčová fráza | online kurz PHP pre začiatočníkov | Hlavné tematické zameranie produktovej stránky |
| Synonymum alebo blízky variant | online kurz základov PHP | Prirodzené alternatívne pomenovanie |
| Súvisiaca fráza | spracovanie formulárov v PHP | Čiastková téma pokrytá kurzom |
| Produktová značka | PHP | Organizácia obsahu vo WooCommerce |

**Synonymá nie sú zoznamom všetkých tém kurzu.** Napríklad MySQL nie je synonymom PHP a Google Ads nie je synonymom digitálneho marketingu.

Frázy navrhnuté AI berieme ako kandidátov. Ich hľadanosť a vhodnosť overíme pomocou dát, napríklad z Google Search Console alebo nástroja na analýzu kľúčových slov. Yoast používa zadanú frázu na analýzu obsahu, sám tým nepotvrdzuje dopyt na trhu.

<a id="cast-8"></a>

## 8. Príklady optimalizácie štyroch kurzov VITA

Nasledujúce frázy sú **pracovné návrhy bez overenej hľadanosti**. Existujúce URL ponecháme. Nebudeme ich meniť iba kvôli zelenej kontrole v Yoaste.

### Príklad A — Digitálny Marketing II. Mierne Pokročilý

**Cieľ úpravy:** kompletný postup a odlíšenie mierne pokročilého kurzu od začiatočníckeho.

Verejný obsah uvádza napríklad segmentáciu, personalizáciu, GA4, marketingové plánovanie a Google Ads. Na týchto témach postavíme konkrétnu hodnotu produktu.

| Pole | Návrh |
|---|---|
| Hlavná fráza | online kurz digitálny marketing |
| SEO názov | Online kurz Digitálny marketing II. – VITA |
| Synonymá a blízke varianty | online kurz digitálneho marketingu, online kurz online marketingu |
| Súvisiace frázy | digitálny marketing pre mierne pokročilých, plánovanie marketingových kampaní |
| Značky | digitálny marketing, Google Analytics 4, Google Ads, marketingová stratégia |

**Návrh meta popisu:**

> Online kurz Digitálny marketing II. pre mierne pokročilých. Prehĺbte si znalosti GA4, Google Ads, segmentácie a plánovania marketingových kampaní. ✅

**Postup optimalizácie:**

1. V popise jasne uvedieme úroveň kurzu a zohľadníme očakávania návštevníka
2. Dodáme AI osnovu a overené fakty
3. Porovnáme všeobecný text s konkrétnym popisom prínosov
4. Vyplníme Yoast a skontrolujeme spätnú väzbu
5. Posúdime možné prekrývanie s kurzom Digitálny Marketing I. alebo kategóriou kurzov

### Príklad B — Enterprise Architektúra

**Cieľ úpravy:** odborná presnosť a odlíšenie témy od názvu softvéru.

V kurze sa spájajú enterprise architektúra, ArchiMate, TOGAF a práca s nástrojom Enterprise Architect. Tieto pomenovania označujú rozdielne veci.

| Pole | Návrh |
|---|---|
| Hlavná fráza | online kurz enterprise architektúra |
| SEO názov | Online kurz Enterprise architektúra – VITA |
| Synonymá a blízke varianty | online kurz podnikovej architektúry, online kurz enterprise architektúry |
| Súvisiace frázy | modelovanie v ArchiMate, TOGAF a podniková architektúra |
| Značky | enterprise architektúra, podniková architektúra, ArchiMate, TOGAF, Enterprise Architect |

**Návrh meta popisu:**

> Online kurz Enterprise architektúra vás prevedie modelovaním v ArchiMate, rámcom TOGAF a návrhom biznis, aplikačnej a technologickej architektúry. ✅

**Postup optimalizácie:**

1. Oddelíme disciplínu, modelovací jazyk, rámec a softvér
2. Vyhľadáme nesprávne synonymá navrhnuté AI a opravíme ich
3. Preložíme odborné vlastnosti do zrozumiteľných prínosov
4. Skontrolujeme, že text nesľubuje oficiálnu certifikáciu TOGAF bez podkladu

### Príklad C — AutoCAD I. Začiatočník

**Cieľ úpravy:** jasné pomenovanie vstupnej úrovne a prepojenie nástrojov s výsledkom práce.

Obsah kurzu zahŕňa technické kreslenie, úpravy objektov, kótovanie, hladiny a bloky.

| Pole | Návrh |
|---|---|
| Hlavná fráza | online kurz AutoCAD pre začiatočníkov |
| SEO názov | Online kurz AutoCAD pre začiatočníkov – VITA |
| Synonymá a blízke varianty | online kurz základov AutoCADu |
| Súvisiace frázy | technické kreslenie v AutoCADe, kótovanie v AutoCADe |
| Značky | AutoCAD, CAD, technické kreslenie, kótovanie |

**Návrh meta popisu:**

> Online kurz AutoCAD pre začiatočníkov. Naučte sa vytvárať technické výkresy, upravovať objekty, kótovať a pracovať s hladinami aj blokmi. ✅

**Postup optimalizácie:**

1. V texte prepojíme vlastnosť „práca s hladinami“ s prínosom „prehľadné usporiadanie výkresu“
2. Skrátime úvod tak, aby návštevník rýchlo pochopil obsah
3. Otvoríme skutočný obrázok a vytvoríme jeho alt text
4. Skontrolujeme, že popis nepredpokladá zahrnutú licenciu AutoCADu ani výučbu nepotvrdených tém

Príklad alt textu použijeme iba vtedy, ak zodpovedá obrázku: „Technický výkres s kótami a hladinami v prostredí AutoCAD“.

### Príklad D — PHP I. Začiatočník

**Cieľ úpravy:** kontrola technickej správnosti a postupná oprava upozornení Yoastu.

Verejný popis uvádza premenné, riadiace štruktúry, formuláre, GET a POST, funkcie a prácu so súbormi.

| Pole | Návrh |
|---|---|
| Hlavná fráza | online kurz PHP pre začiatočníkov |
| SEO názov | Online kurz PHP pre začiatočníkov – VITA |
| Synonymá a blízke varianty | online kurz základov PHP |
| Súvisiace frázy | programovanie v PHP, spracovanie formulárov v PHP |
| Značky | PHP, webové programovanie, formuláre, serverové programovanie |

**Návrh meta popisu:**

> Online kurz PHP pre začiatočníkov. Osvojte si premenné, podmienky, cykly, funkcie a spracovanie formulárov pri tvorbe dynamických webových stránok. ✅

**Postup optimalizácie:**

1. Porovnáme osnovu s textom navrhnutým AI
2. Odstránime nepodložené zmienky o frameworkoch či pokročilých témach
3. Skopírujeme konkrétne upozornenia Yoastu do opravného promptu
4. Vložíme upravený text a opäť spustíme kontrolu

<a id="cast-9"></a>

## 9. Ako pracujeme so zeleným hodnotením Yoastu

Zelený indikátor použijeme ako praktický cieľ obsahovej kontroly. **Nie je potvrdením správnosti faktov ani zárukou pozície v Google.**

| Upozornenie | Ako postupujeme |
|---|---|
| Fráza chýba v SEO názve | Upravíme názov tak, aby ju prirodzene obsahoval, ideálne na začiatku |
| SEO názov je príliš široký | Skrátime doplnkové slová a overíme výsledok v náhľade |
| Fráza chýba v úvode | Doplníme prirodzenú vetu pomenúvajúcu produkt |
| Meta popis je nevhodne dlhý | Upravíme ho podľa konkrétnej kontroly |
| Text je príliš krátky | Doplníme užitočné informácie o produkte |
| Fráza sa opakuje príliš často | Obmedzíme opakovanie a použijeme prirodzené varianty |
| Chýba vhodný alt text | Opíšeme skutočný obsah obrázka |
| Chýbajú interné odkazy | Vyberieme obsahovo relevantné prepojenia |
| Yoast nevidí časť obsahu | Overíme, čo editor a integrácia poskytujú analyzátoru |

Yoast vykonáva viacero samostatných kontrol a ich dostupnosť závisí aj od produktu a jazyka. Slovenský jazyk podporuje, rozsah jazykových funkcií však nie je pri všetkých jazykoch a edíciách totožný.

Orientačné počty znakov pri SEO názvoch a meta popisoch používame ako pomôcku pri príprave textu. Zobrazenie závisí aj od šírky a zariadenia. Google navyše môže vytvoriť iný titulok alebo úryvok než ten, ktorý zadáme.

<a id="cast-10"></a>

## 10. Univerzálny AI prompt pre akýkoľvek produkt

Tento prompt použijeme ako základ. Funguje pre fyzický produkt, digitálny produkt aj službu, ak doplníme správne podklady.

```text
Pracuj ako SEO špecialista a produktový copywriter pre WordPress, WooCommerce a Yoast SEO.

ÚLOHA
Priprav návrh optimalizácie jednej produktovej stránky.
Text musí pomôcť zákazníkovi pochopiť produkt a rozhodnúť sa.

VSTUPY
Názov produktu: [DOPLŇ]
Typ produktu: [FYZICKÝ PRODUKT / DIGITÁLNY PRODUKT / SLUŽBA]
Existujúca URL: [DOPLŇ]
Cieľová skupina: [DOPLŇ]
Trh a jazyk: [DOPLŇ]
Overené vlastnosti a parametre: [DOPLŇ]
Prínosy doložené vlastnosťami: [DOPLŇ]
Obmedzenia a podmienky použitia: [DOPLŇ]
Čo je a nie je súčasťou produktu: [DOPLŇ]
Aktuálny popis: [VLOŽ]
Dostupné dáta o vyhľadávaní: [VLOŽ ALEBO UVEĎ, ŽE CHÝBAJÚ]
Povolené interné odkazy: [VLOŽ URL A ICH VÝZNAM]
Aktívne rozšírenia Yoast: [DOPLŇ]
Štýl značky: [DOPLŇ]

PRAVIDLÁ
1. Použi iba doložené produktové fakty.
2. Chýbajúce údaje označ ako „potrebné overiť“.
3. Nevymýšľaj cenu, zľavy, recenzie, certifikácie, záruky ani dostupnosť.
4. Ak nevieš otvoriť URL, výslovne to povedz.
5. Bez dát netvrď, že poznáš hľadanosť alebo konkurenciu frázy.
6. Zachovaj existujúcu URL. Zmenu iba samostatne zdôvodni.
7. Píš prirodzene a bez nadmerného opakovania kľúčových slov.
8. Rozlišuj synonymá a súvisiace témy.
9. Alt text navrhni len podľa dodaného obrázka alebo jeho presného opisu.
10. Nesľubuj zelené hodnotenie Yoastu ani konkrétnu pozíciu v Google.
11. Nepoužívaj bodkočiarky.

VÝSTUP
A. Vyhľadávací zámer a potreba zákazníka
B. Jedna odporúčaná hlavná fráza s odôvodnením
C. Synonymá a samostatne súvisiace frázy
D. Tri varianty SEO názvu
E. Dva varianty meta popisu
F. Krátky popis produktu
G. Hlavný popis s vhodnými podnadpismi
H. Päť konkrétnych prínosov podložených vlastnosťami
I. Návrh kategórie a primeraného počtu produktových značiek
J. Návrhy interného prelinkovania iba z dodaných URL
K. Zoznam nepodložených tvrdení a chýbajúcich údajov
L. Kontrolný zoznam pred publikovaním

Výstup označ ako návrh na overenie v editore a analyzátore Yoastu.

```

<a id="cast-11"></a>

## 11. Konkrétne AI prompty pre štyri kurzy

Každý nasledujúci prompt použijeme spolu s aktuálnou osnovou a produktovým textom. Samotná URL nenahrádza podklady, ak ju AI nedokáže načítať.

### Prompt 1 — Digitálny Marketing II.

```text
Priprav SEO optimalizáciu produktu VITA:
Online kurz Digitálny Marketing II. Mierne Pokročilý.

URL:
https://www.vita.sk/online-kurz-digitalny-online-marketing-ii-mierne-pokrocily/

Overené tematické okruhy:
segmentácia, personalizácia, GA4, marketingové plánovanie, Google Ads, USP a SMART ciele.

Aktuálna osnova a popis:
[VLOŽ]

Dáta zo Search Console a prípadné konkurenčné URL na našom webe:
[VLOŽ ALEBO UVEĎ, ŽE CHÝBAJÚ]

Priprav:
- hlavnú frázu, synonymá a súvisiace frázy
- SEO názov a meta popis
- krátky popis
- hlavný popis rozdelený do troch logických častí
- produktové značky
- päť bodov na kontrolu v Yoaste

Odliš kurz od začiatočníckeho kurzu digitálneho marketingu.
Zdôrazni rozhodovanie na základe dát a plánovanie kampaní.
Nesľubuj konkrétny rast predaja, ROAS ani návratnosť investície.
Nevymýšľaj certifikáciu Google alebo ďalší obsah kurzu.

Píš po slovensky a oslovuj čitateľa „vy“.
V popise neuvádzaj trvanie kurzu ani odkazy.
Meta popis ukonči znakom ✅.
Nepoužívaj bodkočiarky ani slová „môžeme“ a „môžem“.
Existujúcu URL zachovaj.

```

### Prompt 2 — Enterprise Architektúra

```text
Priprav SEO optimalizáciu produktu VITA:
Online kurz Enterprise Architektúra.

URL:
https://www.vita.sk/online-kurz-enterprise-architektura/

Aktuálna osnova a popis:
[VLOŽ]

Pri práci presne rozlišuj:
- enterprise architektúra je odborná disciplína
- ArchiMate je modelovací jazyk
- TOGAF je architektonický rámec
- Enterprise Architect je softvérový nástroj

Priprav:
1. Hlavnú frázu a jej významovo vhodné synonymá
2. Samostatný zoznam súvisiacich fráz
3. SEO názov a meta popis
4. Krátky popis
5. Hlavný popis v troch logických častiach
6. Päť prínosov pre záujemcu
7. Produktové značky

Nepovažuj názvy ArchiMate, TOGAF a Enterprise Architect za vzájomné synonymá.
Nesľubuj oficiálnu certifikáciu ani akreditáciu bez podkladu.
Nevymýšľaj pokročilé kompetencie, ktoré osnova nepokrýva.

Píš po slovensky, oslovuj čitateľa „vy“.
V popise neuvádzaj trvanie kurzu ani odkazy.
Meta popis ukonči znakom ✅.
Nepoužívaj bodkočiarky ani slová „môžeme“ a „môžem“.
Existujúcu URL zachovaj.

```

### Prompt 3 — AutoCAD I. Začiatočník

```text
Priprav SEO optimalizáciu produktu VITA:
Online kurz AutoCAD I. Začiatočník.

URL:
https://www.vita.sk/online-kurz-autocad-i-zaciatocnik/

Aktuálna osnova a popis:
[VLOŽ]

Obrázok produktu alebo jeho presný opis:
[VLOŽ]

Priprav hlavnú frázu, synonymá, súvisiace frázy, SEO názov, meta popis, krátky popis a hlavný popis v troch logických častiach. Doplň produktové značky.

Zrozumiteľne prepoj témy s prínosmi:
- kreslenie objektov s tvorbou technických výkresov
- kótovanie s vyjadrením rozmerov
- hladiny s organizáciou výkresu
- bloky s opakovaným použitím prvkov

Nevymýšľaj výučbu 3D, BIM ani pokročilých tém.
Netvrď, že licencia AutoCADu je zahrnutá v cene.
Alt text vytvor iba podľa dodaného obrázka.
Ak obrázok chýba, finálny alt text nevytváraj.

Píš po slovensky a oslovuj čitateľa „vy“.
V popise neuvádzaj trvanie kurzu ani odkazy.
Meta popis ukonči znakom ✅.
Nepoužívaj bodkočiarky ani slová „môžeme“ a „môžem“.
Existujúcu URL zachovaj.

```

### Prompt 4 — PHP I. Začiatočník

```text
Priprav SEO optimalizáciu produktu VITA:
Online kurz PHP I. Začiatočník.

URL:
https://www.vita.sk/online-kurz-php-i-zaciatocnik/

Aktuálna osnova a popis:
[VLOŽ]

Overené témy:
premenné, dátové typy, podmienky, cykly, funkcie, formuláre, GET a POST a práca so súbormi.

Priprav:
- hlavnú frázu, synonymá a súvisiace frázy
- SEO názov a meta popis
- krátky popis
- hlavný popis v troch logických častiach
- produktové značky
- zoznam technických tvrdení na overenie

Vysvetli PHP ako jazyk používaný na serverovej strane.
Nevymýšľaj výučbu Laravelu, Symfony ani pokročilej bezpečnosti.
Bez dôkazu netvrď, že kurz používa najnovšiu verziu PHP.
Výsledné kompetencie prispôsob začiatočníckej úrovni.

Píš po slovensky a oslovuj čitateľa „vy“.
V popise neuvádzaj trvanie kurzu ani odkazy.
Meta popis ukonči znakom ✅.
Nepoužívaj bodkočiarky ani slová „môžeme“ a „môžem“.
Existujúcu URL zachovaj.

```

<a id="cast-12"></a>

## 12. Opravný prompt podľa skutočných upozornení Yoastu

Po vložení návrhu do editora skopírujeme presné upozornenia Yoastu a použijeme ich ako vstup do opravného promptu. Postupujeme v cykle **vložiť → skontrolovať → cielene opraviť → znova skontrolovať**.

```text
Uprav nižšie uvedené SEO podklady podľa konkrétnych upozornení Yoastu.

Hlavná kľúčová fráza:
[VLOŽ]

Aktuálny SEO názov:
[VLOŽ]

Aktuálny meta popis:
[VLOŽ]

Aktuálny produktový text:
[VLOŽ]

Presné upozornenia Yoastu:
[VLOŽ DOSLOVNE]

Aktívne rozšírenia Yoast a jazyk webu:
[VLOŽ]

Pravidlá:
- rieš iba uvedené problémy
- zachovaj produktové fakty, úroveň a význam
- nepridávaj vlastnosti ani marketingové sľuby
- zachovaj existujúcu URL
- nepoužívaj neprirodzené opakovanie frázy
- ak problém vyžaduje zásah do editora alebo integrácie, vysvetli to a nesnaž sa ho riešiť zbytočným predlžovaním textu
- nesľubuj výslednú farbu bez kontroly v Yoaste

Výstup:
1. Opravené polia pripravené na vloženie
2. Stručný zoznam vykonaných zmien
3. Upozornenia vyžadujúce manuálnu kontrolu

```

<a id="cast-13"></a>

## 13. Kontrolný prompt pred publikovaním

```text
Skontroluj návrh produktovej stránky oproti overeným podkladom.

Overené produktové podklady:
[VLOŽ]

Navrhnutý text a SEO polia:
[VLOŽ]

Skontroluj:
- nepodložené alebo vymyslené tvrdenia
- nesúlad medzi produktom a vybranou kľúčovou frázou
- nesprávne synonymá
- neprimerané sľuby výsledkov
- opakovanie kľúčových slov
- rozpor medzi krátkym a hlavným popisom
- tvrdenia o cene, licencii, certifikácii a dostupnosti
- chýbajúce informácie dôležité pre rozhodnutie zákazníka

Výstup priprav ako tabuľku:
Miesto | Problém | Dôkaz z podkladov | Navrhovaná oprava

Chýbajúce informácie označ „potrebné overiť“.
Text neprepisuj celý, ak stačí konkrétna oprava.

```
Aj po tejto kontrole výsledok overíme človekom. Google vo svojich pokynoch výslovne zdôrazňuje kontrolu presnosti a dôveryhodnosti AI obsahu pred publikovaním.

<a id="cast-14"></a>

## 14. Technická časť pre správcov a vývojárov

Obsahová analýza Yoastu je iba jednou časťou kontroly produktu. Po uložení zmien overíme aj výstup publikovanej stránky.

| Kontrola | Čo overíme |
|---|---|
| HTML titulok a meta popis | Či sa uložené údaje objavili vo výstupe stránky |
| Hlavný nadpis | Či šablóna správne zobrazuje názov produktu |
| Indexovateľnosť | Či stránka nemá neželané nastavenie noindex |
| Canonical | Či označuje zamýšľanú kanonickú URL |
| Cena a mena | Či sú viditeľné údaje a štruktúrované dáta v súlade |
| Recenzie | Či ide o skutočné hodnotenia daného produktu |
| Identifikátory | Či používame skutočné SKU a prípadné GTIN |
| Schema | Či nevznikajú konfliktné údaje z viacerých rozšírení |

Yoast WooCommerce SEO dopĺňa produktový schema výstup a prepája dostupné údaje o ponuke či hodnoteniach. Kurzom nevymýšľame EAN alebo GTIN iba preto, aby zmizlo upozornenie. SKU je interný identifikátor a nemožno ho automaticky zameniť za GTIN.

Výstup overíme v nástroji Google Rich Results Test:

- **[https://search.google.com/test/rich-results](https://search.google.com/test/rich-results)**

Platné štruktúrované dáta nezaručujú zobrazenie rozšíreného výsledku. Pri online kurzoch tiež nebudeme automaticky predpokladať rovnakú oprávnenosť pre všetky nákupné funkcie Googlu ako pri fyzickom tovare.

<a id="cast-15"></a>

## 15. Kontrola publikovanej stránky a meranie výsledkov

Po uložení a publikovaní zmien overíme:

- Zhodu textov so skutočným produktom
- Jasnú cieľovú skupinu a úroveň
- SEO názov a meta popis v náhľade Yoastu
- Prirodzenosť hlavnej frázy a jej variantov
- Vhodné kategórie a produktové značky
- Obrázky a ich alternatívne texty
- Funkčnosť nákupu a zobrazenie na mobile
- Výsledný HTML výstup a produktové dáta

**Záznam vykonaných zmien:** Pre každý upravený produkt uchováme pôvodný a nový SEO názov, meta popis, produktový text, upozornenia Yoastu, dátum úpravy a stručné zdôvodnenie zmien. Tento záznam použijeme pri porovnávaní výsledkov.

Pri následnom vyhodnotení oddelíme organické kliknutia a zobrazenia, návštevnosť produktovej stránky a objednávky. Porovnanie pred úpravou a po nej posúdime spolu so sezónnosťou, reklamou, cenovými zmenami a ďalšími zásahmi.

Ďalšie úpravy plánujeme podľa zistených problémov a dostupných dát. Pri každej zmene overíme súlad obsahu s produktom aj správne zobrazenie na publikovanom webe.

<a id="zdroje"></a>

## Zdroje a referenčné stránky

### Dokumentácia Yoast

- **[https://yoast.com/features/seo-analysis/](https://yoast.com/features/seo-analysis/)**
- **[https://yoast.com/product-descriptions-woocommerce-seo/](https://yoast.com/product-descriptions-woocommerce-seo/)**
- **[https://developer.yoast.com/features/schema/plugins/woocommerce-seo/](https://developer.yoast.com/features/schema/plugins/woocommerce-seo/)**
- **[https://yoast.com/focus-keyphrase-for-product-pages-yoast-seo/](https://yoast.com/focus-keyphrase-for-product-pages-yoast-seo/)**
- **[https://yoast.com/features/seo-analysis/synonyms/](https://yoast.com/features/seo-analysis/synonyms/)**
- **[https://yoast.com/help/features-per-language/](https://yoast.com/help/features-per-language/)**
- **[https://yoast.com/help/how-to-add-product-identifiers-with-woocommerce-seo/](https://yoast.com/help/how-to-add-product-identifiers-with-woocommerce-seo/)**
- **[https://yoast.com/global-identifiers-woocommerce-seo/](https://yoast.com/global-identifiers-woocommerce-seo/)**

### Dokumentácia WooCommerce

- **[https://woocommerce.com/document/managing-products/product-editor-settings/](https://woocommerce.com/document/managing-products/product-editor-settings/)**
- **[https://woocommerce.com/document/managing-products/](https://woocommerce.com/document/managing-products/)**

### Dokumentácia Google Search Central

- **[https://developers.google.com/search/docs/appearance/title-link](https://developers.google.com/search/docs/appearance/title-link)**
- **[https://developers.google.com/search/docs/appearance/snippet](https://developers.google.com/search/docs/appearance/snippet)**
- **[https://developers.google.com/search/docs/fundamentals/using-gen-ai-content](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)**
- **[https://developers.google.com/search/docs/appearance/structured-data/product](https://developers.google.com/search/docs/appearance/structured-data/product)**

### Referenčné produktové stránky

- **[https://www.vita.sk/online-kurz-digitalny-online-marketing-ii-mierne-pokrocily/](https://www.vita.sk/online-kurz-digitalny-online-marketing-ii-mierne-pokrocily/)**
- **[https://www.vita.sk/online-kurz-enterprise-architektura/](https://www.vita.sk/online-kurz-enterprise-architektura/)**
- **[https://www.vita.sk/online-kurz-autocad-i-zaciatocnik/](https://www.vita.sk/online-kurz-autocad-i-zaciatocnik/)**
- **[https://www.vita.sk/online-kurz-php-i-zaciatocnik/](https://www.vita.sk/online-kurz-php-i-zaciatocnik/)**
