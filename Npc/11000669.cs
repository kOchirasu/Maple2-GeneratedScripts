using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000669: Ronzo
/// </summary>
public class _11000669 : NpcScript {
    internal _11000669(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002718$ 
                // - WHAT?! 
                return true;
            case 30:
                // $script:0831180407002721$ 
                // - What are you doing here? How did you even GET here? 
                switch (selection) {
                    // $script:0831180407002722$
                    // - Easily.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407002723$ 
                // - Kid, I'm impressed. You made it this far, but it's time for you to go. Leave before something bad happens to you.  
                switch (selection) {
                    // $script:0831180407002724$
                    // - Why?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407002725$ 
                // - I stay well away from the basement levels. And I live here! 
                // $script:0831180407002726$ 
                // - I had to come down here today, but believe me... I can't WAIT to get back upstairs. 
                // $script:0831180407002727$ 
                // - Don't try anything stupid. Just get out of here! 
                return true;
            default:
                return true;
        }
    }
}
