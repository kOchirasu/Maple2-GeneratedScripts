using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004183: Landevian
/// </summary>
public class _11004183 : NpcScript {
    internal _11004183(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010628$ 
                // - Life is such a chore. 
                return true;
            case 10:
                // $script:0806025707010629$ 
                // - Arazaad, Arazaad, Arazaad. Hmph. $npcName:11004182[gender:0]$'s always going on and on about the old man. 
                return true;
            default:
                return true;
        }
    }
}
