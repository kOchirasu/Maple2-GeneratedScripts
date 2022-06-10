using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000360: Yosef
/// </summary>
public class _11000360 : NpcScript {
    internal _11000360(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001496$ 
                // - What's wrong?
                return true;
            case 30:
                // $script:0831180407001498$ 
                // - Whew, it sure is hot here! I told my mom that I could make it on my own. Maybe I should've taken $npcName:11000420[gender:1]$'s advice and settled down in $map:02000111$ instead... 
                return true;
            default:
                return true;
        }
    }
}
