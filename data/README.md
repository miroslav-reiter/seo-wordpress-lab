# 🧪 Testovacie SEO dáta

Súbory `pages.csv` a `links.csv` obsahujú **fiktívny model webu**, nie export z VITA.sk.

- `pages.csv`: URL, titulok, príznak indexovateľnosti, typ obsahu.
- `links.csv`: zdrojová URL, cieľová URL, anchor text a umiestnenie odkazu.

Úmyselné problémy:
- `/blog/stary-navod/` a `/faq/prihlasenie/` nemajú prichádzajúce odkazy.
- `/kurzy/neexistujuci/` nie je indexovateľný a reprezentuje vyradený obsah, na ktorý zostal odkaz.
- Kotvy „Kliknite sem“ a „Viac informacii“ majú nevýstižný text.
- Viacero odkazov z jednej zdrojovej stránky smeruje na rovnaký cieľ; porovnajte **Inlinks** a **Unique Inlinks**.

Spustenie lokálneho auditu:
```bash
python3 scripts/internal_link_audit.py --pages data/pages.csv --links data/links.csv
```

Skript nemení súbory ani neposiela požiadavky na internet. Hĺbku vypočítava od `/` pomocou BFS. Bez prichádzajúcich odkazov môže byť i stránka uvedená v sitemape, preto zobrazený nález interpretujeme iba v rámci daných dát.
