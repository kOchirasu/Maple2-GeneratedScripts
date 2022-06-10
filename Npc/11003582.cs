using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003582: Veliche
/// </summary>
public class _11003582 : NpcScript {
    internal _11003582(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1116181907009256$ 
                // - The future is in our hands. 
                return true;
            case 10:
                // $script:1127103307011969$ 
                // - The future is in our hands. 
                return true;
            default:
                return true;
        }
    }
}
