using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001031: Chano
/// </summary>
public class _11001031 : NpcScript {
    internal _11001031(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003525$ 
                // - Ugh... 
                return true;
            case 30:
                // $script:0831180407003528$ 
                // - $npcName:11000335[gender:0]$... Sigh... I don't know what to tell you about him... 
                return true;
            default:
                return true;
        }
    }
}
