using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003396: Kipas Karr
/// </summary>
public class _11003396 : NpcScript {
    internal _11003396(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0706160807008597$ 
                // - 
                return true;
            case 10:
                // $script:0706160807008598$ 
                // - 
                return true;
            default:
                return true;
        }
    }
}
