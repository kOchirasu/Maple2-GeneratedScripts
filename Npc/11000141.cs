using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000141: Morren
/// </summary>
public class _11000141 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407000571$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407000574$
                // - Whoever you are, please help me! My... My boss was taken by them. Please save him!
                switch (selection) {
                    // $script:0831180407000575$
                    // - Don't worry, I'll save him.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0831180407000576$
                // - Thank you so much! I'm here alone and I didn't know what to do until you came along. I've been watching them, and there's a few things you need to know.
                return 31;
            case (31, 1):
                // $script:0831180407000577$
                // - First, don't step on the floor sensors marked red. They'll trip the alarm and you'll be in a world of hurt. I think if I hack into their security system, I should be able to turn off the alarm. Hm... 
                return 31;
            case (31, 2):
                // $script:0831180407000578$
                // - If you beat up a Blackdrake gang foot soldier, they're sure to call a superior for help. I suggest tossing an Energy Bomb at them, and then finishing them off quickly while they're stunned.
                return 31;
            case (31, 3):
                // $script:0831180407000579$
                // - Please, save my boss!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Next,
            (31, 1) => NpcTalkButton.Next,
            (31, 2) => NpcTalkButton.Next,
            (31, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
