using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004046: Surnuny
/// </summary>
public class _11004046 : NpcScript {
    internal _11004046(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010065$ 
                // - The king will come back... He just has to! 
                return true;
            case 10:
                // $script:0614185307010066$ 
                // - The king will come back... He just has to! 
                return true;
            default:
                return true;
        }
    }
}
