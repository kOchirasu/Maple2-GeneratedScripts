using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004020: Junta
/// </summary>
public class _11004020 : NpcScript {
    internal _11004020(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010027$ 
                // - To think I'd be stuck here, useless...
                return true;
            case 20:
                // $script:0614185307010028$ 
                // - To think I'd be stuck here, useless...
                return true;
            default:
                return true;
        }
    }
}
