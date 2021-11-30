#!/bin/bash

PARAM_VERSION_TYPE=$1

Help() {
    file_name=$(basename "$0")
    echo
    echo "Syntax: ./$file_name [-M | -m | -p | -h ]"
    echo "options:"
    echo
    echo "-h | help     Print this Help."
    echo "-M | major    upgrading a major version ex. vX.0.0"
    echo "-m | minor    upgrading a minor version ex. v0.X.0"
    echo "-p | patch    upgrading a patch version ex. v0.0.X"
    echo
}

update_version() {
    #get number parts and increase last one by 1
    case $PARAM_VERSION_TYPE in
    -i | init)
        echo "Initial version...";
        validate_version
        ;;
    -M | major)
        VNUM1=$((VNUM1 + 1))
        VNUM2=0
        VNUM3=0
        ;;
    -m | minor)
        VNUM2=$((VNUM2 + 1))
        VNUM3=0
        ;;
    -p | patch)
        VNUM3=$((VNUM3 + 1))
        ;;
    -h | help)
        Help
        exit
        ;;
    *)
        Help
        exit 1
        ;;
    esac
    NEW_TAG="${VNUM1}.${VNUM2}.${VNUM3}"
}

publish_version() {
    echo "Publishing tag $NEW_TAG"
    git tag $NEW_TAG -m "Release $NEW_TAG"
    git push --tags
}

prompt_publish() {
    while true; do
        read -p "Do you wish to publish this version? (y/n) " yn
        case $yn in
        [Yy]*)
            publish_version
            break
            ;;
        [Nn]*)
            echo "Skiping version..."
            exit
            ;;
        *) echo "Please answer yes or no." ;;
        esac
    done
}

validate_version() {
    #get highest tag number
    VERSION=$(git describe --abbrev=0 --tags 2>/dev/null)

    if [ -z $VERSION ]; then
        NEW_TAG="v1.0.0"
        echo "No tag present. Creating the first one $NEW_TAG"
        prompt_publish
        exit 0
    fi
}

main() {
    if [ -z $PARAM_VERSION_TYPE ]; then
        echo "Version parameter it's missing"
        Help
        exit 1
    fi

    validate_version

    #replace . with space so can split into an array
    VERSION_BITS=(${VERSION//./ })
    VNUM1=${VERSION_BITS[0]}
    VNUM2=${VERSION_BITS[1]}
    VNUM3=${VERSION_BITS[2]}

    #get current hash and see if it already has a tag
    GIT_COMMIT=$(git rev-parse HEAD)
    CURRENT_COMMIT_TAG=$(git describe --contains $GIT_COMMIT 2>/dev/null)

    #only tag if no tag already (would be better if the git describe command above could have a silent option)
    if [ -z "$CURRENT_COMMIT_TAG" ]; then
        update_version
        echo "Updating $VERSION to $NEW_TAG"
    else
        echo "This commit is already tagged as: $CURRENT_COMMIT_TAG"
        exit 0
    fi

    prompt_publish
}

main
