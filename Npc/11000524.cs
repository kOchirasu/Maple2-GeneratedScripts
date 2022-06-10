using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000524: Nick
/// </summary>
public class _11000524 : NpcScript {
    internal _11000524(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002243$ 
                // - What is it?
                return true;
            case 20:
                // $script:0831180407002245$ 
                // - Don't sweat it. Crime is pretty bad around here. That's just how it is.
                return true;
            default:
                return true;
        }
    }
}
