using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000432: Hans
/// </summary>
public class _11000432 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40;41
    }

    // Select 0:
    // $script:0831180407001803$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407001804$
                // - I came here to rest. Stop bothering me.
                return -1;
            case (40, 0):
                // $script:0831180407001805$
                // - ...
                switch (selection) {
                    // $script:0831180407001806$
                    // - $npcName:11000362[gender:0]$'s special...
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:0831180407001807$
                // - ...
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
