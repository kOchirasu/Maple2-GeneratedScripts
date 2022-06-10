using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000024: Lydia
/// </summary>
public class _11000024 : NpcScript {
    internal _11000024(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000133$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0831180407000136$ 
                // - Have you seen the Royal Road? Or rather, what's left of it? A huge earthquake tore right through it! Everyone who wants to get to $map:02000001$ is stuck here now.
 
                // $script:0831180407000137$ 
                // - $map:02000001$ is so close, and yet so far. Those who came by ship to attend the court are beyond disappointed. That's why we've decided to open the mountain path. To those who are authorized to use it, of course. 
                return true;
            case 40:
                // $script:1215093407009645$ 
                // - Hm? How may I help you? 
                switch (selection) {
                    // $script:1215093407009646$
                    // - What can you tell me about trading airships?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1215093407009647$ 
                // - Oh! Well, there was some kind of new-old technological development that recently opened the skies to trade. Flying boats, what a concept! 
                // $script:1215093407009648$ 
                // - But, from what I've heard, only a fraction of the airships going out ever come back... 
                switch (selection) {
                    // $script:1215093407009649$
                    // - What do you mean by that?
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1215093407009650$ 
                // - The airships vanish into... well, thin air! Once they set off for the skies, they just don't come back. 
                switch (selection) {
                    // $script:1215093407009651$
                    // - Does anyone know what happens to them?
                    case 0:
                        Id = 43;
                        return false;
                }
                return true;
            case 43:
                // $script:1215093407009652$ 
                // - I haven't the faintest idea. Anyway, that's all I know. 
                return true;
            default:
                return true;
        }
    }
}
