using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001060: Blanche
/// </summary>
public class _11001060 : NpcScript {
    internal _11001060(INpcScriptContext context) : base(context) {
        Id = 60;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180306000373$ 
                // - Do you have business with me?
                return true;
            case 60:
                // $script:0831180306000376$ 
                // - I don't think I'll do business with you, $MyPCName$. I prefer to work with those who have $achieve:23200015$ Trophies. I apologize for any inconvenience.
                return true;
            default:
                return true;
        }
    }
}
