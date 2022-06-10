using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000603: Degan
/// </summary>
public class _11000603 : NpcScript {
    internal _11000603(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002482$ 
                // - What seems to be the problem?
                return true;
            case 20:
                // $script:0831180407002484$ 
                // - I'll see you soon... my friend...
                return true;
            default:
                return true;
        }
    }
}
