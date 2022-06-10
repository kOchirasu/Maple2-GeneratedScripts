using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000405: Dark Wind Bulletin
/// </summary>
public class _11000405 : NpcScript {
    internal _11000405(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001640$ 
                // - This is the Dark Wind Bulletin Board. 
                return true;
            case 10:
                // $script:0831180407001641$ 
                // - Eliminate $npcName:29000023$ and bring me proof for your reward.

- Captain $npcName:11000044[gender:0]$ 
                return true;
            default:
                return true;
        }
    }
}
