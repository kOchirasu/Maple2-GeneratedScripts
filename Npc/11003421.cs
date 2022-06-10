using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003421: Evagor
/// </summary>
public class _11003421 : NpcScript {
    internal _11003421(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008629$ 
                // - Don't waste my time. $map:02000051$ doesn't need the likes of you. 
                return true;
            case 10:
                // $script:0706160807008630$ 
                // - You want to stay here? You gotta take the warrior's test. 
                return true;
            default:
                return true;
        }
    }
}
