using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003878: Mani
/// </summary>
public class _11003878 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0417135107009872$
    // - Welcome to $map:02000425$, the beautiful island of alchemy.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0417135107009873$
                // - Welcome to $map:02000425$, the beautiful island of alchemy.
                return -1;
            case (20, 0):
                // $script:0419172107009857$
                // - Welcome to $map:02000425$, the beautiful island of alchemy.
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
