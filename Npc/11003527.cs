using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003527: Pyrros Fard
/// </summary>
public class _11003527 : NpcScript {
    internal _11003527(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009051$ 
                // - Grrr... 
                return true;
            case 30:
                // $script:0816160115009052$ 
                // - Grrr... 
                return true;
            default:
                return true;
        }
    }
}
