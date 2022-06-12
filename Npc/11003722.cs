using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003722: 
/// </summary>
public class _11003722 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30;40
    }

    // Select 0:
    // $script:1127164207009322$
    // - Good to see you. 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1127164207009323$
                // - Hi there, $MyPCName$. I'm Zakum, but little. You can call me Little Zakum.
                switch (selection) {
                    // $script:1127164207009324$
                    // - Where's the real Zakum?
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:1127164207009325$
                // - Not happy with Little Zakum? That's fine. You can find the real deal at the Mirror Gate. Just check your Challenge Map! 
                return -1;
            case (30, 0):
                // $script:1130102607009374$
                // - Hey there! It's me, Little Zakum. You know, Zakum, but little. I have a gift for you!
                switch (selection) {
                    // $script:1130104707009376$
                    // - Oh, oh, what is it?
                    case 0:
                        // TODO: goto 31
                        // TODO: gotoFail 32
                        return -1;
                }
                return -1;
            case (31, 0):
                // functionID=1 openTalkReward=True 
                // $script:1130104707009377$
                // - You've got to open it to find out! I hope you like this gift to you from me, Little Zakum.
                return -1;
            case (32, 0):
                // $script:1204155907009629$
                // - You've got to open it to find out! But, uh, it looks like you don't have enough room in your bag. Come back when you're ready for a gift from yours truly, Little Zakum!
                return -1;
            case (40, 0):
                // $script:1130102607009375$
                // - Hey there! It's me, Little Zakum. You know, Zakum, but little. I have a gift for you, and... Hey, I already gave you a gift! You cheeky hero, you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
