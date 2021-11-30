#!/bin/bash
PARAM_PREVIOUS_VERSION=$1
PARAM_CURRENT_VERSION=$2

if [ -z $GREN_GITHUB_TOKEN ]; then
    echo "Access token should be an environment variable."
    echo "Check this doc: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token"
    exit 1
fi

gren changelog --generate --override --tags=$PARAM_PREVIOUS_VERSION..$PARAM_CURRENT_VERSION
gren release --override --tags=$PARAM_PREVIOUS_VERSION..$PARAM_CURRENT_VERSION