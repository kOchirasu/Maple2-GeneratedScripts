using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003647: Olive
/// </summary>
public class _11003647 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1109121007009186$
    // - So much to do, so much mortal danger...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1109121007009187$
                // - What's have we here? A foreigner, in a place like this?
                switch (selection) {
                    // $script:1109121007009188$
                    // - I'm here on business.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1109121007009189$
                // - In that case, $npcName:11003535[gender:1]$ must have sent you. I see she can't be bothered to visit me in person... as usual.
                switch (selection) {
                    // $script:1109121007009190$
                    // - Uh, she tells me that you're doing very important work.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1109121007009191$
                // - That's kind of you to say, but I know the truth. Anyway, please tell her that I said, "Parrot. Shoes. Perfume."
                switch (selection) {
                    // $script:1109121007009192$
                    // - I'll make sure she gets the messsage.
                    case 0:
                        return 13;
                }
                return -1;
            case (13, 0):
                // $script:1109121007009193$
                // - Please remind her that us agents get lonely sometimes, would you?
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
