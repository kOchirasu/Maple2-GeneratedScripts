using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004019: Surnuny
/// </summary>
public class _11004019 : NpcScript {
    internal _11004019(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010025$ 
                // - Something's wrong... My fur's standing on end.
                return true;
            case 20:
                // $script:0614185307010026$ 
                // - Something's wrong... My fur's standing on end.
                return true;
            default:
                return true;
        }
    }
}
