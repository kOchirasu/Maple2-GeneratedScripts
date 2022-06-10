using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000350: Jeremy
/// </summary>
public class _11000350 : NpcScript {
    internal _11000350(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001460$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180407001462$ 
                // - I've been traveling all my life, and the greatest lesson I've learned is to never waste anything. $npcName:21000029$, for example, has hundreds of practical uses. It's amazing stuff!
                return true;
            default:
                return true;
        }
    }
}
