using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000255: Rosetta
/// </summary>
public class _11000255 : NpcScript {
    internal _11000255(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000397$ 
                // - How may I help you?
                return true;
            case 1:
                // $script:0831180610000400$ functionID=1 
                // - $MyPCName$, how shall we style your hair today? Anything you like, just say the word.
                switch (selection) {
                    // $script:0831180610000401$
                    // - Anything? Really? Well, in that case...
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
