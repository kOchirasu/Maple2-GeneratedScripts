using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004332: Lanemone
/// </summary>
public class _11004332 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;30
    }

    // Select 0:
    // $script:1102172107011635$
    // - Hm...
    // Select 20:
    // $script:1010140307011563$
    // - Mm?
    protected override int Select() => Random(0, 20);

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1102172107011636$
                // - I sense something powerful. Something... wrong.
                return -1;
            case (30, 0):
                // $script:1010140307011564$
                // - Hey, you!
                return 30;
            case (30, 1):
                // $script:1010140307011565$
                // - Long time no see.
                return 30;
            case (30, 2):
                // $script:1010140307011566$
                // - I wasn't expecting to run into you here.
                switch (selection) {
                    // $script:1010140307011567$
                    // - What brings you here?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:1010140307011568$
                // - Well, that geezer—erm, Mr. $npcName:11004233[gender:0]$ sent me here.
                return 40;
            case (40, 1):
                // $script:1010140307011569$
                // - The Frontier Foundation caught wind of something quite unexpected here on this continent that warranted investigation.
                return 40;
            case (40, 2):
                // $script:1010140307011570$
                // - Traces of lapenta energy!
                return 40;
            case (40, 3):
                // $script:1010140307011571$
                // - But I suppose you already knew that.
                return 40;
            case (40, 4):
                // $script:1010140307011572$
                // - You should be careful. There's no telling what kinds of dangers lurk in this land.
                switch (selection) {
                    // $script:0111232407012699$
                    // - You too. Take care of yourself.
                    case 0:
                        return 50;
                }
                return -1;
            case (50, 0):
                // $script:0111232407012700$
                // - Oh, you don't have to worry about me.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Next,
            (30, 2) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Next,
            (40, 2) => NpcTalkButton.Next,
            (40, 3) => NpcTalkButton.Next,
            (40, 4) => NpcTalkButton.SelectableDistractor,
            (50, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
