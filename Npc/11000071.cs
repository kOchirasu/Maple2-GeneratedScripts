using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000071: Dixon
/// </summary>
public class _11000071 : NpcScript {
    internal _11000071(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000379$ 
                // - What seems to be the problem? 
                return true;
            case 1:
                // $script:0831180610000383$ functionID=1 
                // - Oooh, $MyPCName$, I'm so glad you found me. I can work miracles! Everyone says so. Now, what did you have in mind? 
                switch (selection) {
                    // $script:0831180610000384$
                    // - Show me the possibilities.
                    case 0:
                        Id = 0;
                        return false;
                }
                return true;
            default:
                return true;
        }
    }
}
