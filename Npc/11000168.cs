using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000168: Kay
/// </summary>
public class _11000168 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1103095507004409$
    // - Welcome to the Maple OX Quiz!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1103095507004412$
                // - How'd you like the quiz? Pretty tricky, right? Come back next time, because there's more where that came from!
                switch (selection) {
                    // $script:1103095507004413$
                    // - I lost. I <i>lost</i>. I <i>never</i> lose!
                    case 0:
                        return 31;
                    // $script:1103095507004414$
                    // - So... what are the questions for the next quiz?
                    case 1:
                        return 32;
                    // $script:1103095507004415$
                    // - Congratulations on being the host.
                    case 2:
                        return 33;
                }
                return -1;
            case (31, 0):
                // $script:1103095507004416$
                // - Don't lose heart. You can always come back and try again next time. I'll be rooting for you, $MyPCName$!
                return -1;
            case (32, 0):
                // $script:1103095507004417$
                // - You want me to help you cheat? No. No way. I can't believe you'd ask me that...
                return -1;
            case (33, 0):
                // $script:1103095507004418$
                // - Thank you! It's a dream come true, to be honest. A dream come true...
                //   <font color="#909090">(He starts weeping.)</font>
                switch (selection) {
                    // $script:1103095507004419$
                    // - Don't cry, little raccoon guy.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1103095507004420$
                // - I-I won't! Sorry. I just wasn't expecting anyone to congratulate me. I'll do my best not to let you down as a host, $MyPCName$!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
