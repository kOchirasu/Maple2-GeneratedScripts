using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004513: Mannstad Gunner
/// </summary>
public class _11004513 : NpcScript {
    internal _11004513(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228182607012469$ 
                // - My bullets always hit their mark!
                return true;
            case 10:
                // $script:1228182607012470$ 
                // - My bullets always hit their mark!
                return true;
            default:
                return true;
        }
    }
}
