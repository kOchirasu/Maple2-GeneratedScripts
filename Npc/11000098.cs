using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000098: Deke
/// </summary>
public class _11000098 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407000383$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000386$
                // - I'm finding way more $itemPlural:30000011$ here than I did in town. I've almost reached my goal!
                return 30;
            case (30, 1):
                // $script:0831180407000387$
                // - When I have enough money, $npc:11000151[gender:1]$ and I will go attend the court, hand in hand.
                //   It'll be great if we can meet again there, won't it?
                return -1;
            case (40, 0):
                // $script:0809153207007163$
                // - I'm finding way more $itemPlural:30000011$ here than I did in town. I've almost reached my goal!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
