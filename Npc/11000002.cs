using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000002: Rina
/// </summary>
public class _11000002 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407000010$
    // - What's the matter, dear?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407000011$
                // - Now that the court's been canceled, everyone has been clearing out of here. I used to pray for this day to come, but now the city feels so empty.
                return -1;
            case (20, 0):
                // $script:0831180407000012$
                // - Welcome, $MyPCName$. I was just about done with this batch of cookies. Would you like to wait for them? My fresh-baked cookies are famous here in $map:02000001$, you know.
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
