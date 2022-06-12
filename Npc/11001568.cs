using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001568: Ishura
/// </summary>
public class _11001568 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0504151707006056$
    // - Ah, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006111$
                // - We can't give up yet. There's still so much to do!
                return -1;
            case (20, 0):
                // $script:0524142307006212$
                // - We can't give up yet. There's still too much to do!
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
