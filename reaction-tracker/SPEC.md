# Reaction Tracker

Implement `ReactionTracker` in `tracker.py`. Standard library only.

You may use any tools you normally use, including AI. I will ask you to explain
your code.

---

## The system

An upstream queue delivers reaction events. Each one looks like this:

```
event_id = "e1"   user_id = "u1"   target_id = "post-42"   kind = "like"     ts = 1000
event_id = "e2"   user_id = "u1"   target_id = "post-42"   kind = "unlike"   ts = 2000
```

`ts` is an integer timestamp **assigned by the producer**, not by you.

Two methods:

```python
tracker.record(event_id, user_id, target_id, kind, ts)   # ingest one event
tracker.like_count(target_id)  -> int                     # read
```

`like_count` returns **the number of distinct users currently in the liked
state for that target.**

---

## What Operations is telling you

These are real reports from production. They are your requirements.

1. **"A user tapped like twice and it counted twice."**
   The two taps arrived as two events with **different `event_id`s**.
   Deduplicating on `event_id` did not catch it.

2. **"A user unliked something and the count didn't go down — sometimes."**
   The queue does not preserve order. We have seen the `unlike` (`ts=2000`)
   arrive **before** the `like` (`ts=1000`) it undoes.

3. **"The count drifted."**
   After a burst of traffic, `like_count` did not match the number of users
   actually in the liked state. It was off in **both** directions.

4. **"Somebody unliked something they never liked."**
   An `unlike` arrives with no prior `like`. Decide what that means, and make
   sure it cannot corrupt the count.

---

## Constraints

- Standard library only.
- `record` is called **concurrently from multiple threads**.
- Targets are created implicitly. Reading a target nobody has touched is not
  an error.

---

## Parts of this spec are deliberately incomplete

Some of the behaviour is not stated here. You have to decide it.

**State your decision and your reasoning.** An assumption you made silently is
the failure mode I am looking for.

---

## When you are done, be ready to walk through

- Where the state lives, and why that shape.
- What your code does when a `like` and an `unlike` for the same user and
  target carry the **same `ts`**.
- Why your count cannot drift — in one sentence.
