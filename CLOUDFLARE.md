# Cloudflare deployment

Worker name: `vindam-fitness`.

The static site is served from `dist/`. `node scripts/stage-dist.mjs` copies `public/` into `dist/` before deploy. Hosting commands use `cf`.

Pushes to `main` deploy through GitHub Actions (`.github/workflows/deploy.yml`). Add these repository secrets before the first run:

- `CLOUDFLARE_API_TOKEN`: an API token from the Edit Cloudflare Workers template.
- `CLOUDFLARE_ACCOUNT_ID`: the account that owns this Worker.

A local deploy uses Node.js 22.18 or newer:

```powershell
npm install
npx cf deploy --dry-run
npm run deploy
```

Published URL:

https://vindam-fitness.programmingwhilesleeping.workers.dev
