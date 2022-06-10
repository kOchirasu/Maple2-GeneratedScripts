using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001301: Ereve
/// </summary>
public class _11001301 : NpcScript {
    internal _11001301(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005018$ 
                // - $MyPCName$, what brings you to me? 
                return true;
            case 10:
                // $script:1215203907005019$ 
                // - Were it not for the lumarigons, we would not have defeated the Demon King. We must go to Drachenheim's aid. 
                return true;
            default:
                return true;
        }
    }
}
