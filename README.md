# Intro
To configure the new path for hooks, change the git config:

```shell
$ git config core.hooksPath .githooks
```

For earlier versions:

```shell
$ find .git/hooks -type l -exec rm {} \;
$ find .githooks -type f -exec ln -sf ../../{} .git/hooks/ \;
```