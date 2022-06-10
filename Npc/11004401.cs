using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004401: Marlene
/// </summary>
public class _11004401 : NpcScript {
    internal _11004401(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1213154907011982$ 
                // - Welcome.
                return true;
            case 10:
                // $script:1213154907011983$ 
                // - You have my full support.
                return true;
            default:
                return true;
        }
    }
}
