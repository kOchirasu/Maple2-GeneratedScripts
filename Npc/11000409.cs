using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000409: Julian
/// </summary>
public class _11000409 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407001728$
    // - Welcome, $MyPCName$!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001729$
                // - The forest trail is too dangerous. We have to make it safe again, as soon as possible.
                return -1;
            case (20, 0):
                // $script:0831180407001730$
                // - $npcName:99000041$ are making this trail too dangerous to travel.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
