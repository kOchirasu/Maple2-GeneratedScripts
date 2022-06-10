using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000098: Deke
/// </summary>
public class _11000098 : NpcScript {
    internal _11000098(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000383$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000386$ 
                // - I'm finding way more $itemPlural:30000011$ here than I did in town. I've almost reached my goal! 
                // $script:0831180407000387$ 
                // - When I have enough money, $npc:11000151[gender:1]$ and I will go attend the court, hand in hand.
It'll be great if we can meet again there, won't it? 
                return true;
            case 40:
                // $script:0809153207007163$ 
                // - I'm finding way more $itemPlural:30000011$ here than I did in town. I've almost reached my goal! 
                return true;
            default:
                return true;
        }
    }
}
