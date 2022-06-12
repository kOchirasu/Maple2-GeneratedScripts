using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000159: Tommy
/// </summary>
public class _11000159 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000670$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000672$
                // - This place is extremely dangerous. Be careful not to fall.
                return -1;
            case (30, 0):
                // $script:0831180407000673$
                // - The others must be quite anxious, since they don't know what's going on.
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
