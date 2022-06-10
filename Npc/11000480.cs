using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000480: Kaya
/// </summary>
public class _11000480 : NpcScript {
    internal _11000480(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002100$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407002102$ 
                // - $npcName:11000328[gender:0]$ has asked us to gather $itemPlural:30000055$ from the quarry in this work cart. I have no idea why he wants useless junk like this.
                return true;
            default:
                return true;
        }
    }
}
