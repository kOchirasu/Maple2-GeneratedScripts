using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000007: Ellie
/// </summary>
public class _11000007 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 1:
    // $script:0831180407000026$
    // - What's wrong?
    protected override int Select() => 1;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000029$
                // - Platoon leader of the Green Hoods, at your service. $npcName:11000015[gender:1]$ sent me here to watch over $map:02000146$.
                return -1;
            case (40, 0):
                // $script:0831180407000030$
                // - There's one person whom I admire more than $npc:11000015[gender:1]$, and it's my father. He died of illness when I was young, but the bow he carved for me was my inspiration to join this militia.
                return 40;
            case (40, 1):
                // $script:0831180407000031$
                // - I'll do my best to become a good militia member, so I can believe my father would be proud of me.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
