using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003644: Ranka
/// </summary>
public class _11003644 : NpcScript {
    internal _11003644(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009150$ 
                // - This data just doesn't add up...
                return true;
            case 10:
                // $script:1109121007009151$ 
                // - Intern? You the intern? I've been waiting!
                switch (selection) {
                    // $script:1109121007009152$
                    // - I think you've got the wrong person.
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009153$ 
                // - The heck I do! I'm too busy trying to making sense of this data to deal with your shenanigans.
                switch (selection) {
                    // $script:1109121007009154$
                    // - If you say so...
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009155$ 
                // - I do, indeed! Now, <i>intern</i>, the first thing you'll want to do is memorize a very special phrase.
                switch (selection) {
                    // $script:1109121007009156$
                    // - Oh? Oh! Yes. I'm listening.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009157$ 
                // - Listen up! "Bolt. Driver. Scale."
                switch (selection) {
                    // $script:1109121007009158$
                    // - Noted.
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009159$ 
                // - That's all for now, intern. But before you go...
                switch (selection) {
                    // $script:1109121007009160$
                    // - Yes?
                    case 0:
                        Id = 15;
                        return false;
                }
                return true;
            case 15:
                // $script:1109121007009161$ 
                // - Would you tell our mutual friend that I need a new assignment? This place is driving me mad.
                switch (selection) {
                    // $script:1109121007009162$
                    // - I'll let her know.
                    case 0:
                        Id = 16;
                        return false;
                }
                return true;
            case 16:
                // $script:1109121007009163$ 
                // - No more data... No more...
                return true;
            default:
                return true;
        }
    }
}
