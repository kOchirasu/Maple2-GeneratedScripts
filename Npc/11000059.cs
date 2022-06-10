using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000059: Oyako
/// </summary>
public class _11000059 : NpcScript {
    internal _11000059(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000261$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407000264$ 
                // - Do you live here? 
                switch (selection) {
                    // $script:0831180407000265$
                    // - Yep!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000266$
                    // - Nope!
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000267$ 
                // - I knew it! I can tell you're from the city by your looks. How much money do you have to make to live in a neighborhood like this? 
                return true;
            case 32:
                // $script:0831180407000268$ 
                // - Oh, no. You look so pale, I-I thought you lived here. I've never been to such a big place before, and everything is so amazing here. And I think I've seen more people today than I've ever seen in my hometown. 
                return true;
            default:
                return true;
        }
    }
}
