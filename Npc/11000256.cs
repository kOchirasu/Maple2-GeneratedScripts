using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000256: Ren
/// </summary>
public class _11000256 : NpcScript {
    internal _11000256(INpcScriptContext context) : base(context) {
        Id = 1;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000402$ 
                // - How may I help you? 
                return true;
            case 1:
                // $script:0831180610000406$ functionID=1 
                // - Nothing expresses the inner YOU like carefully-selected cosmetics. How'd you like to experiment with a new look? 
                switch (selection) {
                    // $script:0831180610000407$
                    // - Yep, time to accessorize!
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
