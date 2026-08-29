---
layout: default
title: Core Rules
subtitle: The rules presented here are all you need to play your first match
---
current version: v{{site.version}}

* TOC
{:toc}

## Introduction

#### Components
To play a match of Dash Bowl, you will need a hexagonal grid board (12 x 19) with a 12-space bounce/scatter template.
You can also try playing on a Blood Bowl Sevens or Blitz Bowl pitch; in that case, use a D8 or D16 for scatters.

A D12 die.
You can also try using 2xD6 for test rolls and a D6 for scatters.

A ball and two teams (miniatures, team roster sheet, and optionally an action deck if you are testing that rule).

#### Teams
The team sheet describes the team, specifying the number of players at each position as well as their stats.
Each player has the following characteristics:
- **Position**: The player's role; miniatures should make it easy to identify each player's position. Position can affect certain cards or team talents.
- **Movement** (M [3-9]): More than just the distance moved, this corresponds to the number of action points available during an activation. Certain actions require multiple movement points.
- **Throw** (T [4-10+]): The player's ability to complete a pass.
- **Block** (B [4-10+]): The player's ability to block or tackle an opponent.
- **Armor** (A [4-10+]): Represents mass, durability, and agility. The player's ability to stay on their feet after a block.

#### Starting the Match
The home team starts the game on defense; the away team kicks off and takes the first turn. You can flip a coin for friendly matches.

Each coach/team then alternates turns, activating their players one by one. The activation order is crucial because if an action fails, the team's turn ends immediately — this is a turnover.

## Glossary
- **Player**: A miniature on the pitch.
- **Coach**: The person moving the miniatures.
- **Standing Player**: A player who is not prone / knocked down.
- **Open Player**: A standing player who has no adjacent standing opposing players.
- **Marked Player**: A standing player who has at least one adjacent standing opposing player.
- **Multi-Marked Player**: A marked player who has at least two adjacent standing opposing players.
- **Prone Player**: A player on the ground can only stand up during their activation.
  A player knocked down must immediately drop the ball (see Scatter / Bounce).
- **KO Player**: Removed from the pitch until the next touchdown.
- **Bounce / Scatter**: The ball is moved to a randomly determined space among the 12 spaces surrounding the bounce point (the 6 adjacent spaces and 6 others at distance 2). If the ball lands on an open player, they catch it.
  If the ball lands on a marked or prone player, it bounces again.
  If the ball would land off the pitch or onto an obstacle, it bounces to the opposite space.
- **Pass Roll, Block Roll, Armor Roll**: The active player's coach rolls a D12 and adds any applicable modifiers. If the result is greater than or equal to the player's corresponding stat, it is a success. Otherwise, it is a failure and the active player's activation ends. Effects are detailed in the relevant sections.
- **Fumble / Blunder**: If a roll results in a natural 1 or 2, or <= 2 after modifiers, the player commits a fumble.
- **Turnover**: After a fumble by the active player, their team's turn ends immediately even if not all players have been activated.


## Kickoff Turn (Turn 0)
The defending team places its players within 5 spaces or fewer of its own touchdown line.

The attacking team places its players on its touchdown line, gives the ball to one of them, and then activates them normally.

## Standard Turns
Standard turns all follow the same sequence:
The defending team plays by activating its players one by one, then the attacking team does the same.

Activating a player allows them to perform the following actions, up to their Movement stat allowance:

#### Run (Open player — 1M)
Move the open player 1 space; the player must still be open after this move.

#### Mark (Open player — 2M)
Move the open player 1 space into an opposing player's marking zone.

#### Pass (Open player — Once per turn per team, 1M + Throw roll)
An open player can spend 1M to attempt a pass to a teammate receiver.
- 1 space & open receiver: Automatic success
- <= 4 spaces: Throw roll
- <= 8 spaces: Throw roll -1
- Marked receiver: -1 per marking opponent

Results:
- **Fumble**: The ball scatters around the thrower. Turnover.
- **Failure**: The ball scatters around the target. The active player and the receiver cannot be activated again this turn.
- **Success**: The ball lands safely in the receiver's hands.

#### Pick Up the Ball (Open / Marked player — 1M)
If during their activation, an open or marked player is in the same space as the ball, they can spend 1 movement point to pick it up.

If they choose not to, the ball bounces.

If the player is marked, they must make an Armor roll (-1 per additional opponent marking them):
- **Fumble**: The active player is knocked down. The ball bounces. Turnover.
- **Failure**: The ball bounces. End of activation.
- **Success**: The ball is safely in the active player's hands.

#### Dodge / Disengage (Marked player — 2M)
Move the marked player 1 space.

Unless marked exclusively by multi-marked opponents, the player must make an Armor roll with -1 per additional opponent marking them:
- **Fumble**: The player is knocked down. Turnover.
- **Failure**: The player is knocked down.
- **Success**: The player remains standing and can continue their activation normally.

#### Block (Marked player — 2M + Block roll)
A marked player can spend 2 movement points to attempt a block on an adjacent opposing player they are marking.
The active player's coach makes a Block roll with the following modifiers:
- +1 for each teammate marking the defender.
- -1 for each opponent marking the active player.

Results:
- **Fumble**: The active player is knocked down. Turnover.
- **Failure**: Nothing happens. The active player's activation ends.
- **Success**: The defending player must make an Armor roll. If they had the ball, it bounces:
  - -1 for each player marking the defender.
  - +1 for each player marking the active player.

  Armor roll results:
  - **Fumble**: The defender is KO.
  - **Failure**: The defender is knocked down (prone).
  - **Success**: The active player's coach chooses to push the defending player into one of the 3 opposite empty spaces. If not possible, the defender is knocked down.
  The active player may advance for free into the space previously occupied by the defending player.

#### Stand Up (Prone player — Full activation action)
A prone player (not KO) at the start of the turn can stand up. They cannot perform any other action during this activation.
If marked, they must make an Armor roll:
- **Fumble**: The player is KO. Turnover.
- **Failure**: The player remains prone.
- **Success**: The player stands up.

## Touchdown
As soon as a player in possession of the ball enters the opponent's touchdown zone, the turn ends and their team scores 1 point.
A new kickoff takes place (as in Turn 0). The team that just scored is now the defending team.

## End of Match
Match end conditions should be agreed upon. Two possible options:
- The match ends after 12 full turns.
- The match ends as soon as a team scores 3 touchdowns.

