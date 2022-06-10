using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004023: Erda
/// </summary>
public class _11004023 : NpcScript {
    internal _11004023(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010033$ 
                // - I'm so very sorry...
                return true;
            case 20:
                // $script:0614185307010034$ 
                // - I'm so very sorry...
                return true;
            default:
                return true;
        }
    }
}
