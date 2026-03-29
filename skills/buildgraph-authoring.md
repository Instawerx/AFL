# BuildGraph Authoring

## Purpose
Create repeatable Unreal build pipelines without hiding critical steps.

## Minimum graph for AFL
- SyncWorkspace
- ValidateConfig
- ValidateContent
- CompileEditor
- RunFastAutomation
- CookArena01
- PackageClient
- PackageServer
- RunGauntlet_AssaultCore
- RunGauntlet_QueueToReward
- PublishArtifacts

## Procedure
1. Define each node with one clear responsibility.
2. Separate validation, compile, cook/package, and runtime tests.
3. Pass explicit parameters for target, config, platform, and artifact output.
4. Keep repo validation runnable outside of Unreal when possible.

## Example command
```bash
RunUAT.bat BuildGraph -Script=build/buildgraph/AFL_BuildGraph.xml -Target=ValidateContent
```

## Validation
- graph parses
- targets can run independently
- artifact paths are explicit
