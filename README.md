# Shortify 2

A revamped version of the free GitHub Pages link shortener Shortify.

## Adding links

Add a link to the shortener by adding it to `routes.yml`, committing and pushing to main. This will trigger a GitHub workflow to build and deploy the new link automatically.

See [Deploy](#deploy) for more details.

## Preview link

If you want to see where a link leads before redirecting, add `?preview=true` at the end of the link. For example, this is how you would preview the link leading to `python`:
```
https://s.godi.se/python?preview=true
```

## Dev setup

Clone the repo and cd into the directory. Then follow the steps below to set up a virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

> [!IMPORTANT]
> For local development, you have to include `.html` after the link. For example the link to `/python` would be `/python.html`

## Dev commands

### Build

Run `build.py` while inside the virtual environment.

```bash
python build.py
```

### Deploy

Deploying is easy, following the steps below:

1. Add/update the routes in `routes.yml` with the format `name: url` for new links
2. Add and commit the file to Git
3. Push to main

GitHub Actions will take care of the rest, and deploy the new shortened links.

> [!NOTE]
> You can add/edit/delete links quickly by updating the `routes.yml` file in the GitHub UI. Committing to main will redeploy with your changes.