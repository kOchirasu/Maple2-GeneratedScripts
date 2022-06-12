using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000185: Ms. Kim
/// </summary>
public class _11000185 : NpcScript {
    protected override int First() {
        return 50;
    }

    // Select 0:
    // $script:0831180407000773$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (50, 0):
                // $script:0831180407000778$
                // - $map:2000123$. How may I help you?
                switch (selection) {
                    // $script:0831180407000781$
                    // - What's been happening lately?
                    case 0:
                        return 53;
                    // $script:0831180407000782$
                    // - I was wondering how you're doing.
                    case 1:
                        return 54;
                }
                return -1;
            case (53, 0):
                // $script:0831180407000799$
                // - You mean the news? If I had good information, do you think I'd share it with you?
                return 53;
            case (53, 1):
                // $script:0831180407000800$
                // - Well, I would. Instead of seeking immediate gains, I invest for the future. That's my philosophy.
                return 53;
            case (53, 2):
                // $script:0831180407000801$
                // - Money or trust... which do you think is better for me in the long run? Heh, I'm still weighing my options.
                return -1;
            case (54, 0):
                // $script:0831180407000805$
                // - What is this? Are you hitting on me? I'm sorry, but I don't answer questions that have nothing to do with my work.
                return 54;
            case (54, 1):
                // $script:0831180407000806$
                // - I'm aware of the rumors about me. One of them says I'm divorced. Another says I'm a widow. 
                return 54;
            case (54, 2):
                // $script:0831180407000807$
                // - Some even say I'm the only daughter of Chairman Goldus. Ha, geez...
                return 54;
            case (54, 3):
                // $script:0831180407000808$
                // - I refuse to be gossip fodder. Don't these people have anything better to do with their lives?
                return 54;
            case (54, 4):
                // $script:0831180407000809$
                // - I'm sorry... I got carried away for a moment. Now, if you'll excuse me, I have developments to inspect.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (50, 0) => NpcTalkButton.SelectableDistractor,
            (53, 0) => NpcTalkButton.Next,
            (53, 1) => NpcTalkButton.Next,
            (53, 2) => NpcTalkButton.Close,
            (54, 0) => NpcTalkButton.Next,
            (54, 1) => NpcTalkButton.Next,
            (54, 2) => NpcTalkButton.Next,
            (54, 3) => NpcTalkButton.Next,
            (54, 4) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
