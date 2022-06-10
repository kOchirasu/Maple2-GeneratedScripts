using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004174: Blake
/// </summary>
public class _11004174 : NpcScript {
    internal _11004174(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010610$ 
                // - You don't have to look twice. I'm who you think I am. 
                return true;
            case 10:
                // $script:0806025707010611$ 
                // - You're lucky to have run into me. I'm not sticking around, I've just popped in for a photo shoot. I can't really have a relaxing vacation with so many frenzied fans around. 
                return true;
            default:
                return true;
        }
    }
}
