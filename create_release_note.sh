#!/bin/bash
export GREN_GITHUB_TOKEN={GIT_TOKEN}

echo $GREN_GITHUB_TOKEN

if [ -z $GREN_GITHUB_TOKEN ]; then
    echo "Access token should be an environment variable."
    echo "Check this doc: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"
    exit 1
fi

gren changelog --generate --override