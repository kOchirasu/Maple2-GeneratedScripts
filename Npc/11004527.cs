using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004527: Richard
/// </summary>
public class _11004527 : NpcScript {
    internal _11004527(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0103163407012512$ 
                // - Oh?!
                return true;
            case 40:
                // $script:0104140207012578$ 
                // - Aaaah.
                return true;
            case 10:
                // $script:0103163407012513$ 
                // - Ah... Hello there.
                switch (selection) {
                    // $script:0103163407012514$
                    // - How's the research going?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0103163407012515$ 
                // - V-very well. As you can see, I'm burning the midnight oil. Eheheh...
                // $script:0103163407012516$ 
                // - If you could see our results, why, they'd knock your socks off!
                // $script:0103163407012517$ 
                // - S-so you go and tell $npcName:11004438[gender:0]$ that we're working hard, okay?
                switch (selection) {
                    // $script:0103163407012518$
                    // - It doesn't look like you're working <i>that</i> hard.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0103163407012519$ 
                // - I-I am, and I have the overtime sheets to show it! L-later. I'll have them later. You'll see...
                return true;
            case 50:
                // $script:0104140207012579$ 
                // - Isn't this place lovely? I get to enjoy this wonderful nature while I work.
                switch (selection) {
                    // $script:0104140207012580$
                    // - I see the "enjoy" part, but what about the "work" part?
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:0104140207012581$ 
                // - I can't help it if I have resting "relaxed" face. Trust me when I say that we're working hard over here.
                return true;
            default:
                return true;
        }
    }
}
