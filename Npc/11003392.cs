using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003392: Last of the Vayar
/// </summary>
public class _11003392 : NpcScript {
    internal _11003392(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008589$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008590$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}