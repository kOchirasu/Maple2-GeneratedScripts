using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000960: Krin
/// </summary>
public class _11000960 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003325$
    // - Kyaaaaah! What? What?!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003327$
                // - Wah! What are you doing? Don't you know how to knock?!
                switch (selection) {
                    // $script:0831180407003328$
                    // - I didn't know someone was in here.
                    case 0:
                        // TODO: goto 21,22,23,24,25,26,27,28,29,30
                        return -1;
                }
                return -1;
            case (21, 0):
                // functionID=1 openTalkReward=True 
                // $script:0831180407003329$
                // - Get out of here! Oh, and take this with you.
                return -1;
            case (22, 0):
                // $script:0831180407003330$
                // - What are you doing? OUT!
                return -1;
            case (23, 0):
                // $script:0831180407003331$
                // - What are you doing? OUT!
                return -1;
            case (24, 0):
                // $script:0831180407003332$
                // - What are you doing? OUT!
                return -1;
            case (25, 0):
                // $script:0831180407003333$
                // - What is this? I can't focus...
                return -1;
            case (26, 0):
                // $script:0831180407003334$
                // - What is this? I can't focus...
                return -1;
            case (27, 0):
                // $script:0831180407003335$
                // - What is this? I can't focus...
                return -1;
            case (28, 0):
                // $script:0831180407003336$
                // - Ah, I was about to leave...
                return -1;
            case (29, 0):
                // $script:0831180407003337$
                // - Ah, I was about to leave...
                return -1;
            case (30, 0):
                // $script:0831180407003338$
                // - Ah, I was about to leave...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (22, 0) => NpcTalkButton.Close,
            (23, 0) => NpcTalkButton.Close,
            (24, 0) => NpcTalkButton.Close,
            (25, 0) => NpcTalkButton.Close,
            (26, 0) => NpcTalkButton.Close,
            (27, 0) => NpcTalkButton.Close,
            (28, 0) => NpcTalkButton.Close,
            (29, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
