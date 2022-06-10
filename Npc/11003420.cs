using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003420: Tina
/// </summary>
public class _11003420 : NpcScript {
    internal _11003420(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008627$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008628$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}
