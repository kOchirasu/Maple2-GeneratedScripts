using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000324: Cantata
/// </summary>
public class _11000324 : NpcScript {
    internal _11000324(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001308$ 
                // - Hey, man! What's happening?
                return true;
            case 30:
                // $script:0910105907003794$ 
                // - It's not difficult to express your feelings in a tasteful way. Do it like the cool person you are!
                switch (selection) {
                    // $script:0910105907003795$
                    // - I have questions about emotes.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0910105907003796$ 
                // - Sure, fire away!
                switch (selection) {
                    // $script:0910105907003797$
                    // - What are emotes?
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0910105907003798$
                    // - Where can I get emotes?
                    case 1:
                        Id = 33;
                        return false;
                    // $script:0910105907003799$
                    // - How can I use emotes?
                    case 2:
                        Id = 34;
                        return false;
                }
                return true;
            case 32:
                // $script:0910105907003800$ 
                // - How do you express yourself when you're happy or sad? Just typing in chat? No, no, that's not how we do it here. That's why you've got emotes, yo.
                // $script:0910105907003801$ 
                // - When you're happy, laugh! Excited? Dance! Sad? Cry! There are tons of actions you can perform to express yourself to those around you, even without words. Make good use of them!
                switch (selection) {
                    // $script:0910105907003802$
                    // - I need to ask something else.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 33:
                // $script:0910105907003803$ 
                // - Some emotes are placed on your F1 - F12 keys by default. When you meet your friends, press F1 or F2 to greet them. If your friends are as sensible as you are, they'd greet you back in the same way!
                // $script:0910105907003804$ 
                // - Aside from the 12 default actions, you can buy more actions at the Meret Market. Take a look at the Expression tab in the Premium Shop for all the available actions you can buy!
                switch (selection) {
                    // $script:0910105907003805$
                    // - I need to ask something else.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 34:
                // $script:0910105907003806$ 
                // - Take a look at the right side of the Chat window for the smiley face icon. Click it to open the emote window. If you buy emotes from the Meret Market, don't forget to learn the Emotes from the Inventory window.
                // $script:0910105907003807$ 
                // - Got so many emotes that it's difficult to remember the hotkeys? Don't worry, I'll fill you in! You can use them by typing their commands into the Chat window. For example, if you want to use the Hello action, you can type /hello in the Chat window instead of pressing F1.
                // $script:0910105907003808$ 
                // - Each emote has multiple commands, so check them in the emote window and use the ones you can remember easily.
                switch (selection) {
                    // $script:0910105907003809$
                    // - I need to ask something else.
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0910105907003810$ 
                // - Is there anything else you want to ask about emotes?
                switch (selection) {
                    // $script:0910105907003811$
                    // - What are emotes?
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0910105907003812$
                    // - Where can I get emotes?
                    case 1:
                        Id = 33;
                        return false;
                    // $script:0910105907003813$
                    // - How can I use emotes?
                    case 2:
                        Id = 34;
                        return false;
                    // $script:0910105907003814$
                    // - I need to be going.
                    case 3:
                        Id = 36;
                        return false;
                }
                return true;
            case 36:
                // $script:0910105907003815$ 
                // - Don't think too hard, dawg. Just express yourself!
                return true;
            default:
                return true;
        }
    }
}
