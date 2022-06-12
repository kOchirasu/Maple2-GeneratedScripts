using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000671: Misplaced Book
/// </summary>
public class _11000671 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407002735$
    // - Yes, here!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002736$
                // - It's locked! You need a key!
                return -1;
            case (20, 0):
                // $script:0831180407002737$
                // - Make sure to return books to where they belong!
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
