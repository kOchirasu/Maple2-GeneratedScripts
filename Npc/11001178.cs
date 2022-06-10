using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001178: Charky
/// </summary>
public class _11001178 : NpcScript {
    internal _11001178(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1012113807004098$ 
                // - You rotten swine, I won't let you get away with this!
                return true;
            case 30:
                // $script:1012113807004101$ 
                // - Do you know what it's like to see your life's work destroyed in a single day? Well I do! <b>I've lost my farm<b>! Gah! I'm so mad I can't even sleep at night.
                switch (selection) {
                    // $script:1012113807004102$
                    // - What happened?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1012113807004103$ 
                // - At first I saw them in the distance, like a tidal wave. Before I knew it, my farm was blanketed by a horde of pigs! They crashed through my farm, trampling everything, leaving only ruin! I couldn't believe my eyes...
                return true;
            default:
                return true;
        }
    }
}
