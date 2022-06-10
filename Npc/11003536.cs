using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003536: Nairin
/// </summary>
public class _11003536 : NpcScript {
    internal _11003536(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1126150707011935$ 
                // - Would you like to take on a mission for Green Hoods?
                return true;
            case 20:
                // $script:1126150707011936$ 
                // - How may I help you today, $male:Sir,female:Ma'am$?
                switch (selection) {
                    // $script:1126150707011937$
                    // - Why are Green Hoods here?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1126150707011938$ 
                // - That's a good question! Most people think we're simple rangers and woodswomen, wandering the forests of Henesys with our bows.
                // $script:1126150707011939$ 
                // - But we're so much more than that! We know all about helping people and making sure they have everything they need.
                // $script:1126150707011940$ 
                // - There's more to keeping the peace than simply being a good fighter. You need to know how to treat a wound and provide a shoulder to cry on.
                // $script:1126150707011941$ 
                // - That's why we've been entrusted with support operations on Sky Fortress.
                // $script:1126150707011942$ 
                // - Of course, you know firsthand how good we are in a fight. Even though I'm stationed up here on the bridge, I'm just as good with my bow as Eka!
                return true;
            default:
                return true;
        }
    }
}
