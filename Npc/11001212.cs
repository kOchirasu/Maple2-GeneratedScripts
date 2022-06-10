using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001212: 
/// </summary>
public class _11001212 : NpcScript {
    internal _11001212(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1022122006000527$ 
                // - Looking for something? I can get you nearly anything for the right price. 
                return true;
            case 30:
                // $script:1022122006000530$ 
                // - Feel free to browse. I've got products you can't find anywhere else. 
                switch (selection) {
                    // $script:1022122006000531$
                    // - That's a unique accent. May I ask where you're from?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1022122006000532$ 
                // - Ah, you've certainly got keen ears. You're the first to notice since I arrived. 
                switch (selection) {
                    // $script:1022122006000533$
                    // - And you arrived from... ?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1022122006000534$ 
                // - Nowhere you've heard of. Just a faraway place across the ocean. Actually, have you met anyone from the Allicari Merchant Society in $map:2000064$? The people who can't stop yelling yalario! 
                switch (selection) {
                    // $script:1022122006000535$
                    // - I don't think so...
                    case 0:
                        Id = 33;
                        return false;
                    // $script:1022122006000536$
                    // - Yes.
                    case 1:
                        Id = 35;
                        return false;
                }
                return true;
            case 33:
                // $script:1022122006000537$ 
                // - Ah, lucky you! If you do, be careful. They can be pretty heartless. 
                switch (selection) {
                    // $script:1022122006000538$
                    // - What do you mean?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1022122006000539$ 
                // - They called me a stowaway and kicked me off their ship just because I couldn't afford the fare. It's not like the ship would sink just because of one extra person. How could they be so cruel? 
                switch (selection) {
                    // $script:1022122006000540$
                    // - But if you couldn't afford the fare...
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 35:
                // $script:1022122006000541$ 
                // - Can you believe how heartless they are? You know they called me a stowaway and kicked me off their ship just because I couldn't afford the fare? They're so mean! 
                switch (selection) {
                    // $script:1022122006000542$
                    // - But if you couldn't afford the fare...
                    case 0:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:1022122006000543$ 
                // - WHAT?! You're taking their side! You're as heartless as they are! 
                return true;
            default:
                return true;
        }
    }
}
