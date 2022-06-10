using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003203: Joddy
/// </summary>
public class _11003203 : NpcScript {
    internal _11003203(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0518141907008520$ 
                // - Training to be a guard is tough. 
                return true;
            case 10:
                // $script:0518141907008521$ 
                // - Huh...? Who is this small friend? 
                return true;
            default:
                return true;
        }
    }
}
