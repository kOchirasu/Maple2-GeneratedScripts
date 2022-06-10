using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004025: Erda
/// </summary>
public class _11004025 : NpcScript {
    internal _11004025(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010037$ 
                // - ...
                return true;
            case 20:
                // $script:0614185307010038$ 
                // - ...
                return true;
            default:
                return true;
        }
    }
}
