using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000174: Broonie
/// </summary>
public class _11000174 : NpcScript {
    internal _11000174(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000728$ 
                // - Can I help you? 
                return true;
            case 20:
                // $script:0831180407000730$ 
                // - Excuse me, but could you take $npcName:11000170[gender:0]$ with you? I've got things to do, and he keeps bothering me with some nonsense about love. I'm fine being friends, but that's it! 
                return true;
            default:
                return true;
        }
    }
}
