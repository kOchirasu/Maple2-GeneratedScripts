using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000635: Prisoner 140918
/// </summary>
public class _11000635 : NpcScript {
    internal _11000635(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002582$ 
                // - Get me out of here... 
                return true;
            case 30:
                // $script:0831180407002585$ 
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:0831180407002586$
                    // - How did you end up in here?
                    case 0:
                        Id = 31;
                        return false;
                }
                // $script:0831180407002588$ 
                // - Ugh... This smell... The toilet is clogged...
                return true;
            case 31:
                // $script:0831180407002587$ 
                // - For swearing. Why? Don't say you never swear. Everyone does it! So why is it such a crime??
                return true;
            default:
                return true;
        }
    }
}
