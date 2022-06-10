using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003165: Frey
/// </summary>
public class _11003165 : NpcScript {
    internal _11003165(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0314104907008094$ 
                // - How do you fare?
                return true;
            case 30:
                // $script:0314104907008097$ 
                // - $npc:11001853[gender:0]$ says there's nothing wrong with you, but I need to be sure. How do you feel?
                switch (selection) {
                    // $script:0314104907008098$
                    // - I'm fine.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0314104907008099$
                    // - I'm a bit sore...
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0314104907008100$ 
                // - Good.
                return true;
            case 32:
                // $script:0314104907008101$ 
                // - Really? We should look into that. I'll have $npc:11001853[gender:0]$ schedule you for some exploratory surgery.
                switch (selection) {
                    // $script:0314104907008102$
                    // - Th-that really isn't necessary!
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:0314104907008103$ 
                // - It's no trouble. After all you did out on the field, this is the least we can do.
                return true;
            case 40:
                // $script:0314104907008104$ 
                // - You were glowing when we found you. How did you do that?
                switch (selection) {
                    // $script:0314104907008105$
                    // - I really don't remember.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0314104907008106$ 
                // - I see. So it wasn't intentional.
                return true;
            default:
                return true;
        }
    }
}
