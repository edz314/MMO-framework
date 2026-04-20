# MMO-framework

A Python sandbox for NPC behaviour using state machines and decision trees.

## Status

Personal project. Actively developed in small bursts over a long period.
Not a finished framework, not a game, and not something to pull into a
shipped title. The code is me thinking about how to compose legible NPC
behaviour — it is not competing with Behavior Designer, Unreal's Behavior
Trees, or the current crop of LLM-driven NPC middleware.

## What the project is exploring

The deliberate constraint of this repo is classical game AI: finite state
machines and decision trees, with behaviour profiles as the unit of
composition. That's the older tradition. It was chosen on purpose.

What I'm interested in is *legibility*. An FSM + decision tree NPC can be
fully audited — every transition is inspectable, every decision has a
cause, and the behaviour profile for a given archetype (guard, scavenger,
merchant, faction agent) is a single artefact you can read, diff, and
version. LLM-driven NPCs offer richer surface behaviour at the cost of that
legibility. I wanted a scaffold where the behavioural contract is visible
before any generative layer goes on top of it, not after.

It's also where this connects to the broader architecture work I do: a
well-structured NPC is a small, tractable instance of the same problem
enterprise systems face — state, transitions, policies, data-driven
behaviour, and the question of which decisions belong inside the machine
and which belong in the configuration around it.

## Current scope

Implemented or scaffolded:

- state machine with the standard idle/patrol/chase/attack archetype set
- decision tree evaluator reading from a bounded world-state abstraction
- behaviour profiles as composable configuration units keyed by NPC type
- data-management layer for per-NPC attributes and world observations
- test harness for deterministic behaviour under fixed world inputs

Not implemented, despite what the directory layout might suggest:

- network transport or any actual MMO substrate — this is single-process
- persistence beyond in-memory
- integration with any specific game engine
- the `/assets/` directory is structure, not content

If the name gives the impression of something that could handle thousands
of concurrent NPCs over a network, it shouldn't. "MMO" in the name reflects
the *kind* of NPC being modelled — one that needs to operate in a
persistent, multi-agent world — not the operational scale of the
implementation.

## Running it

Requires Python 3.10+.

    git clone https://github.com/edz314/MMO-framework.git
    cd MMO-framework
    pip install -r requirements.txt
    pytest tests/

There is no runnable world entry point. The framework is consumed by
instantiating behaviour profiles against a world-state stub. See `tests/`
for working examples of how an NPC is configured and stepped through its
FSM.

## Design sketch

Three layers, kept intentionally separate:

**State.** The FSM defines what the NPC is currently doing. Transitions
are triggered by the decision tree, not by hand-coded `if` branches inside
states.

**Decision.** The decision tree reads from a bounded set of world
observations (proximity, faction, health, time of day) and resolves to a
target state. Trees are defined per behaviour profile.

**Profile.** A behaviour profile binds a set of states, a decision tree,
and a parameter set. An archetype (e.g. "patrolling guard") is one
profile; an archetype variant (e.g. "off-duty guard") is another profile
that inherits and overrides.

The point of the separation is that you can change an NPC's personality by
swapping profiles without touching state or decision logic, and you can
add a new state without rewriting every archetype's decision tree.

## Limitations

- Nothing here has been performance-tested at scale. The data structures
  are chosen for clarity, not throughput.
- No adversarial player modelling. NPCs react to observations; they do
  not anticipate or strategise.
- No learning or adaptation. Behaviour profiles are authored, not
  trained.
- The decision-tree evaluator is naive — no pruning, no caching, no
  memoisation of observations within a tick.
- If you are looking for a production NPC AI solution, use an
  engine-native behaviour tree or an LLM-driven middleware. This repo is
  for thinking, not shipping.

## License

See `LICENSE`.
