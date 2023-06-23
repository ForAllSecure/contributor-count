# Mayhem Contributor Count

This app will help you determine the number of contributors for your
source control repositories for the purpose [Mayhem](https://mayhem.security)
licensing.

## Running (Docker Instructions)

### Prerequisites

* `docker`

### Instructions

1. Clone the repository

```bash
git clone git@github.com:ForAllSecure/contributor-count.git
```

2. Build the Docker image

```bash
docker build -t mayhem-contributor-count:latest .
```

3. Run the app with docker (Example azure devops)

```bash
docker run -it --rm mayhem-contributor-count:latest azure-devops --token pvk... --organization my-organization
```

## Running from source (Python Instructions)

### Prerequisites

* `Python 3.9+`

### Instructions

1. Clone the repository

```bash
git clone git@github.com:ForAllSecure/contributor-count.git
```

2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Run the app (Example azure devops)

```bash
./contrib-count.py azure-devops --token pvk... --organization my-organization
```

# Supported SCM (Source Control Management) sources

## Azure DevOps

### Prerequisites

* **Personal access token**

  You will need a [Personal Access Token](https://docs.microsoft.com/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=vsts)
  in order to access your Azure DevOps repositories.

### Examples


> ℹ️ The following examples run the script from source. 
> 
> If you are using Docker instructions, simply substitute
> 
> `./contrib-count.py`
> 
> for
> 
> `docker run -it --rm mayhem-contributor-count:latest`


#### Get contributor counts for ALL Projects in the last 90 days

```bash
./contrib-count.py azure-devops --token pvk... --organization my-organization
```

#### Get contributor counts for ALL Projects in the last 180 days

```bash
./contrib-count.py azure-devops --token pvk... --organization my-organization --since-days 180
```

#### Get contributor counts for specific Projects in the last 90 days

```bash
./contrib-count.py azure-devops --token pvk... --organization my-organization --projects "project1,project2"
```

