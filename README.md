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
- Membership rates and gym hours are not listed. Every "Message us" link opens Messenger: https://m.me/purokhappyvalleyibabangdupayredv
- Call and email stay on the page as secondary contact.

## Photos

The live slots are real gym photos. To swap one, save over the same filename:

- `public/photos/hero.jpg` — full-bleed hero
- `public/photos/floor-benches.jpg`
- `public/photos/floor-bright.jpg`
- `public/photos/floor-hall.jpg`
- `public/photos/floor-rack.jpg`
- `public/photos/floor-corridor.jpg`

See `public/photos/SLOTS.txt`.

## Local preview

```powershell
python -m http.server 4721 --directory public
```

Open http://127.0.0.1:4721.

## Cloudflare

Pushes to `main` deploy with `.github/workflows/deploy.yml`. The workflow needs repository secrets `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.

Worker name: `vindam-fitness`.
