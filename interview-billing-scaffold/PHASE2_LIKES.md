# Phase 2 — Reactions (like / unlike)

> Give this to the candidate **after** Phase 1 is passing. Budget ~30 minutes.
> Everything you already built stays. This extends it.

---

## What changed

Product wants reactions on posts. The same `POST /events` endpoint now also
receives two new event types:

```json
{ "event_id": "e1", "user_id": "u1", "type": "like",   "target_id": "post-42", "ts": 1000 }
{ "event_id": "e2", "user_id": "u1", "type": "unlike", "target_id": "post-42", "ts": 2000 }
```

And there is one new read endpoint:

```
GET /posts/{post_id}/likes   ->   { "likeCount": 3 }
```

`likeCount` is **the number of distinct users currently in the liked state for
that post.**

---

## What Operations is telling you

These are the reports from production. They are the requirements.

1. **"A user tapped like twice and it counted twice."**
   The two taps came in as two events with **different `event_id`s**. Your
   Phase 1 dedup did not catch it.

2. **"A user unliked a post and the count didn't go down — sometimes."**
   The upstream queue does not preserve order. We have seen the `unlike`
   (`ts=2000`) arrive **before** the `like` (`ts=1000`) it undoes.

3. **"The count drifted."**
   After a burst, `likeCount` did not match the number of users actually in the
   liked state. It was off by a few in both directions.

4. **"Somebody unliked something they never liked."**
   An `unlike` with no prior `like` arrives. Decide what that means and make it
   not corrupt the count.

---

## Constraints

- Existing Phase 1 behaviour must keep working. Do not break `/users/{id}/stats`.
- `like` / `unlike` events also flow through `POST /events`, so they must not
  silently pollute the Phase 1 stats in a way that breaks billing. Decide what
  the right call is and say why.
- Assume multiple requests are in flight at once.

---

## What is deliberately not specified

The spec is incomplete **on purpose**. Some of it you must decide.
State your decision and your reasoning — an unstated assumption is the failure
mode we are looking for.

---

## When you are done

Be ready to walk through:
- Where state lives, and why that shape.
- What happens when two events for the same (user, post) carry the **same `ts`**.
- Why your `likeCount` cannot drift, in one sentence.
