using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004296: Ghost
/// </summary>
public class _11004296 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011366$
    // - How lovely!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011369$
                // - Tell me, what's the one thing you must never, ever forget when you travel?
                switch (selection) {
                    // $script:1002141907011370$
                    // - Your wallet, of course.
                    case 0:
                        return 31;
                    // $script:1002141907011371$
                    // - You can't travel without a suitcase.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011372$
                // - Oh! I suppose your wallet <i>is</i> important. But is it the most important? Think harder!
                switch (selection) {
                    // $script:1002141907011373$
                    // - You can't travel without a suitcase.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1002141907011374$
                // - That's right! All of your most important things go in your suitcase, after all. If you're looking for something, you should always check your suitcase first.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
