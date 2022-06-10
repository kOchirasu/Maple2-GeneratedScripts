using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001197: Ropey
/// </summary>
public class _11001197 : NpcScript {
    internal _11001197(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1016142906000509$ 
                // - Only those who know the true value of Trophies can appreciate the value I offer.
                return true;
            case 30:
                // $script:1016142906000512$ 
                // - What's this? What business do you have with the Trophy expert? Are you interested in Trophies?
                switch (selection) {
                    // $script:1016142906000513$
                    // - Isn't everyone interested in Trophies?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1016142906000514$
                    // - I don't have time for useless junk like Trophies.
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 31:
                // $script:1016142906000515$ 
                // - Ah, another Trophy connoisseur like myself! If you aspire to be an expert in Trophies like me, you'd better work hard. It'll take you a long time to become as savvy as I!
                switch (selection) {
                    // $script:1016142906000516$
                    // - What do I get if I have a lot of Trophies?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1016142906000517$ 
                // - Hmpf! Collecting Trophies is about more than just what you can get! Of course, there are precious few who collect for the sheer joy of it anymore.
                // $script:1016142906000518$ 
                // - In any case, I have some Trophies, and I'm always looking for more. You can never have enough Trophies, you know! If you happen to find any, I'll trade something equally valuable for them.
                switch (selection) {
                    // $script:1016142906000519$
                    // - Do you even have something equally valuable?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1016142906000520$ 
                // - Of course I do! I've got all kinds of treasures from traveling around Maple World. I can't believe you doubt me.
                return true;
            case 34:
                // $script:1016142906000521$ 
                // - How dare you call my beautiful Trophies junk! Insulting my trophies is like personally insulting me, the Trophy expert! You should be ashamed of yourself for being so insulting!
                switch (selection) {
                    // $script:1016142906000522$
                    // - All right! All right! I'm sorry! I shouldn't have called them junk.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:1016142906000523$ 
                // - Hmpf! I suppose I'll forgive you this time. Not everyone understands the true beauty of Trophies, after all. But don't let it happen again! Trophy experts demand respect, I tell you!
                return true;
            default:
                return true;
        }
    }
}
