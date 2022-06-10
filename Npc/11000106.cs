using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000106: Cecilia
/// </summary>
public class _11000106 : NpcScript {
    internal _11000106(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000433$ 
                // - What? 
                return true;
            case 30:
                // $script:0831180407000436$ 
                // - Don't talk to me. 
                return true;
            case 40:
                // $script:0831180407000437$ 
                // - Eww. Stranger danger! 
                return true;
            case 50:
                // $script:1215101207009666$ 
                // - What? 
                // $script:1215101207009667$ 
                // - Don't talk to me. 
                switch (selection) {
                    // $script:1215101207009668$
                    // - What can you tell me about trading airships?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1215101207009669$ 
                // - Airships? I don't know anything about that. 
                switch (selection) {
                    // $script:1215101207009670$
                    // - Are you sure you haven't heard <i>ANYTHING</i>?
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1215101207009671$ 
                // - Ugh, how annoying. That weird guy from earlier was asking the same questions. 
                switch (selection) {
                    // $script:1215101207009672$
                    // - I'm going to keep bothering you until you talk to me...
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:1215101207009673$ 
                // - Ugh! Fine! There are some rumors flying around about airships going missing, but I don't remember any of the details because they were boring.  
                // $script:1215101207009674$ 
                // - I don't even know if they're the same airships you're talking about, just that some have supposedly gone missing. There, are you happy? 
                switch (selection) {
                    // $script:1215101207009675$
                    // - Thanks. You've been a <i>biiig</i> help.
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            case 54:
                // $script:1215101207009676$ 
                // - Don't act like we're friends now. 
                return true;
            default:
                return true;
        }
    }
}
