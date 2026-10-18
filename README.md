# Portfolio

Sito statico per GitHub Pages. Nessuna dipendenza o fase di build richiesta.

## Pubblicazione

Il deploy è automatico: a ogni push su `main` il workflow `CI` esegue i check (HTML, accessibilità, link, video) e, se passano, pubblica su GitHub Pages solo i file del sito (`index.html`, `styles.css`, `script.js`, `assets/`). In **Settings → Pages** la sorgente deve essere **GitHub Actions**.


## Video manifesto

Per creare un video con Hyperframes usando Claude Code, esegui dalla radice del repository:

```bash
npx skills add heygen-com/hyperframes
```

Scegli **Core Skills**, riapri Claude Code nella cartella e usa il comando `/hyperframes` con il brief preparato nella conversazione Codex.
