using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001043: Aiden
/// </summary>
public class _11001043 : NpcScript {
    internal _11001043(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003561$ 
                // - This is an emergency. Whatever business you have, it can wait. 
                return true;
            case 30:
                // $script:0831180407003564$ 
                // - Real pros always know what to do, no matter how dire the situation is.
                return true;
            default:
                return true;
        }
    }
}
