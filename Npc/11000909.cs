using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000909: Liberation Army Orders
/// </summary>
public class _11000909 : NpcScript {
    internal _11000909(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003269$ 
                // - If you can read this directive, follow the instructions in secret.
                return true;
            case 10:
                // $script:0831180407003270$ 
                // - Access denied. Unauthorized personnel.
                return true;
            case 20:
                // $script:0831180407003271$ 
                // - Unauthorized personnel cannot view this directive.
                return true;
            default:
                return true;
        }
    }
}
