# EOS Lobby Session Flow

## Purpose
Define how players move from menu to lobby to live match.

## Session classes
- PublicCompetitive
- PrivateLobby
- SkillsChallenge
- SpectatorOnly
- InternalTest

## Procedure
1. Create or join lobby.
2. Ready-check all members.
3. Create EOS session with correct class and metadata.
4. Hand players off to server.
5. Track reconnect token or equivalent session context.
6. Return to menu cleanly after match resolution.

## Validation
- wrong session class cannot receive full payouts
- private sessions are distinguishable from public sessions
- reconnect path is documented
