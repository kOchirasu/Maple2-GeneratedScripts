using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000259: Dark Wind Agent
/// </summary>
public class _11000259 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;20
    }

    // Select 0:
    // $script:0831180407001069$
    // - What seems to be the problem?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001070$
                // - I'd keep a low profile if I were you.
                return -1;
            case (20, 0):
                // $script:0831180407001071$
                // - It's going to be tough, but we have to comb through the records for clues. We can't let them catch us off guard again.
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
