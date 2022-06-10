using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001281: Ishura
/// </summary>
public class _11001281 : NpcScript {
    internal _11001281(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1211023307004972$ 
                // - Hm... Wait.
                return true;
            case 30:
                // $script:1209020507004851$ 
                // - I don't understand him... I really don't...
                return true;
            default:
                return true;
        }
    }
}
