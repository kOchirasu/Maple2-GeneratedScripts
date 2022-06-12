using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003649: Kupa
/// </summary>
public class _11003649 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009206$
    // - Eh heh heh.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009207$
                // - And what brings a youngster like you here, hm?
                switch (selection) {
                    // $script:1109121007009208$
                    // - I'm looking for someone.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009209$
                // - Looking for someone, eh? Well, you're in luck! I know everybody here. So, who is it you're after, hm?
                switch (selection) {
                    // $script:1109121007009210$
                    // - Oh, I think I can find them on my own.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009211$
                // - Being tight-lipped about it, are you? $npcName:11003535[gender:1]$ trains her people well.
                switch (selection) {
                    // $script:1109121007009212$
                    // - You're with Dark Wind?
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009213$
                // - Eh heh heh! Surprised? Even us old timers can help out sometimes. Anyway, you run along and tell her, "Eyes. Alpha. Blonde hair."
                switch (selection) {
                    // $script:1109121007009214$
                    // - Will do!
                    case 0:
                        return 14;
                }
                return -1;
            case (14, 0):
                // $script:1109121007009215$
                // - Eh heh heh!
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
            (14, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
