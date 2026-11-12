# Attribution and licences of the inputs

The files in `corpus/` and `dictionaries/` are derived from the sources below.
[SOURCES.json](SOURCES.json) pins each source's revision and the SHA-256 of every derived file.
[tools/sources.py](../tools/sources.py) does every change listed here.

## PHP manual

- Source: [php/doc-en](https://github.com/php/doc-en), [doc-es](https://github.com/php/doc-es), [doc-ru](https://github.com/php/doc-ru), [doc-zh](https://github.com/php/doc-zh), [doc-ja](https://github.com/php/doc-ja).
- Author: the PHP Documentation Group.
- Licence: [Creative Commons Attribution 3.0](https://creativecommons.org/licenses/by/3.0/).
- Derived files:
  - `corpus/{en,es,ru,zh,ja}.txt`: text of the manual with the XML markup removed, about 4 MiB;
  - `corpus/emoji.txt`: `en.txt` with emoji sequences inserted;
  - `corpus/manual-pages.json`: English pages as separate texts;
  - `dictionaries/php-identifiers.json`, `dictionaries/php-functions.json`: function and method names from the manual;
  - `dictionaries/words-{en,es,ru,zh,ja}.json`, `dictionaries/words-en-frequent.json`: words of given frequency ranks.
- The derived files are under the same licence.

## MDN translated content

- Source: [mdn/translated-content](https://github.com/mdn/translated-content), Korean pages.
- Authors: Mozilla Contributors.
- Licence: [Creative Commons Attribution-ShareAlike 2.5](https://creativecommons.org/licenses/by-sa/2.5/).
- Derived files: `corpus/ko.txt` (text with the markup removed, about 4 MiB) and `dictionaries/words-ko.json`.
- These two files are offered under CC BY-SA 2.5.

## Civil Comments

- Source: [google/civil_comments](https://huggingface.co/datasets/google/civil_comments), file `data/test-00000-of-00001.parquet`.
- Licence: [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
- Derived file: `corpus/comments.json`, the first 10,000 comment texts.

## User-Agent strings and crawler patterns

- [monperrus/crawler-user-agents](https://github.com/monperrus/crawler-user-agents), © 2017 Martin Monperrus, MIT licence ([copy](licenses/crawler-user-agents.LICENSE)).
- [intoli/user-agents](https://github.com/intoli/user-agents), © 2018-present Intoli, LLC, 2-Clause BSD licence ([copy](licenses/intoli-user-agents.LICENSE)).
- Derived files:
  - `dictionaries/crawler-patterns.json`: the patterns of crawler-user-agents that are literal strings;
  - `corpus/user-agents.json`: 10,000 strings, about 80% browsers sampled by weight from intoli/user-agents and 20% crawler instances from crawler-user-agents.

## LDNOOBW

- See [dictionaries/ldnoobw/ATTRIBUTION.md](../dictionaries/ldnoobw/ATTRIBUTION.md).
