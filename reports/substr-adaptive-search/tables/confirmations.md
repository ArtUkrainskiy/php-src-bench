# Complete finite AMD confirmation stage

Every selected case is retained, including favourable, unfavourable and noisy originals. One A/B repeat per selected case. All originally usable slower cases also have stock and candidate A/A controls. The fixed [policy](../data/amd/final-confirmation/policy.json) and [selection](../data/amd/final-confirmation/selection.json) are unchanged.

| Case | Compiler | Original elapsed change | Repeat elapsed change | Original result | Repeat result | Source |
|---|---|--:|--:|---|---|---|
| banlist12/en/comment/early | GCC 15.2 | +2.93% | −2.62% | Noise | Unclear | [gcc15-case002-ab-repeat](../data/amd/final-confirmation/gcc15-case002-ab-repeat.json) |
| banlist12/ru/thread/early | GCC 15.2 | +0.82% | +1.81% | Noise | Noise | [gcc15-case017-ab-repeat](../data/amd/final-confirmation/gcc15-case017-ab-repeat.json) |
| banlist12/es/post/early | GCC 15.2 | +1.27% | +0.56% | Noise | Unclear | [gcc15-case021-ab-repeat](../data/amd/final-confirmation/gcc15-case021-ab-repeat.json) |
| parse-records/4k | GCC 15.2 | +1.51% | +0.84% | Slower | Unclear | [gcc15-case063-ab-repeat](../data/amd/final-confirmation/gcc15-case063-ab-repeat.json) |
| parse-query/4k | GCC 15.2 | +1.04% | +0.44% | Slower | Unclear | [gcc15-case064-ab-repeat](../data/amd/final-confirmation/gcc15-case064-ab-repeat.json) |
| parse-http/body64k | GCC 15.2 | +2.54% | +2.24% | Slower | Slower | [gcc15-case066-ab-repeat](../data/amd/final-confirmation/gcc15-case066-ab-repeat.json) |
| log-contains/level/thread/early | GCC 15.2 | −22.07% | −23.76% | Noise | Faster | [gcc15-case074-ab-repeat](../data/amd/final-confirmation/gcc15-case074-ab-repeat.json) |
| banlist12/zh/thread/early | GCC 15.2 | −17.35% | −14.23% | Noise | Faster | [gcc15-case110-ab-repeat](../data/amd/final-confirmation/gcc15-case110-ab-repeat.json) |
| explode-limit2/colon2/short | GCC 15.2 | +2.08% | +1.32% | Slower | Unclear | [gcc15-case146-ab-repeat](../data/amd/final-confirmation/gcc15-case146-ab-repeat.json) |
| parse-query/small | GCC 15.2 | +1.41% | +1.66% | Slower | Slower | [gcc15-case181-ab-repeat](../data/amd/final-confirmation/gcc15-case181-ab-repeat.json) |
| parse-query/64k | GCC 15.2 | +1.01% | +0.77% | Slower | Unclear | [gcc15-case183-ab-repeat](../data/amd/final-confirmation/gcc15-case183-ab-repeat.json) |
| parse-http/cookie4k | GCC 15.2 | +1.31% | +2.48% | Slower | Slower | [gcc15-case185-ab-repeat](../data/amd/final-confirmation/gcc15-case185-ab-repeat.json) |
| explode/pipe2/4k | Clang 21.1 | +3.24% | +0.20% | Slower | Unclear | [clang21-case052-ab-repeat](../data/amd/final-confirmation/clang21-case052-ab-repeat.json) |
| explode/comma/64k | Clang 21.1 | +0.30% | −0.59% | Noise | Unclear | [clang21-case062-ab-repeat](../data/amd/final-confirmation/clang21-case062-ab-repeat.json) |
| log-contains/level/post/early | Clang 21.1 | −20.92% | −17.73% | Noise | Faster | [clang21-case070-ab-repeat](../data/amd/final-confirmation/clang21-case070-ab-repeat.json) |
| log-contains/event/thread/early | Clang 21.1 | −18.67% | −13.18% | Noise | Faster | [clang21-case073-ab-repeat](../data/amd/final-confirmation/clang21-case073-ab-repeat.json) |
| log-contains/level/thread/early | Clang 21.1 | −16.93% | −25.15% | Noise | Noise | [clang21-case074-ab-repeat](../data/amd/final-confirmation/clang21-case074-ab-repeat.json) |
| explode/tab/short | Clang 21.1 | −1.17% | −0.84% | Noise | Unclear | [clang21-case170-ab-repeat](../data/amd/final-confirmation/clang21-case170-ab-repeat.json) |
| explode/amp/4k | Clang 21.1 | +2.57% | +1.77% | Noise | Unclear | [clang21-case176-ab-repeat](../data/amd/final-confirmation/clang21-case176-ab-repeat.json) |
| explode/amp/absent | Clang 21.1 | +0.74% | −2.15% | Noise | Noise | [clang21-case179-ab-repeat](../data/amd/final-confirmation/clang21-case179-ab-repeat.json) |
| find-http-end/incomplete | Clang 21.1 | +0.05% | −1.38% | Noise | Unclear | [clang21-case189-ab-repeat](../data/amd/final-confirmation/clang21-case189-ab-repeat.json) |
| render-template/small | Clang 21.1 | −1.88% | −1.18% | Noise | Unclear | [clang21-case191-ab-repeat](../data/amd/final-confirmation/clang21-case191-ab-repeat.json) |
| document/html-phpnet/href="/4k | Clang 21.1 | −0.08% | +1.79% | Noise | Unclear | [clang21-case222-ab-repeat](../data/amd/final-confirmation/clang21-case222-ab-repeat.json) |
