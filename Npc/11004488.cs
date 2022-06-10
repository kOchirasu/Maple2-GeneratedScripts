using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004488: Oranda
/// </summary>
public class _11004488 : NpcScript {
    internal _11004488(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;12
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012293$ 
                // - I'm so glad your here! I needed to share this with someone.
                return true;
            case 10:
                // $script:1227192907012294$ 
                // - I'm so glad your here! I needed to share this with someone.
                switch (selection) {
                    // $script:1227192907012295$
                    // - Oh? What is it?
                    case 0:
                        Id = 11;
                        return false;
                }
                // $script:1227192907012296$ 
                // - Look at that structure up ahead. Really <i>look</i> at it. You can use my telescope if you like.
                switch (selection) {
                    // $script:1227192907012297$
                    // - Yeah, that's... um... something.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012298$ 
                // - The whole thing is made of some kind of porous material, and it's soaked in aetherine like a sponge!
                // $script:1227192907012299$ 
                // - The cylinder at the center looks like it draws aetherine directly from the ground. I think. I'm not exactly sure how it works...
                // $script:1227192907012300$ 
                // - I think this terminal is connected somehow. I haven't managed to get it to do anything yet, though.
                return true;
            default:
                return true;
        }
    }
}
