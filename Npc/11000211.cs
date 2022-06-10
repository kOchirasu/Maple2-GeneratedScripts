using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000211: Zeta
/// </summary>
public class _11000211 : NpcScript {
    internal _11000211(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000897$ 
                // - What do you want?
                return true;
            case 20:
                // $script:0831180407000899$ 
                // - What? Stop bothering me. Don't you have anything better to do?
                return true;
            default:
                return true;
        }
    }
}
