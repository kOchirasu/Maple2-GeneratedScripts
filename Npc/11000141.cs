using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000141: Morren
/// </summary>
public class _11000141 : NpcScript {
    internal _11000141(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000571$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0831180407000574$ 
                // - Whoever you are, please help me! My... My boss was taken by them. Please save him!
                switch (selection) {
                    // $script:0831180407000575$
                    // - Don't worry, I'll save him.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000576$ 
                // - Thank you so much! I'm here alone and I didn't know what to do until you came along. I've been watching them, and there's a few things you need to know.
                // $script:0831180407000577$ 
                // - First, don't step on the floor sensors marked red. They'll trip the alarm and you'll be in a world of hurt. I think if I hack into their security system, I should be able to turn off the alarm. Hm... 
                // $script:0831180407000578$ 
                // - If you beat up a Blackdrake gang foot soldier, they're sure to call a superior for help. I suggest tossing an Energy Bomb at them, and then finishing them off quickly while they're stunned.
                // $script:0831180407000579$ 
                // - Please, save my boss!
                return true;
            default:
                return true;
        }
    }
}
