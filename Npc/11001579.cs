using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001579: Landevian
/// </summary>
public class _11001579 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0504151707006067$
    // - Ah, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0515180307006121$
                // - This is not going to be easy. 
                return -1;
            case (20, 0):
                // $script:0524142307006215$
                // - This is not going to be easy. 
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
