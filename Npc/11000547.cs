using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000547: Eka
/// </summary>
public class _11000547 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407002320$
    // - Ugh... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002322$
                // - Checkpoint... under attack... $map:02000076$... in danger...
                return -1;
            case (30, 0):
                // $script:0831180407002323$
                // - I-I'm okay... 
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
