using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000111: John
/// </summary>
public class _11000111 : NpcScript {
    internal _11000111(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000456$ 
                // - What's up? 
                return true;
            case 10:
                // $script:0831180407000457$ 
                // - Aww, I really don't think I can enter $map:02000116$. 
                switch (selection) {
                    // $script:0831180407000458$
                    // - Why?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180407000459$ 
                // - A while back, I followed my uncle who works as a royal porter to the entrance of the forest. I couldn't see more than a few feet in front of me, the underbrush was so thick. Plus it was raining... I never want to go through that again.  
                return true;
            default:
                return true;
        }
    }
}
