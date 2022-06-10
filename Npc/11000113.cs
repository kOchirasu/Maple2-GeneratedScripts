using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000113: Shogi
/// </summary>
public class _11000113 : NpcScript {
    internal _11000113(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000467$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407000470$ 
                // - $MyPCName$, are you here to make a buck too?
                switch (selection) {
                    // $script:0831180407000471$
                    // - Why would I want to make money?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0831180407000472$
                    // - How can I make money here?
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000473$ 
                // - Oh, you didn't hear? The empress has called for an open court. If you want to get to the mainland to see it, you'll need a lot of money.
                return true;
            case 32:
                // $script:0831180407000474$ 
                // - Well, I usually check the boxes and jars laying around the village. You can find all kinds of cash or stuff to sell in 'em.
                // $script:0831180407000475$ 
                // - If you want to make money quickly, you can always gather clams at $map:63000002$ over there. I've heard some of them hide expensive pearls and starfish.
                // $script:0831180407000476$ 
                // - Be careful, though. Monsters are milling about the beach. I'd rather make money slowly than be beaten up by those things.
                return true;
            default:
                return true;
        }
    }
}
