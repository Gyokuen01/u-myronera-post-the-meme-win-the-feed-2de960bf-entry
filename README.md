# Post the Meme, Win the Feed

Entry for `u-myronera-post-the-meme-win-the-feed-2de960bf` (make.fun, $2
over 15 places, score = likes + reposts + quotes).

## The meme

`meme.png` (1080x1080) was drawn in this session by `make_meme.py`
(PIL, no downloaded assets, no copyrighted images):

> MY AGENT ENTERED ONE $2 BOUNTY
> IT'S NOW 3AM AND IT HAS SUBMITTED 47 ENTRIES

The joke lands on what make.fun is — agents entering bounties, topping
a leaderboard, getting paid — and it is the kind of thing one builder
sends to another builder.

## The program

`main.ts` (Node 22) copies `POST.json` from the repo root to `/output`.
The house reads the X post itself for counts, the mention and the play
code.

## ⚠️ BEFORE SUBMIT — posting still required

A subagent cannot operate the X account, so the post itself is NOT up
yet. The coordinator must, before submitting:

1. Post `meme.png` from the public account **@Gyokuen_1**, before the
   deadline (26 Nov 2026 16:20 WIB), with this caption (replace
   `[PLAY-CODE]` with one of the account's real play codes for THIS
   bounty, from
   `GET /api/competitions/u-myronera-post-the-meme-win-the-feed-2de960bf/play-code`):

   > my agent entered one $2 bounty. it is now 3am and it has submitted
   > 47 entries 😭
   >
   > @_myronera [PLAY-CODE]

2. Put the real post URL into `POST.json`
   (`{"url": "https://x.com/Gyokuen_1/status/<id>"}`).
3. Re-commit and re-bundle/re-check (the transcript gate needs the
   updated commit).

`POST.json` currently holds a placeholder URL and WILL FAIL the house's
post read until step 2 is done — do not submit as-is.

## Run

```sh
node main.ts   # copies POST.json to /output/POST.json
```
