using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003269: Ellie
/// </summary>
public class _11003269 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0403155707008220$
    // - What's wrong?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0403155707008221$
                // - Platoon leader of the Green Hoods, at your service. $npcName:11000015[gender:1]$ sent me here to watch over $map:02000146$.
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
