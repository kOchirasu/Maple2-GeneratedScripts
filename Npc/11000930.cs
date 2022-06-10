using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000930: Mocamoca
/// </summary>
public class _11000930 : NpcScript {
    internal _11000930(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003302$ 
                // - I don't trust you humans. Caw!
                return true;
            case 20:
                // $script:0831180407003304$ 
                // - Humans are bad. Caw!
                return true;
            default:
                return true;
        }
    }
}
