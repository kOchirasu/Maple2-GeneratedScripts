using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001342: Venchas
/// </summary>
public class _11001342 : NpcScript {
    internal _11001342(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005288$ 
                // - Sigh... This is getting tiring... 
                return true;
            case 30:
                // $script:1217012607005291$ 
                // - You can't swat a bug in the water, but you can still spray it. 
                return true;
            default:
                return true;
        }
    }
}
