# Shortify 2

A revamped version of the free GitHub Pages link shortener Shortify.

## Adding links

Add a link to the shortener by adding it to `routes.yml`, committing and pushing to main. This will trigger a GitHub workflow to build and deploy the new link automatically.

See [Deploy](#deploy) for more details.

## Dev setup

Clone the repo and cd into the directory. Then follow the steps below to set up a virtual environment and install the dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

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