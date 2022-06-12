using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003518: Chiumbo
/// </summary>
public class _11003518 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0817044507008854$
    // - What is it?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0817044507008857$
                // - What is it?
                switch (selection) {
                    // $script:0817044507008858$
                    // - Tell me about the five auras.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0817044507008859$
                // - Kiyos live in Zulu Canyon to the northwest. If you capture a kiyo, you can take its Free Spirit.
                switch (selection) {
                    // $script:0817044507008860$
                    // - Tell me about Zulu Canyon.
                    case 0:
                        return 32;
                    // $script:0817044507008861$
                    // - Tell me about kiyos.
                    case 1:
                        return 33;
                }
                return -1;
            case (32, 0):
                // $script:0817044507008862$
                // - There are peaks upon peaks at Zulu Canyon. If you don't have wings, you won't be able to cross it.
                switch (selection) {
                    // $script:0817044507008863$
                    // - I need to ask something else.
                    case 0:
                        return 34;
                }
                return -1;
            case (33, 0):
                // $script:0817044507008864$
                // - The kiyos are agile. They don't like it when anyone gets close.
                switch (selection) {
                    // $script:0817044507008865$
                    // - I need to ask something else.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:0817044507008866$
                // - W-what?
                switch (selection) {
                    // $script:0817044507008867$
                    // - Tell me about Zulu Canyon.
                    case 0:
                        return 32;
                    // $script:0817044507008868$
                    // - Tell me about kiyos.
                    case 1:
                        return 33;
                }
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.SelectableDistractor,
            _ => NpcTalkButton.None,
        };
    }
}
