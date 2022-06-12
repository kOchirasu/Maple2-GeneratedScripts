using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003202: Joddy
/// </summary>
public class _11003202 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0404083307008230$
    // - Jeez, who knew being a guard would be so tough?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0404083307008231$
                // - I'm learning so much just from standing in the same room as you, $MyPCName$.
                return -1;
            case (20, 0):
                // $script:0518141907008519$
                // - $MyPCName$! Something terrible has happened!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
