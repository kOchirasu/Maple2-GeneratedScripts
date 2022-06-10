using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001033: Vadell
/// </summary>
public class _11001033 : NpcScript {
    internal _11001033(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003533$ 
                // - Cough, cough... Please be careful. 
                return true;
            case 30:
                // $script:0831180407003536$ 
                // - Ugh... I've been holed up in here so long. My head is killing me.
                return true;
            default:
                return true;
        }
    }
}
