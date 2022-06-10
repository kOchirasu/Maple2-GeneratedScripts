using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004559: Mint
/// </summary>
public class _11004559 : NpcScript {
    internal _11004559(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014487$ 
                // - Aaaah.
                return true;
            case 10:
                // $script:0220211107014488$ 
                // - Aaaah.
                // $script:0220211107014489$ 
                // - Oh, hello! I remember you.
                switch (selection) {
                    // $script:0220211107014490$
                    // - Yeah, and I've seen you around.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0220211107014491$ 
                // - I suppose it would be weird if you <i>didn't</i> know who I am.
                // $script:0220211107014492$ 
                // - So, you're here for the Queen Bean Rumble, right? Are you sure you're up to fighting me?
                switch (selection) {
                    // $script:0220211107014493$
                    // - I was about to ask you the same.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0220211107014494$ 
                // - Oh, you think you can take me on just because I dance all day? Well, I have news for you, $male:buddy,female:lady$. Dancing is fantastic exercise. I'm going to crush you like a teeny tiny bug!
                return true;
            default:
                return true;
        }
    }
}
