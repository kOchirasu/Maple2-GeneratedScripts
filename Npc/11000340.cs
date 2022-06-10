using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000340: Zobek
/// </summary>
public class _11000340 : NpcScript {
    internal _11000340(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001360$ 
                // - What can I do for you?
                return true;
            case 30:
                // $script:0831180407001363$ 
                // - I've been by $npcName:11000341[gender:1]$'s side since she was born. It's the least I could do to repay her grandfather, who took me under his wing when I had no place to go.
                return true;
            case 40:
                // $script:0831180407001364$ 
                // - If the Andreas hadn't fallen so easily, this $map:02000178$ would not be here today. 
                switch (selection) {
                    // $script:0831180407001365$
                    // - What happened to the Andreas?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407001366$ 
                // - T-that's... Ah, let's not stir up old, painful memories.
                return true;
            default:
                return true;
        }
    }
}
