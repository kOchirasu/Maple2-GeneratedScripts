using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000203: Jacob
/// </summary>
public class _11000203 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000884$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000886$
                // - Why do I even bother cutting down trees and chopping firewood? Those sneaky $npcPlural:21090023$ come crawling out of the $map:02000082$ and steal it all, leaving me with nothing to show for my work but sore arms.
                return -1;
            case (30, 0):
                // $script:0831180407000887$
                // - This place used to be a dense forest, and many lumberjacks lived in the cabins here. But then the darkness seeped into Maple World through the shadow gate, rotting the trees from their roots.
                return 30;
            case (30, 1):
                // $script:0831180407000888$
                // - The loggers left, one after another, and this place became a wasteland. After the closing of the Shadow Gate, the last remaining loggers dug out the rotting tree roots and planted new saplings. Now this land is recovering, all thanks to them.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
