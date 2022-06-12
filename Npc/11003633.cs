using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003633: Anton
/// </summary>
public class _11003633 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009025$
    // - Goods for sale! Get your goods at various prices!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009026$
                // - Knick-knacks for sale! I've also got paddywhacks!
                switch (selection) {
                    // $script:1109121007009027$
                    // - Not interested.
                    case 0:
                        return 11;
                    // $script:1109121007009028$
                    // - You're no ordinary peddler...
                    case 1:
                        return 12;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009029$
                // - Heh! That was a test, $MyPCName$. And you failed.
                switch (selection) {
                    // $script:1109121007009030$
                    // - You know me?
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009031$
                // - Our mutual friend sent you, didn't she? Tell her, "the cuckoo bird goes caw caw."
                switch (selection) {
                    // $script:1109121007009032$
                    // - What does that even mean?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009033$
                // - Ahem! Pardon me, $male:sir,female:ma'am$, but if you're not buying anything, please make way for paying customers.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.SelectableDistractor,
            (13, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
