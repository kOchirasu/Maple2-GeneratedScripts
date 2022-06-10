using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004026: Bjorn
/// </summary>
public class _11004026 : NpcScript {
    internal _11004026(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010039$ 
                // - ...
                return true;
            case 20:
                // $script:0614185307010040$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
