using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003448: Tina
/// </summary>
public class _11003448 : NpcScript {
    internal _11003448(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008651$ 
                // - The people need a reason to raise their heads up high.
                return true;
            case 10:
                // $script:0706160807008652$ 
                // - We're all in this together.
                return true;
            default:
                return true;
        }
    }
}
