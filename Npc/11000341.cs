using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000341: Rue
/// </summary>
public class _11000341 : NpcScript {
    internal _11000341(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001367$ 
                // - Did you come to see me?
                return true;
            case 30:
                // $script:0831180407001370$ 
                // - After my family fell, the only thing I had left was the mansion. I decided to forget my former glory as the heiress of House Andrea, and turned the mansion into $map:02000178$. People started to call me $npcName:11000341[gender:1]$ not long after.
                // $script:0831180407001371$ 
                // - $npcName:11000340[gender:0]$ had been the butler for my family as long as I could remember. When my family fell, he stayed behind when everyone else left. Now he's the hotelier of my hotel. I owe him so much.
                return true;
            default:
                return true;
        }
    }
}
