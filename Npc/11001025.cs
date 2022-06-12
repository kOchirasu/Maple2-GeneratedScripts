using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001025: Eve
/// </summary>
public class _11001025 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003479$
    // - Ah... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003482$
                // - It's not over until we catch $npcName:11000044[gender:0]$. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
