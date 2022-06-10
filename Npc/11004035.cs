using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004035: Orde
/// </summary>
public class _11004035 : NpcScript {
    internal _11004035(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010055$ 
                // - It's not like I want to be here. But I've got a debt to repay.
                return true;
            case 20:
                // $script:0614185307010056$ 
                // - It's not like I want to be here. But I've got a debt to repay.
                return true;
            default:
                return true;
        }
    }
}
