using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001233: Rejan
/// </summary>
public class _11001233 : NpcScript {
    internal _11001233(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1125194807004478$ 
                // - Ugh... 
                return true;
            case 30:
                // $script:1125194807004481$ 
                // - Ugh... I was injured by a trap, and $npc:11001244[gender:0]$ ran on ahead on his own. 
                switch (selection) {
                    // $script:1205222707004732$
                    // - What happened?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1205222707004733$ 
                // - We tracked $npcName:11001231[gender:0]$ and his Jibricia followers here, but they had already filled the passage with traps. I'm worried $npcName:11001244[gender:0]$ might be in danger. 
                return true;
            default:
                return true;
        }
    }
}
