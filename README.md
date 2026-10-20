# Vindam Fitness Gym

Demo site for Vindam Fitness Gym, Lucena City.

Live site: https://vindam-fitness.programmingwhilesleeping.workers.dev/

## Facts on the page

- Address: Maharlika Hwy, Lucena City
- Phone: +63 966 522 5892
- Email: geobellerivera@gmail.com
- Facebook: https://www.facebook.com/purokhappyvalleyibabangdupayredv
- Rating shown: 4.7 on Google
- Directions: https://www.google.com/maps/search/Vindam%20Fitness%20Gym%20Lucena%20City
- Membership rates and gym hours are not listed. The page says to message the gym.

## Photos

The live slots are real gym photos. To swap one, save over the same filename:

- `public/photos/1.jpg` — hero
- `public/photos/2.jpg` through `public/photos/6.jpg` — strip under the hero

See `public/photos/SLOTS.txt`.

## Local preview

```powershell
python -m http.server 4721 --directory public
```

Open http://127.0.0.1:4721.

## Cloudflare

Pushes to `main` deploy with `.github/workflows/deploy.yml`. The workflow needs repository secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.

Worker name: `vindam-fitness`.
