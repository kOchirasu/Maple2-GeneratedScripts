using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000892: Naina
/// </summary>
public class _11000892 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003260$
    // - Ugh... I'm still half asleep... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003261$
                // - May the light of the forest be with you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
