using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001277: Krend
/// </summary>
public class _11001277 : NpcScript {
    internal _11001277(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1208175407004832$ 
                // - Shush! You'll scare them off.
                return true;
            case 30:
                // $script:1208175407004835$ 
                // - Sorry, but now isn't a good time. As you can see, I'm busy.
                switch (selection) {
                    // $script:1208175407004836$
                    // - What are you up to?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1208175407004837$ 
                // - I'm collecting special materials. I'm a specialist in restoring old documents, antiques, and what have you. The secretions of the $npcNamePlural:21000074$ are important in my line of work. 
                return true;
            default:
                return true;
        }
    }
}
