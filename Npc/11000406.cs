using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000406: Blake
/// </summary>
public class _11000406 : NpcScript {
    internal _11000406(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001642$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407001644$ 
                // - Sometimes I'm afraid to look in the mirror. 
                switch (selection) {
                    // $script:0831180407001645$
                    // - Why?
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0831180407001646$ 
                // - I might fall in love with myself! 
                switch (selection) {
                    // $script:0831180407001647$
                    // - But I'm already in love with you!
                    case 0:
                        Id = 22;
                        return false;
                    // $script:0831180407001648$
                    // - I'm just gonna pretend I didn't hear that.
                    case 1:
                        Id = 23;
                        return false;
                }
                return true;
            case 22:
                // $script:0831180407001649$ 
                // - I know how difficult it is to resist my incredible charms. Don't hate me because I can't love you in return. 
                return true;
            case 23:
                // $script:0831180407001650$ 
                // - Hey, hey! What are you looking at? Look at me! Hello! Hey, can't you hear me? 
                return true;
            default:
                return true;
        }
    }
}
