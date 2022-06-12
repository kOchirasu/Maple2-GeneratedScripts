using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000480: Kaya
/// </summary>
public class _11000480 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002100$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002102$
                // - $npcName:11000328[gender:0]$ has asked us to gather $itemPlural:30000055$ from the quarry in this work cart. I have no idea why he wants useless junk like this.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
