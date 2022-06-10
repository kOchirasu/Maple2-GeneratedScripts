using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001680: Bravos
/// </summary>
public class _11001680 : NpcScript {
    internal _11001680(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0629000607006457$ 
                // - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
                return true;
            case 30:
                // $script:0629000607006460$ 
                // - Hm... Did I ever tell you why they call me $npcName:11001680[gender:0]$? I'm sure I told someone, but I can't remember if it was you.
                switch (selection) {
                    // $script:0629000607006461$
                    // - Why do you keep asking that question?
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0629000607006462$
                    // - Let's talk about something else.
                    case 1:
                        Id = 50;
                        return false;
                }
                return true;
            case 40:
                // $script:0629000607006463$ 
                // - You got a problem with that? I'm my own man, and if I want to ask the same question over and over again, you can't stop me. Just for that, I'll tell you again!
                // $script:0629000607006465$ 
                // - They call me Bravos 'cause I'm so great I deserve a standing ovation! I hope you remember this time, 'cause there will be a test!
                // $script:0629000607006466$ 
                // - What, you come here to stare at me? Unless you have something else to say, scram!
                return true;
            case 50:
                // $script:0706165507006640$ 
                // - Yeah, what do you want to talk about?
                switch (selection) {
                    // $script:0706165507006641$
                    // - What was that clone in the video?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:0706165507006642$ 
                // - Beats me. I never saw it before. This is a messed up thought, but could you imagine having 100 $npcNamePlural:11001688[gender:0]$ running around? Ugh, just having one of him is too much.
                return true;
            default:
                return true;
        }
    }
}
