# Demi's Greek Songs

## Setup

1. First, make sure homebrew is installed (`brew -v`) and if not, run this:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. Add env variable credentials to you `.bash_profile`:
```bash
export SPOTIPY_CLIENT_ID='some client id'
export SPOTIPY_CLIENT_SECRET='some client secret'
```

3. Open a new terminal window so the env variables are set

4. Next, install Pipenv:
```bash
brew install pipenv
```

5. Install dependencies:
```bash
pipenv install --dev
```

Enter the virtualenv shell:
```bash
pipenv shell
```

Run the app:
```bash
python main.py
```
