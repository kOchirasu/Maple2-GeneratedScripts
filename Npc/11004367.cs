using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004367: Mia
/// </summary>
public class _11004367 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109213607011779$
    // - You know how hard I work, but even I need a break.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109213607011780$
                // - Working is intensely satisfying. And it also makes my rest hours that much sweeter.
                return 10;
            case (10, 1):
                // $script:1120173007011854$
                // - $MyPCName$, take care of yourself this season. Happy holidays!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
