using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004495: Joule 
/// </summary>
public class _11004495 : NpcScript {
    internal _11004495(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012362$ 
                // - The gravity, erm, situation in this place is fascinating. Why, these huge structures look as though they might simply float away.
                return true;
            case 10:
                // $script:1227192907012363$ 
                // - The gravity, erm, situation in this place is fascinating. Why, these huge structures look as though they might simply float away.
                switch (selection) {
                    // $script:1227192907012364$
                    // - How's the research going?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012365$ 
                // - It's early to say, but I think this could lead to a second energy revolution.
                // $script:1227192907012366$ 
                // - Think about it. The vast majority of Sky Fortress's power generation goes into keeping it in the air. How might we use that power if we had aetherine to lift the ship aloft, instead?
                switch (selection) {
                    // $script:0114163707012715$
                    // - That would be incredible.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114163707012716$ 
                // - And that's why we've got to learn everything we can about aetherine.
                return true;
            default:
                return true;
        }
    }
}
