using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000285: Torhara
/// </summary>
public class _11000285 : NpcScript {
    internal _11000285(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001114$ 
                // - What brings you here? 
                return true;
            case 30:
                // $script:0831180407001117$ 
                // - Is there someone you love? 
                switch (selection) {
                    // $script:0831180407001118$
                    // - Yes.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407001119$
                    // - No.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407001120$ 
                // - Good for you. Cherish them while you can. Have you ever lost someone you love? 
                switch (selection) {
                    // $script:0831180407001121$
                    // - Yes.
                    case 0:
                        Id = 33;
                        return false;
                    // $script:0831180407001122$
                    // - No.
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407001123$ 
                // - I see. Sometimes love begets tragedy, but it's worth more than the pain.  
                return true;
            case 33:
                // $script:0831180407001124$ 
                // - I see. I daresay I understand your pain.  
                return true;
            case 34:
                // $script:0831180407001125$ 
                // - I see. Let me give you some advice. Never take the ones you love for granted.  
                return true;
            default:
                return true;
        }
    }
}
