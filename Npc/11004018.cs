using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004018: Surnuny
/// </summary>
public class _11004018 : NpcScript {
    internal _11004018(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010023$ 
                // - Hey! I've seen you around Tria! 
                return true;
            case 20:
                // $script:0614185307010024$ 
                // - I'm Surnuny, Tria's best weapons merchant. I came here to trade. 
                return true;
            default:
                return true;
        }
    }
}
