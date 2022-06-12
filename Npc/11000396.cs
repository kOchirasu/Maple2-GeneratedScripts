using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000396: Ivan
/// </summary>
public class _11000396 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407001606$
    // - Why me? What did I do?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001608$
                // - Keep those thugs away from me...
                return -1;
            case (30, 0):
                // $script:0831180407001609$
                // - So hungry...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
