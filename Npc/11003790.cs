using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003790: Tristan
/// </summary>
public class _11003790 : NpcScript {
    internal _11003790(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213192607009650$ 
                // - Let's get to business. 
                return true;
            case 10:
                // $script:1213192607009651$ 
                // - ...Finally, the time has come. 
                return true;
            default:
                return true;
        }
    }
}
