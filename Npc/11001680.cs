using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001680: Bravos
/// </summary>
public class _11001680 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629000607006457$
    // - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0629000607006460$
                // - Hm... Did I ever tell you why they call me $npcName:11001680[gender:0]$? I'm sure I told someone, but I can't remember if it was you.
                switch (selection) {
                    // $script:0629000607006461$
                    // - Why do you keep asking that question?
                    case 0:
                        return 40;
                    // $script:0629000607006462$
                    // - Let's talk about something else.
                    case 1:
                        return 50;
                }
                return -1;
            case (40, 0):
                // $script:0629000607006463$
                // - You got a problem with that? I'm my own man, and if I want to ask the same question over and over again, you can't stop me. Just for that, I'll tell you again!
                return 40;
            case (40, 1):
                // $script:0629000607006465$
                // - They call me Bravos 'cause I'm so great I deserve a standing ovation! I hope you remember this time, 'cause there will be a test!
                return 40;
            case (40, 2):
                // $script:0629000607006466$
                // - What, you come here to stare at me? Unless you have something else to say, scram!
                return -1;
            case (50, 0):
                // $script:0706165507006640$
                // - Yeah, what do you want to talk about?
                switch (selection) {
                    // $script:0706165507006641$
                    // - What was that clone in the video?
                    case 0:
                        return 51;
                }
                return -1;
            case (51, 0):
                // $script:0706165507006642$
                // - Beats me. I never saw it before. This is a messed up thought, but could you imagine having 100 $npcNamePlural:11001688[gender:0]$ running around? Ugh, just having one of him is too much.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (51, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
