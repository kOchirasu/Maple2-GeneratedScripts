using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000324: Cantata
/// </summary>
public class _11000324 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407001308$
    // - Hey, man! What's happening?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0910105907003794$
                // - It's not difficult to express your feelings in a tasteful way. Do it like the cool person you are!
                switch (selection) {
                    // $script:0910105907003795$
                    // - I have questions about emotes.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0910105907003796$
                // - Sure, fire away!
                switch (selection) {
                    // $script:0910105907003797$
                    // - What are emotes?
                    case 0:
                        return 32;
                    // $script:0910105907003798$
                    // - Where can I get emotes?
                    case 1:
                        return 33;
                    // $script:0910105907003799$
                    // - How can I use emotes?
                    case 2:
                        return 34;
                }
                return -1;
            case (32, 0):
                // $script:0910105907003800$
                // - How do you express yourself when you're happy or sad? Just typing in chat? No, no, that's not how we do it here. That's why you've got emotes, yo.
                return 32;
            case (32, 1):
                // $script:0910105907003801$
                // - When you're happy, laugh! Excited? Dance! Sad? Cry! There are tons of actions you can perform to express yourself to those around you, even without words. Make good use of them!
                switch (selection) {
                    // $script:0910105907003802$
                    // - I need to ask something else.
                    case 0:
                        return 35;
                }
                return -1;
            case (33, 0):
                // $script:0910105907003803$
                // - Some emotes are placed on your F1 - F12 keys by default. When you meet your friends, press F1 or F2 to greet them. If your friends are as sensible as you are, they'd greet you back in the same way!
                return 33;
            case (33, 1):
                // $script:0910105907003804$
                // - Aside from the 12 default actions, you can buy more actions at the Meret Market. Take a look at the Expression tab in the Premium Shop for all the available actions you can buy!
                switch (selection) {
                    // $script:0910105907003805$
                    // - I need to ask something else.
                    case 0:
                        return 35;
                }
                return -1;
            case (34, 0):
                // $script:0910105907003806$
                // - Take a look at the right side of the Chat window for the smiley face icon. Click it to open the emote window. If you buy emotes from the Meret Market, don't forget to learn the Emotes from the Inventory window.
                return 34;
            case (34, 1):
                // $script:0910105907003807$
                // - Got so many emotes that it's difficult to remember the hotkeys? Don't worry, I'll fill you in! You can use them by typing their commands into the Chat window. For example, if you want to use the Hello action, you can type /hello in the Chat window instead of pressing F1.
                return 34;
            case (34, 2):
                // $script:0910105907003808$
                // - Each emote has multiple commands, so check them in the emote window and use the ones you can remember easily.
                switch (selection) {
                    // $script:0910105907003809$
                    // - I need to ask something else.
                    case 0:
                        return 35;
                }
                return -1;
            case (35, 0):
                // $script:0910105907003810$
                // - Is there anything else you want to ask about emotes?
                switch (selection) {
                    // $script:0910105907003811$
                    // - What are emotes?
                    case 0:
                        return 32;
                    // $script:0910105907003812$
                    // - Where can I get emotes?
                    case 1:
                        return 33;
                    // $script:0910105907003813$
                    // - How can I use emotes?
                    case 2:
                        return 34;
                    // $script:0910105907003814$
                    // - I need to be going.
                    case 3:
                        return 36;
                }
                return -1;
            case (36, 0):
                // $script:0910105907003815$
                // - Don't think too hard, dawg. Just express yourself!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Next,
            (33, 1) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Next,
            (34, 1) => NpcTalkButton.Next,
            (34, 2) => NpcTalkButton.SelectableDistractor,
            (35, 0) => NpcTalkButton.SelectableDistractor,
            (36, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
