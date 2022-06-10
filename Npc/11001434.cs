using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001434: Pardore
/// </summary>
public class _11001434 : NpcScript {
    internal _11001434(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1216230507005197$ 
                // - They have to be around here somewhere.
                return true;
            case 40:
                // $script:1216230507005201$ 
                // - It's peaceful out here, isn't it? Of course, it'd be more peaceful without all the monsters.
                switch (selection) {
                    // $script:1216230507005202$
                    // - What can you tell me about the place?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1216230507005203$ 
                // - Minar Desert used to be the home of the dragons, or so they say. Whether or not that's true, there are plenty of legends about this place... Such as the legend of the sacred tribe.
                switch (selection) {
                    // $script:1216230507005204$
                    // - What sacred tribe?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1216230507005205$ 
                // - Do you know about the snow leopards? There are only a few of them. The younger leopards look human, but as they grow, so does their sacred power. They grow bestial and lose the ability to speak. They're no ordinary spirits; some believe they're closer to gods.
                switch (selection) {
                    // $script:1216230507005206$
                    // - Have you ever seen a snow leopard?
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:1216230507005207$ 
                // - I caught a glimpse of one once. Of course, most folks think I dreamed it, but I know that's not true. I'm determined to uncover the secret of the snow leopards. 
                return true;
            default:
                return true;
        }
    }
}
