# redirect-chain

A simple cli tool to see the history of redirects of a URL.
Sample output:

```bash
▶ redirect-chain https://developer.mozilla.org/learn/html
0  https://developer.mozilla.org/learn/html 301
1 > https://developer.mozilla.org/Learn/HTML 302
2 >> https://developer.mozilla.org/docs/Learn/HTML 302
3 >>> https://developer.mozilla.org/en-US/docs/Learn/HTML 200
```

## Installation

```bash
pipx install redirect-chain
redirect-chain http://www.peterbe.com/oc-
```

## License

MIT
