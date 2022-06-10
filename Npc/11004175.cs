using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004175: Girl
/// </summary>
public class _11004175 : NpcScript {
    internal _11004175(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806025707010612$ 
                // - Today is the best day of my life!! 
                return true;
            case 10:
                // $script:0806025707010613$ 
                // - Eek! It's $npcName:11004174[gender:0]$! It's really $npcName:11004174[gender:0]$!! I can't believe it, I think I'm gonna die. 
                return true;
            default:
                return true;
        }
    }
}
