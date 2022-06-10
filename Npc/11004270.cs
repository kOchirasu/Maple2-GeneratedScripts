using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004270: Rainy
/// </summary>
public class _11004270 : NpcScript {
    internal _11004270(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011230$ 
                // - ...
                return true;
            case 10:
                // $script:0911203207011231$ 
                // - ...
                // $script:0911203207011232$ 
                // - Stop stomping around so loudly! You're giving me away!
                switch (selection) {
                    // $script:0911203207011233$
                    // - Sorry. What're you up to?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011234$ 
                // - Isn't it obvious? I'm observing! This data is gonna be used in an amazing research paper I'm gonna write.
                switch (selection) {
                    // $script:0911203207011235$
                    // - Sure, but what's with the disguise?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0911203207011236$ 
                // - Look around! The ecosystem here is an impossible combination of nature and machine. There's so much we don't know about this place.
                // $script:0911203207011237$ 
                // - Now add in my disguise, and the answer to your question should be obvious, right?
                switch (selection) {
                    // $script:0911203207011238$
                    // - I still don't get it.
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0911203207011239$ 
                // - Ugh, use your brain! I'm conducting <b>monster research</b>! I'm in costume so they don't flee or attack. Obviously.
                // $script:0911203207011240$ 
                // - Now that I've answered your question, can you run along? I haven't moved from this spot for a week, and the last thing I want is for you to ruin my research!
                return true;
            default:
                return true;
        }
    }
}
