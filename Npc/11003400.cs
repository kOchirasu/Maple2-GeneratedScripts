using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003400: Rovey
/// </summary>
public class _11003400 : NpcScript {
    internal _11003400(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0621181107008568$ 
                // - Focus on your training.
                return true;
            case 10:
                // $script:0621181107008569$ 
                // - Willpower alone does not make you a knight.
                return true;
            default:
                return true;
        }
    }
}
