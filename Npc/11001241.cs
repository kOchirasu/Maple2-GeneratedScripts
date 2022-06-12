using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001241: Minok
/// </summary>
public class _11001241 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1123214707004450$
    // - Sigh...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1123214707004453$
                // - Agh... I'm so disappointed in myself! I can barely get anywhere in the $map:2000350$... and it's all because of those stupid $item:90000014$.
                switch (selection) {
                    // $script:1123214707004454$
                    // - Why are you so eager to be here?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1123214707004455$
                // - Because everything is... <i>wrong</i>! This spreading darkness is turning our world cold and evil. So many fairies have already fallen trying to stem the tide, and I have to do my part too!
                switch (selection) {
                    // $script:1123214707004456$
                    // - You should leave this work to someone else.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1123214707004457$
                // - What? You think I can't do it just 'cause I'm fairfolk? What makes you so special? Typical human arrogance!
                return 32;
            case (32, 1):
                // $script:1123214707004458$
                // - The fairies have kept the darkness from touching Maple World since before you were in diapers. We never ask for anything in return, either. And what do we get for our troubles? The disdain of humans. Pah!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
