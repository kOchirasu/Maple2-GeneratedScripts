using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004052: Allon
/// </summary>
public class _11004052 : NpcScript {
    internal _11004052(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010077$ 
                // - The full might of the empire stands behind the Frontier Foundation. We too will stand against the darkness. 
                return true;
            case 10:
                // $script:0614185307010078$ 
                // - The full might of the empire stands behind the Frontier Foundation. We too will stand against the darkness. 
                return true;
            default:
                return true;
        }
    }
}
