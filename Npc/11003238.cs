using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003238: Oska
/// </summary>
public class _11003238 : NpcScript {
    internal _11003238(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008129$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0403155707008130$ 
                // - One strange occurrence after another...
                return true;
            default:
                return true;
        }
    }
}
