using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000203: Jacob
/// </summary>
public class _11000203 : NpcScript {
    internal _11000203(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000884$ 
                // - What is it? 
                return true;
            case 20:
                // $script:0831180407000886$ 
                // - Why do I even bother cutting down trees and chopping firewood? Those sneaky $npcPlural:21090023$ come crawling out of the $map:02000082$ and steal it all, leaving me with nothing to show for my work but sore arms. 
                return true;
            case 30:
                // $script:0831180407000887$ 
                // - This place used to be a dense forest, and many lumberjacks lived in the cabins here. But then the darkness seeped into Maple World through the shadow gate, rotting the trees from their roots. 
                // $script:0831180407000888$ 
                // - The loggers left, one after another, and this place became a wasteland. After the closing of the Shadow Gate, the last remaining loggers dug out the rotting tree roots and planted new saplings. Now this land is recovering, all thanks to them. 
                return true;
            default:
                return true;
        }
    }
}
