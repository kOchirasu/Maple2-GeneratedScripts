using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000673: Anonymous Prisoner's Diary
/// </summary>
public class _11000673 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180407002739$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407002740$
                // - <font color="#909090">(This looks like an old journal. You open the faded cover and turn to a dusty page.)</font>
                return 10;
            case (10, 1):
                // $script:0831180407002741$
                // - "When I discovered the secret passageway, I was excited beyond measure. I thought I could finally escape."
                return 10;
            case (10, 2):
                // $script:0831180407002742$
                // - "But at the other end of the passageway, an endless abyss awaited me. Is it really impossible to escape from this misery?"
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
