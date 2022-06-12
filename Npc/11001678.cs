using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001678: Bravos
/// </summary>
public class _11001678 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0629000607006437$
    // - You need anything, you just call out my name. Not that I'll come running, but maybe it'll give you good luck.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0629000607006440$
                // - Do you know why I'm called $npcName:11001545[gender:0]$?
                switch (selection) {
                    // $script:0629000607006441$
                    // - No clue.
                    case 0:
                        return 40;
                    // $script:0629000607006442$
                    // - Yes.
                    case 1:
                        return 50;
                    // $script:0706165507006635$
                    // - Let's talk about something else.
                    case 2:
                        return 60;
                }
                return -1;
            case (40, 0):
                // $script:0629000607006443$
                // - I'm so great I deserve a standing ovation! Haw! I can't believe you never heard of me. Well, remember me for next time.
                return 40;
            case (40, 1):
                // $script:0629000607006444$
                // - What, you come here to stare at me? Unless you have something else to say, scram!
                return -1;
            case (50, 0):
                // $script:0629000607006445$
                // - You probably already heard this, but listen anyway. They call me Bravos 'cause I'm so great I deserve a standing ovation! Get it?
                return 50;
            case (50, 1):
                // $script:0629000607006446$
                // - What, you come here to stare at me? Unless you have something else to say, scram!
                return -1;
            case (60, 0):
                // $script:0706165507006636$
                // - Yeah, what do you want to talk about?
                switch (selection) {
                    // $script:0706165507006637$
                    // - What's your standing in Blackstar, exactly?
                    case 0:
                        return 70;
                }
                return -1;
            case (70, 0):
                // $script:0706165507006638$
                // - Isn't it obvious? There's a reason I'm always picked for the best missions. The boss trusts me. I'll be an officer in no time, and then idiots like $npcName:11001686[gender:0]$ will have to do whatever I say.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Next,
            (50, 1) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.SelectableDistractor,
            (70, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
