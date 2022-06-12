using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000429: Remy
/// </summary>
public class _11000429 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;41
    }

    // Select 0:
    // $script:0831180407001785$
    // - Ah, the smell of the sea!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001787$
                // - I just ate lunch, and I'm already hungry. 
                return -1;
            case (40, 0):
                // $script:0831180407001788$
                // - Mm? Do I know you?
                switch (selection) {
                    // $script:0831180407001789$
                    // - Come try $npcName:11000362[gender:0]$'s $itemPlural:30000140$!
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001790$
                // - $itemPlural:30000140$? That sounds delicious! I'll be back for those.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
