using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000153: Gina
/// </summary>
public class _11000153 : NpcScript {
    internal _11000153(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000652$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000655$ 
                // - Not right now, I'm power-walking.
                return true;
            default:
                return true;
        }
    }
}
