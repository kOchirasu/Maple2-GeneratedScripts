using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003645: Mario
/// </summary>
public class _11003645 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009164$
    // - Hm... Interesting.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009165$
                // - Ah, $MyPCName$. You're just on time.
                switch (selection) {
                    // $script:1109121007009166$
                    // - You were expecting me?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009167$
                // - Based on your past travel patterns, current wind pressure readings, and my horoscope for today, I predicted a 96.9% chance that you would drop by.
                switch (selection) {
                    // $script:1109121007009168$
                    // - That's amazing.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009169$
                // - Anyway, how do you like my disguise?
                switch (selection) {
                    // $script:1109121007009170$
                    // - It's okay, I guess?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009171$
                // - I see. This is perhaps the greatest disguise I've ever designed, and you say such things...
                switch (selection) {
                    // $script:1109121007009172$
                    // - Um... Do you have a message for me?
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009173$
                // - Oh, yes, good point. Let's see... "Sunshine. Ocean. Wind."
                switch (selection) {
                    // $script:1109121007009174$
                    // - See you later.
                    case 0:
                        return 15;
                }
                return -1;
            case (15, 0):
                // $script:1109121007009175$
                // - According to my research, you will indeed see me again. But it will be sooner than you think...
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.SelectableDistractor,
            (14, 0) => NpcTalkButton.SelectableDistractor,
            (15, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
